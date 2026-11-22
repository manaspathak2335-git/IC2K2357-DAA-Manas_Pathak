from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def insert(self,Edges=[]):
        if len(Edges) == 0:
            return
        for u,v in Edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

    def print_adj(self):
        print("Adjacency List:",self.adj)

    def BFS(self,Node):
        queue = deque()
        visited = set()
        queue.append(Node)
        visited.add(Node)

        while queue:
            current=queue.popleft()
            print(current,end=" ")
            for n in self.adj[current]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

    def DFS(self,Node):
        stack = deque()
        visited = set()
        stack.append(Node)
        visited.add(Node)

        while stack:
            current = stack.pop()
            print(current,end=" ")
            for n in reversed(self.adj[current]):
                if n not in visited:
                    stack.append(n)
                    visited.add(n)

    def DFS_recursive(self,Node,visited=set()):
        visited.add(Node)
        print(Node,end=" ")
        for n in self.adj[Node]:
            if n not in visited:
                self.DFS_recursive(n,visited)
                    


G = Graph()
G.insert([('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('E','F')])
G.print_adj()
print("BFS:",end=" ")
G.BFS('A')
print()
print("DFS:",end=" ")
G.DFS('A')
print()
print("DFS recursive:",end=" ")
G.DFS_recursive('A')

