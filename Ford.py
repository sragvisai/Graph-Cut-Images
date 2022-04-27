from collections import defaultdict 
  
class FordK:
    def __init__(self) -> None:
        self.countVisited = 1
    

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
        
    def getMinCut(self, imageAsMatrix, source, sink):
        noOfRows = len(imageAsMatrix)
        visited = [0] * noOfRows
        minCut = [False] * noOfRows
        maxFlowValue = 0

        while(True):
            
            flow = self.helperDFS(imageAsMatrix, visited, source, sink, float('inf'))
            self.countVisited += 1
            
            maxFlowValue += flow
            if flow < 1e-4:
                for i in range(0,noOfRows):
                    if (visited[i] == self.countVisited-1):
                         minCut[i] = True
                return minCut
            
            
