from __future__ import print_function
import os, sys
from algorithms import *
from algorithms import algo 
from algorithms import load_graphs
filepath = os.path.dirname(os.path.abspath(__file__))
import time
import threading
start_time = time.time()

class Node:
    
    def __init__(self):
        self.dfs_code = []
        self.id_list = []
        self.nodes = {}
        
    def __get_all__(self):
        x = []
        
        for key, node in self.nodes.iteritems(): 
            if node.dfs_code:
                x.append([node.dfs_code])
            
            x += node.__get_all__()
                
        return x
    
    def __print_all__(self):
        x = []
        
        for key, node in self.nodes.iteritems(): 
            if node.dfs_code:
                print(node.dfs_code)
                print(node.id_list)
            	print('')
            node.__print_all__()
        
        return     
                	
    def __str__(self):
        return self.dfs_code
    
    def __insert__(self, arr_dfs_code, pos = 0):
        temp = self
        for i in range(0,len(arr_dfs_code[0])):
            current_dfs_code = arr_dfs_code[0][i]
            if current_dfs_code not in temp.nodes:
                temp.nodes[current_dfs_code] = Node()
            temp.nodes[current_dfs_code].dfs_code = current_dfs_code
            temp_id = sorted(temp.nodes[current_dfs_code].id_list + arr_dfs_code[1])
            temp_id = list(set(temp_id))
            temp.nodes[current_dfs_code].id_list = temp_id
            temp = temp.nodes[current_dfs_code]            
    	return True
    
    
    def __add_id__(self, arr_dfs_code, gid) :
        temp = self
        for i in range(0,len(arr_dfs_code)):
            current_dfs_code = arr_dfs_code[i]
            if current_dfs_code in temp.nodes: 
                temp = temp.nodes[current_dfs_code]
            else: 
                return False 
        
        temp.id_list.append(gid)
        return True
        
    
    def __search__(self,arr_dfs_code, pos = 0):
        temp = self
        for i in range(0,len(arr_dfs_code)):
            current_dfs_code = arr_dfs_code[i]
            if current_dfs_code in temp.nodes: 
                temp = temp.nodes[current_dfs_code]
            else: 
                return False 
        
        return True
        
class Trie:
  
   def __init__(self):
        self.root = Node()
        
   def insert(self, pattern):
        self.root.__insert__(pattern)
        
   def get_all(self):
        return self.root.__get_all__()
	
   def print_all(self):
   		self.root.__print_all__()
   		
   def search(self, pattern):
        return self.root.__search__(pattern)
        
   def add_id(self, pattern, gid):
       return self.root.__add_id__(pattern,gid)

threadLock = threading.Lock()
graphs = []  
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
        graphs.append(load_graphs(self.name, self.fname))
        # Free lock to release next thread
        threadLock.release()


def main(filename='data/test.txt', min_sup=20):
#    filename = os.path.join(filepath, filename)
    threads = []
       
	# Create new threads
    thread1 = myThread(1, "Thread-1", "datag/1.txt")
    thread2 = myThread(2, "Thread-2", "datag/2.txt")
    thread3 = myThread(3, "Thread-3", "datag/3.txt")
    thread4 = myThread(4, "Thread-4", "datag/4.txt")
    thread5 = myThread(5, "Thread-5", "datag/5.txt")
    thread6 = myThread(6, "Thread-6", "datag/6.txt")
    thread7 = myThread(7, "Thread-7", "datag/7.txt")
    thread8 = myThread(8, "Thread-8", "datag/8.txt")
    thread9 = myThread(9, "Thread-9", "datag/9.txt")
    thread10 = myThread(10, "Thread-10", "datag/10.txt")
    thread11 = myThread(11, "Thread-11", "datag/11.txt")
    thread12 = myThread(12, "Thread-12", "datag/12.txt")
    thread13 = myThread(13, "Thread-13", "datag/13.txt")
    thread14 = myThread(14, "Thread-14", "datag/14.txt")
    thread15 = myThread(15, "Thread-15", "datag/15.txt")
    thread16 = myThread(16, "Thread-16", "datag/16.txt")
    thread17 = myThread(17, "Thread-17", "datag/17.txt")
    thread18 = myThread(18, "Thread-18", "datag/18.txt")
    thread19 = myThread(19, "Thread-19", "datag/19.txt")
    thread20 = myThread(20, "Thread-20", "datag/20.txt")
    thread21 = myThread(21, "Thread-21", "datag/21.txt")
    thread22 = myThread(22, "Thread-22", "datag/22.txt")
    thread23 = myThread(23, "Thread-23", "datag/23.txt")
    thread24 = myThread(24, "Thread-24", "datag/24.txt")
    thread25 = myThread(25, "Thread-25", "datag/25.txt")

	# Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()
    thread17.start()
    thread18.start()
    thread19.start()
    thread20.start()
    thread21.start()
    thread22.start()
    thread23.start()
    thread24.start()
    thread25.start()
    
	# Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    threads.append(thread4)
    threads.append(thread5)
    threads.append(thread6)
    threads.append(thread7)
    threads.append(thread8)
    threads.append(thread9)
    threads.append(thread10)
    threads.append(thread11)
    threads.append(thread12)
    threads.append(thread13)
    threads.append(thread14)
    threads.append(thread15)
    threads.append(thread16)
    threads.append(thread17)
    threads.append(thread18)
    threads.append(thread19)
    threads.append(thread20)
    threads.append(thread21)
    threads.append(thread22)
    threads.append(thread23)
    threads.append(thread24)
    threads.append(thread25)

	# Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")


    for i in graphs:
        i.print_graph()
        print()
		
    #graphs = load_graphs(filename)
    print('end')
    n = len(graphs)
    extensions = []
    extensions_id = []
    start_time = time.time()
    algo([], graphs, min_sup=min_sup, extensions=extensions,extensions_id=extensions_id)
    ct = 0
    ans = []
    ans_id = []
    ct = 0
    for i in extensions_id:
    	if i not in ans_id:
    		ans_id.append(i) 
    for i in range(0,len(ans_id)):
        ans_id[i][1].sort()
    for i in ans_id:
    	if i[0]:
    		ct += 1
    		print('Subgraph %d' % (ct))
    		ct1 = 0
    		for _i in i:
    			if ct1 == 0:
    				ct1 += 1
    				for _a in _i:
        				print(_a)			
    			else: 
    				print("The above fragment is present in the following graphs %s" % _i)
        			print('')
    return ans_id


V = []
max_len = 3
queryAll = []
def generate_subgraph(X,Y,Q):
    if len(X) == max_len: 
        return
    if X:
        T = set()
        for x in X:
            for a in Q.adjacent_vertices(x):
                if ((a not in Y) and (a not in X)):
                    T.add(a)
                  
    else:
        T = V
    Y1 = set(Y)
    for vertex in T:
        X.append(vertex)
        if (len(X) > 1):
		    #print('Subgraph : ')
		    #for waste in X:
		    #    print("%s %s" % (waste.id,waste.label))
		    #Function to create a DFS code from the obtained output
		    # DFSOG -> DFS of the output graph 
		    DFSOG = []
		    for i in range(0,len(X)-1):
		        #DFSOG.append((X[i].id,X[i+1].id,X[i].label,X[i+1].label,Q.get_edge(X[i].id,X[i+1].id).label))
		        DFSOG.append((X[i].id,X[i+1].id,X[i].label,X[i+1].label,'_'))
			#code for converting dfscode to correct dfs code 
		    hashmap = {} #A hashmap for id conversion
		    count = 0
		    for i in DFSOG:
		        u,v,_u,_v,_uv = i
		        if u in hashmap: 
		            v #Waste block, Same as continue
		        else :
		            hashmap[u] = count
		            count += 1
		            
		        if v in hashmap:
		            continue
		        else :
		            hashmap[v] = count
		            count += 1
		            
		    DFSCODE = []
		    for i in DFSOG:
		        u,v,_u,_v,_uv = i
		        DFSCODE.append((hashmap.get(u), hashmap.get(v), _u, _v, _uv))
		        
		    #print(DFSCODE)
		    queryAll.append(DFSCODE)
        generate_subgraph(X,Y1,Q)
        X.remove(vertex)
        Y1.add(vertex)
   


def getMatched():
    ans = 0
    for i in range(0,275):
        ans += 1
    return ans


ans = main()
#print(ans)
trie = Trie() 
for i in ans:
    if i[0]:
        trie.insert(i)
print('The elements of the prefix tree are')
trie.print_all()

#Loading and generating the query graph
filename = os.path.join(filepath, "datag/q6.txt")
query = load_graphs("",filename)
query_graph = query
#print('The given query Graph is')
#Graph.print_graph(query_graph)
print()
#printing the vertices of the query graph
for v in query_graph.vertices: 
    V.append(v)
    
max_len = len(V)
generate_subgraph([],set(),query_graph)
#pattern = [(0, 1, 'a', 'b', '_'),(1, 2, 'b', 'a', '_')]

#print(trie.search(pattern))
countans = 0
for x in queryAll:
#    print('The pattern going to search : %s' % x)
    val = trie.search(x)
#    print(val)
    if val == True: 
        countans += 1

#print("--- %s seconds ---" % (time.time() - start_time))

print("Number of frequent fragments generated  %d" % (len(ans) - 1))
print("The number of subgraphs generated  %d" % len(queryAll))
print('Matched %d' % countans)
print('Do you want to insert the new graph? Y or N')
inp = raw_input()
  
if inp == 'Y':
    filename = os.path.join(filepath, "data/query.txt")
    query = load_graphs("",filename)
    new_graph = query
    V = []
    for v in new_graph.vertices :
        V.append(v)
    max_len = len(V)
    queryAll = []
    generate_subgraph([],set(),new_graph)
    print('Enter the id of the new graph')
    new_graph_id = raw_input()
    for x in queryAll:
        if trie.search(x) == True: #if it is a frequent fragment
            trie.add_id(x, new_graph_id)
    
    print('The elements of the prefix tree after inserting a new graph are')
    trie.print_all()
    
