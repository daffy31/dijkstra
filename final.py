import sys

# ΠΙΝΑΚΑΣ ΣΥΣΧΕΤΙΣΗΣ ΑΠΟΣΤΑΣΕΩΝ ΚΟΜΒΩΝ
graph =   [ [0,1,0,0,0,0,0,0],
			[1,0,2,0,0,0,0,0],
			[0,2,0,2,2,0,0,4],
		    [0,0,2,0,0,0,0,0],
			[0,0,2,0,0,3,5,0],
			[0,0,0,0,3,0,0,0],
			[0,0,0,0,5,0,0,3],
			[0,0,4,0,0,0,3,0],]

allDist=[]

# DICT ΣΥΣΧΕΤΙΣΗΣ ΚΟΜΒΩΝ (key) ΜΕ ΓΕΙΤΟΝΙΚΟΥΣ ΚΟΜΒΟΥΣ
res = {0: [1], 
       1: [0, 2], 
       2: [1,3,4,7], 
       3: [2], 
       4: [2,5,6], 
       5: [4], 
       6: [4,7], 
       7: [2,6]
       }
nodesSolutionMatrix = []
nodes=[]


def dijkstra(src):
    
    dist = [sys.maxsize] * len(graph)
    dist[src] = 0
    boolTable = [False] * len(graph)

    for i in range(len(graph)):
        x = minDist(dist, boolTable)
        boolTable[x] = True
  
        for y in range(len(graph)):
            if graph[x][y] > 0 and boolTable[y] == False and dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
    
    printSolution(dist, nodesSolutionMatrix)


def printSolution(dist, nodesSolutionMatrix):
    dist_sum = 0
    case_list=[]
    print("\n ΟΜΑΔΑ",i,"\n")
    
    print("KOMBOΣ \t ΑΘΡΟΙΣΜΑ ΑΠΟΣΤΑΣΗΣ ΚΑΛΥΤΕΡΗΣ ΔΙΑΔΡΟΜΗΣ ΑΠΟ","N(",i,")")
    for node in range(len(graph)):
        dist_sum = dist_sum + dist[node]
        print("N",node+1, "\t", dist[node])
    print("TO ΑΘΡΟΙΣΜΑ ΤΩΝ ΚΑΛΥΤΕΡΩΝ ΔΥΝΑΤΩΝ ΔΙΑΔΡΟΜΩΝ ΟΛΩΝ ΤΩΝ ΚΟΜΒΩΝ ΑΠΟ ΤΟΝ ","N(",i,") ΒΑΣΕΙ DIJKSTRA","EINAI:",dist_sum,"\n")
    nodesSolutionMatrix.append(dist_sum) 
    nodes.append(i)


def minDist(dist, boolTable):
    min = sys.maxsize
    for u in range(len(graph)):
        if dist[u] < min and boolTable[u] == False:
            min = dist[u]
            min_index = u
    return min_index


def printAllPathsUtil(u, d, visited, path, allDist):
    # Mark the current node as visited and store in path
    visited[u]= True
    path.append(u)
    # AN H ΠΗΓΗ ΕΙΝΑΙ ΙΔΙΑ ΜΕ ΤΟΝ ΠΡΟΟΡΙΣΜΟ ΤΥΠΩΣΕ ΤΗ ΔΙΑΔΡΟΜΗ
    if u == d:
        print("ΔΙΑΔΡΟΜΗ ΜΕΣΩ ΚΟΜΒΩΝ",path)
        pathDistance(path,graph,allDist)
    else:
        # ΑΝ Ο ΚΟΜΒΟΣ (source) ΕΙΝΑΙ ΔΙΑΦΟΡΟΣ TOY Destination
        # ΕΠΑΝΕΛΑΒΕ ΓΙΑ ΟΛΟΥΣ ΤΟΥΣ ΓΕΙΤΟΝΙΚΟΥΣ
        
        for j in res[u]:
            # print(self.graph[u])
            if visited[j]== False:
                printAllPathsUtil(j, d, visited, path, allDist)
    # ΑΦΟΙΡΟΥΜΕ ΤΟΝ ΤΩΡΙΝΟ ΚΟΜΒΟ ΑΠΟ ΤΟ PATH ΚΑΙ ΤΟΝ ΜΑΡΚΑΡΟΥΜΕ UNVISITED
    path.pop()
    visited[u]= False

    
def pathDistance(path,graph,allDist):
    sum = 0
    for q in range(len(path)-1):
        buffer = graph[path[q]][path[q+1]]
        sum = sum + buffer
    allDist.append(path.copy())
    print("ME ΣΥΝΟΛΙΚΗ ΑΠΟΣΤΑΣΗ",sum,"\n")
    

# ΟΛΕΣ ΟΙ ΠΙΘΑΝΕΣ ΔΙΑΔΡΟΜΕΣ ΑΠΟ Source ΣΕ Destination
def printAllPaths(s, d):
    # ΠΙΝΑΚΑΣ ΑΛΗΘΕΙΑΣ ΓΙΑ ΤΟ ΑΝ ΕΧΟΥΜΕ ΕΞΕΤΑΣΕΙ ΤΟΝ ΚΟΜΒΟ (ΞΕΚΙΝΑΜΕ ΜΕ ΟΛΑ false)
    visited =[False]*(len(graph))
    # ΛΙΣΤΑ ΓΙΑ ΤΗ ΔΙΑΔΡΟΜΗ
    path = []
    # RECURSION συναρτηση
    printAllPathsUtil(s, d, visited, path,allDist)


for i in range(len(graph)):
 dijkstra(i)


for x in range(len(graph)):
    for y in range(len(graph)):
        s = x ; d = y
        print ("ΤΑ ΠΙΘΑΝΑ ΜΟΝΟΠΑΤΙΑ ΑΠΟ % d ΣΕ % d" %(s, d),"EINAI : \n")
        
        printAllPaths(s, d)
        print("---")

# ΜΕΤΑΤΡΟΠΗ ΛΙΣΤΑΣ ΣΕ DICT
new_dict = {nodes: nodesSolutionMatrix for nodes,
            nodesSolutionMatrix in zip(nodes, nodesSolutionMatrix)}

# SORTARISMA
sorted_i = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1])}

print("\nΛΙΣΤΑ ΟΜΑΔΩΝ ΚΑΤΑ ΑΥΞΟΥΣΑ ΣΕΙΡΑ",sorted_i)





