def edge_to_vertex(n, edges):
    m = len(edges)
    new_edges = []
    vals = [0] * (n + m)
    for i, (u, v, val) in enumerate(edges):
        new_edges.append((u, n + i))
        new_edges.append((n + i, v))
        vals[n + i] = val
    return new_edges, vals
