def merge(ps_l, ps_r):
    """merge the two lists sorted by y-coordinates into one."""
    szl, szr = len(ps_l), len(ps_r)
    ps = []
    il, ir = 0, 0
    for i in range(szl + szr):
        if ir == szr:
            ps.append(ps_l[il])
            il += 1
        elif il == szl:
            ps.append(ps_r[ir])
            ir += 1
        elif ps_l[il][1] < ps_r[ir][1]:
            ps.append(ps_l[il])
            il += 1
        else:
            ps.append(ps_r[ir])
            ir += 1
    return ps


def closest_pair_rec(points):
    """calculate closest pair's distance by divide-and-conquer."""
    INF = 1.0 * 10 ** 9
    size = len(points)
    if size <= 1:
        return INF, points
    mid = size // 2
    x_mid = points[mid][0]
    dist_l, ps_l = closest_pair_rec(points[0:mid])
    dist_r, ps_r = closest_pair_rec(points[mid:size])
    dist = min(dist_l, dist_r)
    ps = merge(ps_l, ps_r)
    qs = []
    for xp, yp in ps:
        if abs(xp - x_mid) >= dist:
            continue
        for xq, yq in reversed(qs):
            dx = xp - xq
            dy = yp - yq
            if dy >= dist:
                break
            dist = min((dx ** 2 + dy ** 2) ** 0.5, dist)
        qs.append((xp, yp))
    return dist, ps


def closest_pair(points):
    dist, _ = closest_pair_rec(sorted(points))
    return dist
