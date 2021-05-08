# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.Heap.IntervalHeap import IntervalHeap
from misc.xorshift import xorshift32


def main():
    # 昇順push / 昇順pop
    ih = IntervalHeap()
    for i in range(100):
        ih.push(i)
        assert(ih.max == i)
        assert(ih.min == 0)
    for i in range(100):
        val = ih.min
        poped = ih.pop_min()
        assert(val == poped)

    # 昇順push / 降順pop
    ih = IntervalHeap()
    for i in range(100):
        ih.push(i)
        assert(ih.max == i)
        assert(ih.min == 0)
    for i in range(100):
        val = ih.max
        poped = ih.pop_max()
        assert(val == poped)

    # 降順push / 昇順pop
    ih = IntervalHeap()
    for i in reversed(range(100)):
        ih.push(i)
        assert(ih.max == 99)
        assert(ih.min == i)
    for i in range(100):
        val = ih.min
        poped = ih.pop_min()
        assert(val == poped)

    # 降順push / 降順pop
    ih = IntervalHeap()
    for i in reversed(range(100)):
        ih.push(i)
        assert(ih.max == 99)
        assert(ih.min == i)
    for i in range(100):
        val = ih.max
        poped = ih.pop_max()
        assert(val == poped)

    # ランダム
    ih = IntervalHeap()
    rand32 = xorshift32()
    array = []
    for i in range(100):
        val = rand32()
        ih.push(val)
        array.append(val)
        assert(ih.max == max(array))
        assert(ih.min == min(array))

    for i in range(1000):
        val = ih.min
        poped = ih.pop_min()
        assert(val == poped)
        assert(val == min(array))
        del array[array.index(val)]

        val = ih.max
        poped = ih.pop_max()
        assert(val == poped)
        assert(val == max(array))
        del array[array.index(val)]

        for _ in range(2):
            val = rand32()
            ih.push(val)
            array.append(val)


if __name__ == '__main__':
    main()
    print("Hello World")
