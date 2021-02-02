class PersistentStack:
    def __init__(self, val=None, prev=None):
        self.val = val
        self.prev = prev

    def top(self):
        return self.val

    def push(self, x):
        return PersistentStack(x, self)

    def pop(self):
        return self.prev
