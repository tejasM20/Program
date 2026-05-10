def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=' ')
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def bfs(graph, start):
    visited = set([start])
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Larger Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'F', 'H'],
    'F': ['C', 'E', 'I'],
    'G': ['D'],
    'H': ['E'],
    'I': ['F']
}

print("DFS Traversal:")
dfs(graph, 'A', set())

print("\nBFS Traversal:")
bfs(graph, 'A')
