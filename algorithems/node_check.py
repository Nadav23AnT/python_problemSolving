def dfs(graph, node, visited):
    """
    Depth-First Search traversal of a graph starting from the given node.

    Args:
        graph (dict): The graph represented as an adjacency dictionary.
        node: The current node being visited.
        visited (set): A set to keep track of visited nodes.
    """
    visited.add(node)  # O(1)
    for neighbor in graph[node]:  # O(V), where V is the number of neighbors
        if neighbor not in visited:  # O(1)
            dfs(graph, neighbor, visited)  # Recursive call


def has_route_to_all_nodes(graph, start):
    """
    Check if there's a route from the starting node to all nodes in the graph.

    Args:
        graph (dict): The graph represented as an adjacency dictionary.
        start: The starting node for the traversal.

    Returns:
        bool: True if there's a route to all nodes, False otherwise.
    """
    visited = set()  # O(1)
    dfs(graph, start, visited)  # Calls dfs
    return visited == set(graph)  # O(V), where V is the number of nodes


def transpose_graph(graph):
    """
    Create the transpose of the given graph.
    The transpose graph has edges reversed compared to the original graph.

    Args:
        graph (dict): The graph represented as an adjacency dictionary.

    Returns:
        dict: The transpose graph represented as an adjacency dictionary.
    """
    transpose = {vertex: [] for vertex in graph}  # O(V), where V is the number of nodes
    for vertex in graph:  # O(V)
        for neighbor in graph[vertex]:  # O(E), where E is the number of edges
            transpose.setdefault(neighbor, []).append(vertex)  # O(1)
    return transpose


def is_hole(graph, node):
    """
    Check if the given node is part of a 'hole' in the graph.
    A hole is a subgraph where every node can be reached from every other node.

    Args:
        graph (dict): The graph represented as an adjacency dictionary.
        node: The node being tested.

    Returns:
        bool: True if the node is part of a hole, False otherwise.
    """
    return has_route_to_all_nodes(
        transpose_graph(graph), node
    )  # Calls has_route_to_all_nodes and transpose_graph


def special_hole(graph, node):
    """
    Check if the given node is part of a special hole in the graph.
    A special hole is a hole where the given node is not directly connected to any other node.

    Args:
        graph (dict): The graph represented as an adjacency dictionary.
        node: The node being tested.

    Returns:
        bool: True if the node is part of a special hole, False otherwise.
    """
    is_a_hole = is_hole(graph, node)  # Calls is_hole
    if not is_a_hole:  # O(1)
        return False
    for vertex in graph:  # O(V)
        if graph[vertex] == node:  # O(1)
            return False
    return True

def has_monochromatic_path(graph, colors):
    """
    Check if there's no monochromatic path between nodes in the graph.
    
    Args:
        graph (dict): The graph represented as an adjacency dictionary.
        colors (dict): A dictionary mapping nodes to their colors.
        
    Returns:
        bool: True if there are no monochromatic paths between nodes, False otherwise.
    """
    for node in graph:
        visited = set()
        if dfs_monochromatic(graph, node, colors, visited):
            return False  # Monochromatic path found
    return True

def dfs_monochromatic(graph, node, colors, visited):
    """
    Depth-First Search traversal to check for monochromatic paths.
    
    Args:
        graph (dict): The graph represented as an adjacency dictionary.
        node: The current node being visited.
        colors (dict): A dictionary mapping nodes to their colors.
        visited (set): A set to keep track of visited nodes.
        
    Returns:
        bool: True if a monochromatic path is found, False otherwise.
    """
    visited.add(node)
    current_color = colors[node]

    for neighbor in graph[node]['neighbors']:
        if neighbor not in visited:
            if colors[neighbor] == current_color:
                return True  # Monochromatic path found
            if dfs_monochromatic(graph, neighbor, colors, visited):
                return True

    return False


