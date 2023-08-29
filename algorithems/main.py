import node_check


# Example graph represented as an adjacency list
example_graph = {
    'A': {}, # is a special hole
    'B': {'A', 'D', 'E'},
    'C': {'A'},
    'D': {'B', 'A'},
    'E': {'B', 'A'},
    'F': {'A', 'B', 'C', 'D', 'E'} # is a root
}


# check is_hole
## node_to_check = input("Enter a node to check if it's a root: ")
## print(node_check.is_hole(example_graph, node_to_check))

# check is_special_hole 
## node_to_check = input("Enter a node to check if it's a root: ")
## print(node_check.special_hole(example_graph, node_to_check))

# Example colored graph
colored_graph = {
    'node1': {'color': 'red', 'neighbors': ['node2', 'node3']},
    'node2': {'color': 'blue', 'neighbors': ['node1', 'node3']},
    'node3': {'color': 'red', 'neighbors': ['node2']}
}

colors = {node: colored_graph[node]['color'] for node in colored_graph}

# Test if there is no monochromatic path starting from 'node1'
result = node_check.has_monochromatic_path(colored_graph, colors)
print("No monochromatic path:",result)
