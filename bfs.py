from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)


def bfs_partition(adjacency_list, start_vertex, threshold):
    num_vertices = len(adjacency_list)
    visited = [False] * num_vertices
    partition = [0] * num_vertices
    queue = deque()

    queue.append((0, start_vertex))
    visited[start_vertex] = True

    while queue:
        curr_level, current_vertex = queue.popleft()
        partition[current_vertex] = curr_level

        for neighbor in adjacency_list[current_vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((curr_level + 1, neighbor))

