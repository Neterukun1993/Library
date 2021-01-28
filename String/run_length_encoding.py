def encoding(s):
    n = len(s)
    begin, cnt = 0, 0
    ans = []
    if n == 0:
        return ans
    for end in range(n + 1):
        if end == n or s[begin] != s[end]:
            ans.append((s[begin], cnt))
            begin, cnt = end, 1
        else:
            cnt += 1
    return ans
