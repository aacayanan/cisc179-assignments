import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import defaultdict
matplotlib.use('TkAgg')  # or 'QtAgg', 'Agg', 'MacOSX', 'WebAgg', etc., depending on your system

# create a graph
G = nx.Graph()

# create a random amount of nodes
num_nodes = random.randint(3, 8)
nodes = []
for i in range(num_nodes):
    nodes.append(i)

# add a node
G.add_nodes_from(nodes)

# add edges to ensure the graph is connected
edge_paths = []
G.add_edges_from(edge_paths)
for i in range(num_nodes - 1):
    node1 = list(G.nodes)[i]
    node2 = list(G.nodes)[i + 1]
    G.add_edge(node1, node2)
    edge_paths.append((node1, node2))

# add random edges
for i in range(1, num_nodes):
    # choose two random nodes
    node1 = random.choice(list(G.nodes))
    node2 = random.choice(list(G.nodes))
    # add an edge between the two nodes
    G.add_edge(node1, node2)
    edge_paths.append((node1, node2))
edge_paths = list(set(tuple(sorted(edge)) for edge in edge_paths))  # remove duplicates

# check each node's degree and classify them
even_nodes = []
odd_nodes = []
for node in G.nodes:
    if G.degree(node) % 2 == 0:
        even_nodes.append(node)
    else:
        odd_nodes.append(node)
print("Even degree nodes:", len(even_nodes))
print("Odd degree nodes:", len(odd_nodes))

# check if the graph has an Euler circuit or path
if 0 < len(odd_nodes) <= 2:
    print(f"There are {len(odd_nodes)} odd degree nodes, so the graph has an Euler path.")
elif len(odd_nodes) == 0:
    print("There are no odd degree nodes, so the graph has an Euler circuit.")
else:
    print(f"There are {len(odd_nodes)} odd degree nodes, so the graph has no Euler path or circuit.")

edge_list = []  # to preserve directionality
used = set()    # to track used edges
edge_map = defaultdict(list)    # to map nodes to edges
# iterate through edges and create a mapping
for i, (u, v) in enumerate(edge_paths):
    edge = tuple(sorted((u, v)))
    edge_list.append((u, v))  # preserve directionality
    edge_map[u].append((v, i))
    edge_map[v].append((u, i))  # undirected


def dfs(node, path, visited_edges):
    # base case to check if all edges are visited, return the path
    if len(visited_edges) == len(edge_paths):
        return path

    # visit each neighbor of the current node
    for neighbor, edge_id in edge_map[node]:
        # check if the edge is already visited
        if edge_id not in visited_edges:
            visited_edges.add(edge_id)  # mark the edge as visited
            path.append((node, neighbor))   # add the edge to the path
            result = dfs(neighbor, path, visited_edges) # recursive call
            if result:
                return result
            # backtrack if no path is found and remove the edge from visited to explore other paths
            visited_edges.remove(edge_id)
            path.pop()
    return []


# find the Euler path using DFS
for i in range(num_nodes):
    start_node = i  # start from each node
    result_path = dfs(start_node, [], set())
    # check if a path is found
    if result_path:
        break

# draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# initial state with interactive mode
plt.ion()
plt.show()

# animate drawing each edge
for edge in result_path:
    plt.pause(1)  # pause for a second
    nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='red', width=2)

# show the final graph
plt.ioff()
plt.show()
