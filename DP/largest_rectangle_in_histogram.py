def largest_rectangle_in_histogram(heights):
    heights = heights + [-1]  # sentinel
    ans = 0
    stack = []
    for i, height in enumerate(heights):
        idx = i
        while True:
            if not stack or stack[-1][0] <= height:
                stack.append((height, idx))
                break
            else:
                h, l = stack.pop()
                ans = max(h * (i - l), ans)
                idx = l
    return ans
