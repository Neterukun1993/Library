class LinkedList:

    class LazyConcatLinkedList:
        def __init__(self, left, right):
            self.l = left
            self.r = right

        def evaluate(self):
            l = self.l.pop()
            return LinkedList.concat(l, self.r)

    class LazyReverseLinkedList:
        def __init__(self, ll):
            self.head = ll.head
            self.tail = ll.tail

        def evaluate(self):
            head, tail = self.head, self.tail
            ret = LinkedList.push(None, head)
            while tail is not None:
                head, tail = tail.head, tail.tail
                ret = LinkedList.push(ret, head)
            return ret

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def top(self):
        return self.head

    def pop(self):
        if self.tail is not None:
            self.tail = self.tail.evaluate()
        return self.tail

    def evaluate(self):
        return self

    @classmethod
    def push(cls, ll, head):
        return LinkedList(head, ll)

    @classmethod
    def reverse(cls, ll):
        return cls.LazyReverseLinkedList(ll)

    @classmethod
    def concat(cls, ll_left, ll_right):
        if ll_left is None:
            return ll_right.evaluate()
        return LinkedList(ll_left.head,
                          cls.LazyConcatLinkedList(ll_left, ll_right))


class BankersQueue:
    def __init__(self, f=None, r=None, fsize=0, rsize=0):
        self.f = f
        self.r = r
        self.fsize = fsize
        self.rsize = rsize

    def _normalize(self):
        if self.fsize >= self.rsize:
            return self
        else:
            lazy_rotate = LinkedList.concat(self.f, LinkedList.reverse(self.r))
            return BankersQueue(lazy_rotate,
                                None,
                                self.fsize + self.rsize,
                                0)

    def front(self):
        return self.f.top()

    def push(self, val):
        return BankersQueue(self.f,
                            LinkedList.push(self.r, val),
                            self.fsize,
                            self.rsize + 1)._normalize()

    def pop(self):
        return BankersQueue(self.f.pop(),
                            self.r,
                            self.fsize - 1,
                            self.rsize)._normalize()
