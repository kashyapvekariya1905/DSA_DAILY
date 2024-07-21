class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def build_graph(conditions):
            graph = defaultdict(list)
            for x, y in conditions:
                graph[x - 1].append(y - 1)
            return graph

        def find_cycle(graph):
            color = [0] * k

            def dfs(v):
                color[v] = 1
                for u in graph[v]:
                    if color[u] == 0:
                        if dfs(u):
                            return True
                    elif color[u] == 1:
                        return True
                color[v] = 2
                return False

            for v in range(k):
                if color[v] == 0 and dfs(v):
                    return True
            return False

        def topological_sort(graph):
            visited = [False] * k
            ans = []

            def dfs(v):
                visited[v] = True
                for u in graph[v]:
                    if not visited[u]:
                        dfs(u)
                ans.append(v)

            for i in range(k):
                if not visited[i]:
                    dfs(i)
            return ans[::-1]

        graph1 = build_graph(rowConditions)
        graph2 = build_graph(colConditions)

        if find_cycle(graph1) or find_cycle(graph2):
            return []

        ans1 = topological_sort(graph1)
        ans2 = topological_sort(graph2)

        ans = [[0] * k for _ in range(k)]
        m = {v: i for i, v in enumerate(ans2)}

        for i in range(k):
            ans[i][m[ans1[i]]] = ans1[i] + 1

        return ans
