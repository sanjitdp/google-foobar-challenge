from collections import deque

# finds the shortest path from start to anywhere in map using BFS
# (including distance to walls)


def shortest_paths(start, map):
    m = len(map)
    n = len(map[0])

    # initialize queue of positions to look at
    queue = deque([start])

    # initialize matrix of distances to each position
    distances = [[None for j in range(n)] for i in range(m)]
    distances[start[0]][start[1]] = 1

    # bfs iteration to compute distances to all reachable vertices
    while queue:
        # pick new vertex from queue
        vertex = queue.popleft()

        vertex_x = vertex[0]
        vertex_y = vertex[1]

        distance_to_vertex = distances[vertex_x][vertex_y]

        adjacent_vertices = [(vertex_x - 1, vertex_y),
                             (vertex_x + 1, vertex_y),
                             (vertex_x, vertex_y - 1),
                             (vertex_x, vertex_y + 1)]

        for adj in adjacent_vertices:
            adj_x = adj[0]
            adj_y = adj[1]

            # if looking at an unseen position in-bounds then add
            # to distances matrix and queue appropriately
            if 0 <= adj_x < m and 0 <= adj_y < n and not distances[adj_x][adj_y]:
                distances[adj_x][adj_y] = distance_to_vertex + 1
                if map[adj_x][adj_y] == 0:
                    queue.append(adj)

    return distances


def solution(map):
    m = len(map)
    n = len(map[0])

    # compute distances to points from start and end
    distances_from_start = shortest_paths((0, 0), map)
    distances_from_end = shortest_paths((m-1, n-1), map)

    # find minimum total distance to reachable position
    min_distance = float("inf")
    for i in range(m):
        for j in range(n):
            if distances_from_start[i][j] and distances_from_end[i][j]:
                min_distance = min(
                    min_distance, distances_from_start[i][j] + distances_from_end[i][j] - 1)

    return int(min_distance)
