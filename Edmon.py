from collections import defaultdict 
  
class EdmonKarps: 
  
    def __init__(self,matrixAsGraph):
        self.matrixAsGraph = matrixAsGraph
        #storing the oroginal overlap adj matrix , which later helps us in determining the cut
        self.org_matrixAsGraph = [i[:] for i in matrixAsGraph] 
        self. noOfRows = len(matrixAsGraph) 
        self.noOfCols = len(matrixAsGraph[0])

    def breadhFirstSearch(self,s, t, parent): 
  
        #no node is visited yet
        visited =[False]*(self.noOfRows) 
  
        que=[] 
  
        # Make the source node visited and add it to the que
        que.append(s)
        visited[s] = True
  
        # Standard breadhFirstSearch Loop 
        while que: 
  
            #Deque a vertex from que and print it 
            u = que.pop(0) 
  
            #BFS APPROACH -> if the neigbhbouring node is not visited, mark it and add it to the que
            for index, val in enumerate(self.matrixAsGraph[u]): 
                if visited[index] == False and val > 0 : 
                    que.append(index) 
                    visited[index] = True
                    parent[index] = u 
  
        return True if visited[t] else False
          
    
    def depthFirstSearch(self, matrixAsGraph,s,visited):
        visited[s]=True
        for i in range(len(matrixAsGraph)):
            if matrixAsGraph[s][i]>0 and not visited[i]:
                self.depthFirstSearch(matrixAsGraph,i,visited)
  
    # Returns the min-cut of the given matrixAsGraph 
    def minCut(self, source, sink): 
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.noOfRows) 
  
        maxFlow = 0
        while self.breadhFirstSearch(source, sink, parent) : 
  
            pathValue = float("Inf") 
            s = sink
            
            while(s != source): 
                pathValue = min (pathValue, self.matrixAsGraph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            maxFlow += pathValue 
  
           
            v = sink 
            while(v != source): 
                u = parent[v] 
                self.matrixAsGraph[u][v] -= pathValue 
                self.matrixAsGraph[v][u] += pathValue 
                v = parent[v] 
  
        visited=len(self.matrixAsGraph)*[False]
        
        self.depthFirstSearch(self.matrixAsGraph,s,visited)

        #to store left side of the edge
        left_image = []
        #to store right side of the edge
        right_image = []
        
        for i in range(self.noOfRows): 
            for j in range(self.noOfCols): 
                if self.matrixAsGraph[i][j] == 0 and self.org_matrixAsGraph[i][j] > 0 and visited[i]:
                    left_image .append(i)
                    right_image.append(j)
                    
        return left_image,right_image,visited


#Referred from https://www.geeksforgeeks.org/minimum-cut-in-a-directed-graph/