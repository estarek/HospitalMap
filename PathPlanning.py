import collections
from Graph import Graph


class PathPlanning:
    def __init__(self, map):
        self.map = map
        self.path_dfs = []
        self.path_bfs = []

    def getPath(self, start_node, end_node):
        pass

    def dfs(self, graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        self.path_dfs.append(start)
        #print(start)
        for next in graph[start] - visited:
            self.dfs(graph, next, visited)
        return self.path_dfs

    def bfs(self, graph, startnode):
        # Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        self.path_bfs.append(startnode)
        while queue:
            vertex = queue.popleft()
            #self.marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
                    self.path_bfs.append(node)
        return self.path_bfs

    def marked(self, n):
        print(n)







if __name__ == '__main__':
    pass
