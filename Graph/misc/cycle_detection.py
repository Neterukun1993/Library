def cycle_detection(graph):
    def _dfs(v):
        stack = [v, 0]
        visited[v] = 1
        while stack:
            v, idx = stack[-2:]
            if idx < len(graph[v]):
                nxt_v = graph[v][idx]
                stack[-1] += 1
                if visited[nxt_v] == 1:
                    # detect cycle
                    cycle.append(nxt_v)
                    while cycle[0] != v:
                        cycle.append(v)
                        stack.pop(), stack.pop()
                        v = stack[-2]
                    cycle.reverse()
                    return
                if visited[nxt_v] == 2:
                    continue
                visited[nxt_v] = 1
                stack.append(nxt_v)
                stack.append(0)
            else:
                visited[v] = 2
                stack.pop(), stack.pop()

    n = len(graph)
    visited = [0] * n
    cycle = []
    for v in range(n):
        if not cycle and visited[v] == 0:
            _dfs(v)
    return cycle
