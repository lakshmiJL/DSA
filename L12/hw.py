class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def createEdge(self, x, y):
        self.adj[x - 1].append(y - 1)
        self.adj[y - 1].append(x - 1)

    def BFS(self, source):
        visited = [False] * self.n
        distances = [-1] * self.n  # Initialize distances to -1 (not visited)
        res = []

        queue = []
        queue.append(source)
        visited[source] = True
        distances[source] = 0  # Distance from source to itself is 0

        while queue:
            s = queue.pop(0)
            res.append(s)

            for node in self.adj[s]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
                    distances[node] = distances[s] + 1  # Increment distance

        return distances  # Return the list of distances

# Create a graph with 4 nodes
graph = Graph(4)

# Add edges to the graph
graph.createEdge(1, 2)
graph.createEdge(1, 3)
graph.createEdge(2, 4)

# Perform BFS starting from node 0 and calculate distances
distances_from_node_0 = graph.BFS(0)
print(distances_from_node_0)
