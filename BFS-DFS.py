from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        output = []
        queue = Queue()
        visited = [False] * (max(self.graph) + 1)

        queue.put(s)
        visited[s] = True

        while not queue.empty():
            s = queue.get()
            output.append(s)
            for z in self.graph[s]:
                if not visited[z]:
                    visited[z] = True
                    queue.put(z)
        return output

    def DFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        output = []

        def dfs_util(node):
            visited[node] = True
            output.append(node)
            for z in self.graph[node]:
                if not visited[z]:
                    dfs_util(z)

        dfs_util(s)
        return output



g=Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)
print(f'BFS Traversal for the Graph is {g.BFS(2)}')
print(f'DFS Traversal for the Graph is {g.DFS(2)}')