from __future__ import print_function
import threading
import os, csv
import time
import numpy as np
filepath = os.path.dirname(os.path.abspath(__file__))
g = []


def read_data(filename, has_header=True):
    data, header = [], None
    with open(filename, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        if has_header:
            header = spamreader.next()
        for row in spamreader:
            data.append(row)
    return (np.array(data), np.array(header))

def load_graphs(threadName, filename):
    data, _ = read_data(filename, has_header=False)
    graphs = []
    for line in data:
        if line[0] == 't':
            G = Graph(id=int(line[2]))
            graphs.append(G)
        else:
            if line[0] == 'v':
                v = Vertex(id=int(line[1]), label=line[2])
                graphs[len(graphs)-1].add_vertex(vertex=v)
            elif line[0] == 'e':
                e = Edge(label=line[3],
                         from_vertex=graphs[len(graphs)-1].get_vertex(id=int(line[1])),
                         to_vertex=graphs[len(graphs)-1].get_vertex(id=int(line[2])))
                graphs[len(graphs)-1].add_edge(edge=e)
    return graphs[0]

class Vertex():
    """
        Implementation of an Vertex in a graph
    """
    visited = False
    dfs_id = 0
    def __init__(self, id, label):
        self.id = id
        self.label = label

class Edge():
    """
        Implementation of an Edge in a graph
    """
    def __init__(self, label, from_vertex, to_vertex):
        self.label = label
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex

    def connected_to(self, vertex):
        return vertex.id == self.from_vertex.id or \
               vertex.id == self.to_vertex.id

class Graph():
    """
        Implementation of a Graph
    """
    edges, vertices = [], []
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.vertices = []
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
    def add_edge(self, edge):
        self.edges.append(edge)
    def get_vertex(self, id):
        for v in self.vertices:
            if v.id == id:
                return v
        raise KeyError('No vertex with the id was found in graph')
    def adjacent_edges(self, vertex):
        adj_edges = []
        for e in self.edges:
            if e.connected_to(vertex):
                adj_edges.append(e)
        return adj_edges
    def adjacent_vertices(self, vertex):
        adj_edges = self.adjacent_edges(vertex)
        adj_vertices = []
        for e in adj_edges:
            if e.from_vertex.id == vertex.id:
                adj_vertices.append(e.to_vertex)
            else:
                adj_vertices.append(e.from_vertex)
        return adj_vertices
    def adjacent_connections(self, vertex):
        adj_edges = self.adjacent_edges(vertex)
        adj_connections = []
        for e in adj_edges:
            if e.from_vertex.id == vertex.id:
                adj_connections.append((e, e.to_vertex))
            else:
                adj_connections.append((e, e.from_vertex))
        # Sort according to node index
        ids = [w.id for e,w in adj_connections]
        idx = np.argsort(ids)
        adj_connections = [adj_connections[i] for i in idx]
        return adj_connections
    def generate_vertices(self):
        for e in self.edges:
            for v in [e.from_vertex, e.to_vertex]:
                v.id = v.dfs_id
                if not v in self.vertices:
                    self.add_vertex(vertex=v)
    def get_max_vertex(self):
        ids = [v.id for v in self.vertices]
        idx = np.argsort(ids)[::-1]
        return self.vertices[idx[0]]
    def get_max_dfs_id_vertex(self):
        vertices_id = []
        for i, v in enumerate(self.vertices):
            if not v.dfs_id is None:
                vertices_id.append(i)
        if len(vertices_id) > 0:
            ids = [self.vertices[i].id for i in vertices_id]
            idx = np.argsort(ids)[::-1]
            return self.vertices[idx[0]]
        else:
            return []
    def get_min_vertex(self):
        ids = [v.id for v in self.vertices]
        idx = np.argsort(ids)
        return self.vertices[idx[0]]
    def contains_vertex_id(self, id):
        for v in self.vertices:
            if v.id == id:
                return True
        return False
    def contains_edge(self, from_id, to_id):
        for e in self.edges:
            if (e.from_vertex.id == from_id and e.to_vertex.id == to_id) or \
               (e.to_vertex.id == from_id and e.from_vertex.id == to_id):
               return True
        return False
    def reverse_graph(self):
        for e in self.edges:
            tmp_from = e.from_vertex
            e.from_vertex = e.to_vertex
            e.to_vertex = tmp_from
        self.edges = self.edges[::-1]
        self.vertices = self.vertices[::-1]
    def print_graph(self):
        DFScode = G2DFS(self)
        for line in DFScode:
            print(line)
    def get_edge(self, from_id, to_id):
        for e in self.edges:
            if (e.from_vertex.id == from_id and e.to_vertex.id == to_id) or \
               (e.to_vertex.id == from_id and e.from_vertex.id == to_id):
               return e
        return None
    def reset(self):
        for v in self.vertices:
            v.visited = False
            v.dfs_id = None


def G2DFS(G):
    DFScode = []
    for e in G.edges:
        DFScode.append((e.from_vertex.id, e.to_vertex.id,
            e.from_vertex.label, e.to_vertex.label, e.label))
    return DFScode

class myThread (threading.Thread):
    def __init__(self, threadID, name, fname):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.fname = fname
    def run(self):
        print('starting' + self.name) 
        # Get lock to synchronize threads
        threadLock.acquire()
        g.append(load_graphs(self.name, self.fname))
        # Free lock to release next thread
        threadLock.release()


threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", "data/1.txt")
thread2 = myThread(2, "Thread-2", "data/2.txt")

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")


for i in g:
    i.print_graph()
    print()
