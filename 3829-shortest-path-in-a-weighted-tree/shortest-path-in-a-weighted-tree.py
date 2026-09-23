class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, index, value):
        index += 1

        while index <= self.n:
            self.bit[index] += value
            index += index & -index

    def query(self, index):
        index += 1

        total = 0

        while index > 0:
            total += self.bit[index]
            index -= index & -index

        return total


class Solution(object):
    def treeQueries(self, n, edges, queries):

        graph = [[] for _ in range(n + 1)]
        edge_weight = {}

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

            key = (min(u, v), max(u, v))
            edge_weight[key] = w

        parent = [0] * (n + 1)
        base_dist = [0] * (n + 1)

        tin = [0] * (n + 1)
        tout = [0] * (n + 1)

        # Use a list so we don't need nonlocal
        timer = [0]

        child_of_edge = {}

        def dfs(node, par):

            tin[node] = timer[0]
            timer[0] += 1

            for nei, weight in graph[node]:

                if nei == par:
                    continue

                parent[nei] = node

                base_dist[nei] = base_dist[node] + weight

                key = (min(node, nei), max(node, nei))
                child_of_edge[key] = nei

                dfs(nei, node)

            tout[node] = timer[0] - 1

        dfs(1, 0)

        bit = Fenwick(n)

        answer = []

        for query in queries:

            if query[0] == 1:

                _, u, v, new_weight = query

                key = (min(u, v), max(u, v))

                old_weight = edge_weight[key]

                delta = new_weight - old_weight

                edge_weight[key] = new_weight

                child = child_of_edge[key]

                # Add delta to entire subtree
                bit.add(tin[child], delta)
                bit.add(tout[child] + 1, -delta)

            else:

                _, x = query

                update = bit.query(tin[x])

                current_dist = base_dist[x] + update

                answer.append(current_dist)

        return answer