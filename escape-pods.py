# use the Ford-Fulkerson maximum flow algorithm to compute
# all possible augmenting paths from any source to any
# sink until there are none remaining
def solution(entrances, exits, path):
    n = len(path)

    flow = 0

    augmented_path_found = True
    while augmented_path_found:

        # check whether an augmenting path was found
        augmented_path_found = False

        # try starting at each of the entrances
        for entrance in entrances:
            visited = set()
            augmenting_path = []

            node = entrance
            while True:
                visited.add(node)

                # keep track of largest edge seen
                largest_edge = 0
                next_node = -1

                # compute greedy next node, if it exists
                for i in range(n):
                    if path[node][i] > largest_edge and i not in visited:
                        largest_edge = path[node][i]
                        next_node = i

                # if there is a greedily best node, go there
                if next_node >= 0:
                    augmenting_path.append(node)
                    node = next_node

                # backtracking for DFS
                elif augmenting_path:
                    node = augmenting_path.pop()

                # if we've exhausted all possible augmenting paths, try next entrance
                else:
                    break

                # if at end of path, update residual and maximum flow
                if node in exits:
                    augmenting_path.append(node)

                    # compute bottleneck edge (this is added flow due to the augmenting path)
                    bottleneck = float("inf")
                    for i in range(len(augmenting_path) - 1):
                        if path[augmenting_path[i]][augmenting_path[i+1]] < bottleneck:
                            bottleneck = path[augmenting_path[i]
                                              ][augmenting_path[i+1]]

                    # add bottleneck of augmenting path to flow
                    flow += bottleneck

                    # update residual graph based on augmenting path
                    for j in range(len(augmenting_path) - 1):
                        path[augmenting_path[j]
                             ][augmenting_path[j+1]] -= bottleneck
                        path[augmenting_path[j+1]
                             ][augmenting_path[j]] += bottleneck

                    # we've found an augmenting path, so break out of the loop
                    augmented_path_found = True
                    break

    # return total flow
    return int(flow)
