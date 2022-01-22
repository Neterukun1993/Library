# from heapq import heappushpop, heappush
from standard_library.heapq import heappushpop, heappush


class DynamicMedian:
    def __init__(self):
        self.l_q = []
        self.r_q = []
        self.l_sum = 0
        self.r_sum = 0

    def add(self, val):
        if len(self.l_q) == len(self.r_q):
            self.l_sum += val
            val = -heappushpop(self.l_q, -val)
            self.l_sum -= val
            heappush(self.r_q, val)
            self.r_sum += val
        else:
            self.r_sum += val
            val = heappushpop(self.r_q, val)
            self.r_sum -= val
            heappush(self.l_q, -val)
            self.l_sum += val

    def median_low(self):
        if len(self.l_q) + 1 == len(self.r_q):
            return self.r_q[0]
        else:
            return -self.l_q[0]

    def median_high(self):
        return self.r_q[0]

    def minimum_query(self):
        """min(|x - a_1| + |x - a_2| + ⋯ + |x - a_N|) s.t. any x"""
        res1 = (len(self.l_q) * self.median_high() - self.l_sum)
        res2 = (self.r_sum - len(self.r_q) * self.median_high())
        return res1 + res2
