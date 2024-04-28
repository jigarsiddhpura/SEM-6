from collections import deque


def ford_fulkerson(G, source, sink):
    """
    A function to implement the Ford-Fulkerson algorithm to find the maximum flow in a graph.

    Parameters:
    - G: the graph represented as an adjacency list
    - source: the source node in the graph
    - sink: the sink node in the graph

    Returns:
    - max_flw: the maximum flow value in the graph
    - allpath: a list of all paths taken during the flow calculation
    - path_flws: a list of flow values for each path taken
    """
    max_flw = 0
    allpath, path_flws = [], []
    while True:
        paths = bfs(G, source, sink)
        if not paths:
            break
        for path in paths:
            path_flw = min(G[path[i]][path[i + 1]]
                           for i in range(len(path) - 1))
            allpath.append(path)
            path_flws.append(path_flw)
            max_flw += path_flw
            G = modify_G(G, path, path_flw)
    return max_flw, allpath, path_flws


def bfs(G, source, sink):
    """
    Perform a breadth-first search on a graph to find paths from a source node to a sink node.
    
    Parameters:
    - G: the graph represented as an adjacency matrix
    - source: the starting node for the search
    - sink: the destination node for the search
    
    Returns:
    - paths: a list of paths from the source to the sink node
    """
    paths = []
    queue = deque([(source, [source])])
    while queue:
        u, path = queue.popleft()
        for v, capacity in enumerate(G[u]):
            if capacity > 0 and v not in path:
                if v == sink:
                    paths.append(path + [v])
                else:
                    queue.append((v, path + [v]))
    return paths


def modify_G(G, path, flw):
    """
    Modify the graph G by updating the flow along the given path.
    
    Parameters:
    G (dict): The graph represented as a dictionary.
    path (list): The list of nodes representing the path in the graph.
    flw (int): The amount of flow to be modified along the path.
    
    Returns:
    dict: The modified graph G after updating the flow.
    """
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        G[u][v] -= flw
        G[v][u] += flw
    print("\nResidual Graph:")
    print(G)
    return G


#        D   M   K   B  P  s
G = [[0, 8, 14, 0, 0, 0], [0, 0, 14, 12, 0, 0], [0, 6, 0, 0, 10, 0], [0, 0, 10, 0, 0, 17], [0, 0, 0, 7, 0, 6], [0, 0, 0, 0, 0, 0]]

source = 0
sink = 5
max_flw, allpath, path_flws = ford_fulkerson(G, source, sink)
print(f"\nMaximum flow: {max_flw}")
print("\n ============ All augmenting paths and their corresponding flows ===========")
for i, path in enumerate(allpath):
    print(f"Path {i + 1} is {path} & flow along path is {path_flws[i]}\n")

