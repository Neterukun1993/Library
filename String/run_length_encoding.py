def encoding(string):
    n = len(string)
    begin, cnt = 0, 0
    ans = []
    if n == 0:
        return ans
    for end in range(n + 1):
        if end == n or string[begin] != string[end]:
            ans.append((string[begin], cnt))
            begin, cnt = end, 1
        else:
            cnt += 1
    return ans
