from collections import deque

def BFS(Adj,Node):
    queue = deque()
    visited = set()
    queue.append(Node)
    visited.add(Node)

    while queue:
        current = queue.popleft()
        print(current,end=" ")
        for n in Adj[current]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

def DFS(Adj,Node):
    stack=deque()
    visited=set()
    stack.append(Node)
    visited.add(Node)

    while stack:
        current = stack.pop()
        print(current,end=" ")
        for n in reversed(Adj[current]):
            if n not in visited:
                visited.add(n)
                stack.append(n)

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("BFS:",end=" ")
BFS(adj_list,'A')
print()
print("DFS:",end=" ")
DFS(adj_list,'A')
