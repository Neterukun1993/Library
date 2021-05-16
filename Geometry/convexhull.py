def convexhull(points):
    def ccw(p0, p1, p2):
        v1 = p1[0] - p0[0], p1[1] - p0[1]
        v2 = p2[0] - p0[0], p2[1] - p0[1]
        crs = v1[0] * v2[1] - v1[1] * v2[0]
        if crs > 0: return 1  # 反時計回り
        if crs < 0: return -1  # 時計回り
        return 0  # 直線上

    ps = sorted(points)
    if len(ps) <= 2:
        return ps

    lower = [ps[0], ps[1]]
    upper = [ps[0], ps[1]]
    for p in ps[2:]:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) > 0:
            upper.pop()
        upper.append(p)
    return lower + upper[::-1][1:-1]
