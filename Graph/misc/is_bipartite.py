def is_bipartite(graph):
    n = len(graph)
    cols = [-1] * n
    cnts = []
    for v in range(n):
        if cols[v] != -1:
            continue
        cols[v] = 0
        cnt = [1, 0]
        stack = [v]
        while stack:
            v = stack.pop()
            for nxt_v in graph[v]:
                if cols[nxt_v] != -1:
                    if cols[nxt_v] == cols[v] ^ 1:
                        continue
                    else:
                        return False, cols, cnts
                cols[nxt_v] = cols[v] ^ 1
                cnt[cols[nxt_v]] += 1
                stack.append(nxt_v)
        cnts.append(cnt)
    return True, cols, cnts
