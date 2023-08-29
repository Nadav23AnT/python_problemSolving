import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimate of cost from current node to goal node

    def f(self):
        return self.g + self.h

def astar(start, goal, heuristic, get_neighbors):
    open_set = []   # Priority queue for open nodes
    closed_set = set()  # Set to track explored nodes

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_set, (start_node.f(), start_node))

    while open_set:
        _, current_node = heapq.heappop(open_set)  # O(log n), where n is the number of nodes in the open set

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Reverse path to start-to-goal order

        closed_set.add(current_node.state)

        for neighbor_state in get_neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue

            g = current_node.g + 1  # Assuming unit edge weights
            h = heuristic(neighbor_state, goal)
            neighbor_node = Node(neighbor_state, current_node, g, h)

            # Check if the neighbor is already in the open set with a lower cost
            found_better = False
            for _, existing_node in open_set:
                if existing_node.state == neighbor_state and existing_node.g > g:
                    found_better = True
                    break

            if not found_better:
                heapq.heappush(open_set, (neighbor_node.f(), neighbor_node))  # O(log n), where n is the number of nodes in the open set

    return None  # No path found

# Example usage
def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])  # Manhattan distance

def get_neighbors(state):
    x, y = state
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 10 and 0 <= ny < 10]  # 4 neighbors in a 10x10 grid

start = (0, 0)
goal = (9, 9)
path = astar(start, goal, heuristic, get_neighbors)
print(path)
