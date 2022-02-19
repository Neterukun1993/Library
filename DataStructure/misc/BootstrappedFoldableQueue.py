class ListStack:
    def __init__(self, head=None, tail=None):
        self._head = head
        self._tail = tail

    def __bool__(self):
        return self._tail is not None

    def __iter__(self):
        ptr = self
        while ptr:
            yield ptr.head()
            ptr = ptr.tail()

    def cons(self, value):
        return ListStack(value, self)

    def head(self):
        if not self:
            raise IndexError("head from empty list")
        return self._head

    def tail(self):
        if not self:
            raise IndexError("tail from empty list")
        return self._tail

    def reverse(self):
        ret = ListStack()
        for x in self:
            ret = ret.cons(x)
        return ret

    def concat(self, other):
        ret = other
        for x in self.reverse():
            ret = ret.cons(x)
        return ret


class Suspension:
    def __init__(self, func):
        self.func = func

    def force(self):
        if callable(self.func):
            self.func = self.func()
        return self.func


class PhysicistsQueue:
    def __init__(self, w=None, fsize=0, f=None, rsize=0, r=None):
        self.working = ListStack() if w is None else w
        self.fsize = fsize
        self.f = Suspension(lambda: ListStack()) if f is None else f
        self.rsize = rsize
        self.r = ListStack() if r is None else r

    def __bool__(self):
        return self.fsize != 0

    def _checkw(self):
        if not self.working:
            return PhysicistsQueue(self.f.force(), self.fsize, self.f,
                                   self.rsize, self.r)
        else:
            return self

    def _check(self):
        if self.rsize <= self.fsize:
            return self._checkw()
        f = self.f.force()
        susp = Suspension(lambda: f.concat(self.r.reverse()))
        return PhysicistsQueue(f, self.fsize + self.rsize, susp,
                               0, ListStack())._checkw()

    def snoc(self, value):
        return PhysicistsQueue(self.working, self.fsize, self.f,
                               self.rsize + 1, self.r.cons(value))._check()

    def head(self):
        if not self.working:
            raise IndexError("head from empty queue")
        return self.working.head()

    def tail(self):
        if not self.working:
            raise IndexError("tail from empty queue")
        susp = Suspension(lambda: self.f.force().tail())
        return PhysicistsQueue(self.working.tail(), self.fsize - 1, susp,
                               self.rsize, self.r)._check()


class BootstrappedFoldableQueue:
    def __init__(self, op,
                 fmsize=0, f=None, m=None, m_agg=None, rsize=0, r=None):
        self.op = op
        self.fmsize = fmsize
        self.f = ListStack() if f is None else f
        self.m = PhysicistsQueue() if m is None else m
        self.m_agg = self if m_agg is None else m_agg
        self.rsize = rsize
        self.r = ListStack() if r is None else r

    def __len__(self):
        return self.fmsize + self.rsize

    def _check_q(self):
        def reverse(list_stack):
            agg = list_stack.head()[0]
            ret = ListStack().cons((agg, agg))
            for value, _ in list_stack.tail():
                agg = self.op(value, agg)
                ret = ret.cons((value, agg))
            return ret

        if self.fmsize >= self.rsize:
            return self._check_f()
        else:
            susp = Suspension(lambda: reverse(self.r))
            return BootstrappedFoldableQueue(self.op, self.fmsize + self.rsize,
                                             self.f, self.m.snoc(susp),
                                             self.m_agg.snoc(self.r.head()[1]),
                                             0, ListStack())._check_f()

    def _check_f(self):
        if not self.m and not self.f:
            return BootstrappedFoldableQueue(self.op)
        if not self.f:
            return BootstrappedFoldableQueue(self.op, self.fmsize,
                                             self.m.head().force(),
                                             self.m.tail(), self.m_agg.tail(),
                                             self.rsize, self.r)
        return self

    def all_fold(self):
        if not self:
            raise IndexError("fold from empty queue")
        agg = self.f.head()[1]
        agg = self.op(agg, self.m_agg.all_fold()) if self.m_agg else agg
        agg = self.op(agg, self.r.head()[1]) if self.r else agg
        return agg

    def snoc(self, value):
        if not self:
            return BootstrappedFoldableQueue(self.op, 1,
                                             ListStack().cons((value, value)),
                                             PhysicistsQueue(), self, 0,
                                             ListStack())
        else:
            agg = self.op(self.r.head()[1], value) if self.r else value
            elem = (value, agg)
            return BootstrappedFoldableQueue(self.op, self.fmsize, self.f,
                                             self.m, self.m_agg,
                                             self.rsize + 1,
                                             self.r.cons(elem))._check_q()

    def head(self):
        if not self:
            raise IndexError("head from empty queue")
        return self.f.head()[0]

    def tail(self):
        if not self:
            raise IndexError("tail from empty queue")
        return BootstrappedFoldableQueue(self.op, self.fmsize - 1,
                                         self.f.tail(), self.m, self.m_agg,
                                         self.rsize, self.r)._check_q()
