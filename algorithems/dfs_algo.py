def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')  # You can modify this to do something with the node
            stack.extend(graph[node] - visited)



