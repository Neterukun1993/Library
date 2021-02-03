def cartesian_tree(arr):
    n = len(arr)
    par = [-1] * n
    stack = []
    for i in range(n):
        prv_i = -1
        while stack and arr[i] < arr[stack[-1]]:
            prv_i = stack.pop()
        if prv_i != -1:
            par[prv_i] = i
        if stack:
            par[i] = stack[-1]
        stack.append(i)
    return par
