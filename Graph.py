import collections
class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        return self.findedges()

    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = set()
            #self.gdict[vrtx].add(vrtx)

            # Add the new edge

    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            if vrtx2 not in self.gdict[vrtx1]:
                self.gdict[vrtx1].add(vrtx2)
        else:
            self.gdict[vrtx1] = set()
            self.gdict[vrtx1].add(vrtx2)
        if vrtx2 in self.gdict:
            if vrtx1 not in self.gdict[vrtx2]:
                self.gdict[vrtx2].add(vrtx1)
        else:
            self.gdict[vrtx2] = set()
            self.gdict[vrtx2].add(vrtx1)

    # List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def getPathes(self,start,end):
        paths = []
        if start!=end:

            pathes_count = len(self.gdict[start])
            i=0
            for p in range(0,pathes_count):
                p = []
                p.append(start)
                paths.append(p)
            i =0
            for e in self.gdict[start]:
                paths[i].append(e)
                paths[i] = self.continuePath(e,end,paths[i])
                i = i + 1

        return paths

    def continuePath(self,node,target,path):
        curr = node
        while curr != target :
            childs = self.gdict[curr]
            for c in childs:
                if c not in path:
                    path.append(c)
                    curr = c
        return path






# Create the dictionary with graph elements
'''
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = Graph(graph_elements)
g.AddEdge({'a', 'e'})
g.AddEdge({'a', 'c'})
print(g.edges())
'''
