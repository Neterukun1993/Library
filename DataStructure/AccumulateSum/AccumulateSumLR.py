class AccumulateSumLR:
    def __init__(self, array, op, e):
        self.op = op
        self.e = e
        n = len(array)
        self.left = [self.e] * (n + 1)
        self.right = [self.e] * (n + 1)
        for i in range(n):
            self.left[i + 1] = self.op(self.left[i], array[i])
        for i in reversed(range(n)):
            self.right[i] = self.op(self.right[i + 1], array[i])

    def left_fold(self, upper):
        """fold of [0, upper)"""
        return self.left[upper]

    def right_fold(self, lower):
        """fold of [lower, n)"""
        return self.right[lower]

    def fold(self, ex_idx):
        """fold all of the elements except for array[ex_idx]"""
        return self.op(self.left[ex_idx], self.right[ex_idx + 1])
