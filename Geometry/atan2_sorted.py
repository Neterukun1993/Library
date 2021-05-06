def atan2_sorted(points):
    class Cmp:
        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return self.cmp(self.obj, other.obj) < 0

        def cmp(self, p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 * y2 - y1 * x2 < 0: return 1
            elif x1 * y2 - y1 * x2 > 0: return -1
            else: return 0

    quadrant = [[] for i in range(4)]
    for x, y in points:
        if x == 0 and y == 0: quadrant[2].append((x, y))
        elif x <= 0 and y < 0: quadrant[0].append((x, y))
        elif x > 0 and y <= 0: quadrant[1].append((x, y))
        elif x >= 0 and y > 0: quadrant[2].append((x, y))
        else: quadrant[3].append((x, y))

    res = []
    for i in range(4):
        quadrant[i].sort(key=Cmp)
        for p in quadrant[i]:
            res.append(p)
    return res
