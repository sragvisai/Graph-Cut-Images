from collections import defaultdict 
  
class FordK:
    def __init__(self) -> None:
        self.countVisited = 1

    #a dfs method which calculates and updates the flow on the considered matrix
    def helperDFS(self,imageAsMatrix, visited, node, sink, flow):
        if (node == sink): 
            return flow

        valueAtNode = imageAsMatrix[node]
        visited[node] = self.countVisited

        for i in range(len(valueAtNode)):
            if visited[i] != self.countVisited and valueAtNode[i] > 0:

                if (valueAtNode[i] < flow):
                    flow = valueAtNode[i]
                value = self.helperDFS(imageAsMatrix, visited, i, sink, flow)

                if (value > 0):
                    imageAsMatrix[node][i] -= value
                    imageAsMatrix[i][node] += value
                    return value

        return 0

    # this function is used to get the mincut path for a given adjancency matrix
    # takes the following args:
    # imageAsMatrix : adjanceny matrix for the overlap region
    # source : source of the graph
    # sink : target of the grpah    
    def getMinCut(self, imageAsMatrix, source, sink):
        noOfRows = len(imageAsMatrix)
        noOfCols = len(imageAsMatrix[0])
        #we store the originalMatrix, which helps us in detemining the edges which faced a cut
        self.originalMatrix = imageAsMatrix
        visited = [0] * noOfRows
        minCut = [False] * noOfRows
        maxFlowValue = 0

        while(True):
            
            # we call in a DFS method starting from the source till the sink
            flow = self.helperDFS(imageAsMatrix, visited, source, sink, float('inf'))
            self.countVisited += 1
            
            maxFlowValue += flow
            if flow < 1e-4:
                for i in range(0,noOfRows):
                    if (visited[i] == self.countVisited-1):
                         minCut[i] = True

                #contains the left side of the edges
                left_image = []
                #contains the right side of the edges
                right_image = []
        
                for i in range(noOfRows): 
                    for j in range(noOfCols): 
                        if imageAsMatrix[i][j] < 2 and self.originalMatrix[i][j] > 0 and minCut[i]:
                            left_image .append(i)
                            right_image.append(j)
                return left_image,right_image,minCut

       
            
            
#Referred from https://www.geeksforgeeks.org/minimum-cut-in-a-directed-graph/