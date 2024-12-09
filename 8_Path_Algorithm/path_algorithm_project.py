# Define a graph using an adjacency list representation
# Each node is a key, and its value is a list of tuples (neighbor, weight)
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    """
    Calculate the shortest paths from the start node to all other nodes using a simplified Dijkstra's algorithm.
    
    Parameters:
        graph (dict): The adjacency list of the graph where each node maps to its neighbors and weights.
        start (str): The starting node for the pathfinding algorithm.
        target (str, optional): Specific target node to display results for. If empty, show all paths.
    
    Returns:
        tuple: A dictionary of distances and a dictionary of paths from the start node to every other node.
    """

    # Initialize the set of unvisited nodes
    unvisited = list(graph)
    
    # Initialize distances for all nodes: 0 for the start node, infinity for others
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Initialize paths for all nodes as empty lists; start node's path contains only itself
    paths = {node: [] for node in graph}
    paths[start].append(start)

    # Continue until all nodes have been visited
    while unvisited:
        # Select the unvisited node with the smallest known distance (greedy approach)
        current = min(unvisited, key=distances.get)

        # Explore all neighbors of the current node
        for neighbor, weight in graph[current]:
            # Calculate the potential new distance to the neighbor
            new_distance = weight + distances[current]
            if new_distance < distances[neighbor]:  # Update if the new distance is shorter
                distances[neighbor] = new_distance
                
                # Update the path to the neighbor
                if paths[neighbor] and paths[neighbor][-1] == neighbor:
                    # If the neighbor already has a valid path, reset it to the new one
                    paths[neighbor] = paths[current][:]
                else:
                    # Extend the current node's path to include the neighbor
                    paths[neighbor].extend(paths[current])
                paths[neighbor].append(neighbor)

        # Mark the current node as visited by removing it from the unvisited set
        unvisited.remove(current)

    # Determine which nodes to display results for (all nodes if target is not specified)
    targets_to_print = [target] if target else graph

    for node in targets_to_print:
        if node == start:  # Skip displaying the distance from the start node to itself
            continue
        
        # Display the distance and path to the node
        print(f'\n{start}-{node} distance: {distances[node]}')
        print(f'Path: {" -> ".join(paths[node])}')

    return distances, paths

# Example usage: Find the shortest path from node 'A' to 'F' in the graph
shortest_path(my_graph, 'A', 'F')
