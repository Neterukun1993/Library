# verification-helper: PROBLEM https://yukicoder.me/problems/no/263
import sys
input = sys.stdin.readline

from String.PalindromicTree import PalindromicTree


def main():
    s = input()[:-1]
    t = input()[:-1]

    pt_s = PalindromicTree()
    for char in s:
        pt_s.add(char)

    pt_t = PalindromicTree()
    for char in t:
        pt_t.add(char)

    freq_s = pt_s.frequency_build()
    freq_t = pt_t.frequency_build()

    ans = 0
    stack = [(0, 0), (1, 1)]
    while stack:
        idx_s, idx_t = stack.pop()
        if idx_s > 1:
            ans += freq_s[idx_s] * freq_t[idx_t]
        for char in pt_s.nodes[idx_s].link:
            if char in pt_t.nodes[idx_t].link:
                nxt_s = pt_s.nodes[idx_s].link[char]
                nxt_t = pt_t.nodes[idx_t].link[char]
                stack.append((nxt_s, nxt_t))
    print(ans)


if __name__ == '__main__':
    main()
