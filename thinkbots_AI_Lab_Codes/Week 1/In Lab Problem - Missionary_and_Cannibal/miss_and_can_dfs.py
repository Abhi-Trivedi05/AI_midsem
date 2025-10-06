from collections import deque

def valid(st):
    m, c, b = st
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def next_states(st):
    res = []
    m, c, b = st
    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    for dm, dc in moves:
        ns = (m - dm, c - dc, 0) if b == 1 else (m + dm, c + dc, 1)
        if valid(ns):
            res.append(ns)
    return res

def dfs(start, goal):
    stack = [(start, [])]
    seen = set()
    cnt = 0
    while stack:
        st, path = stack.pop()
        if st in seen:
            continue
        seen.add(st)
        cnt += 1
        path = path + [st]
        if st == goal:
            print(f"Total nodes visited (DFS): {cnt}")
            return path
        for nxt in next_states(st):
            stack.append((nxt, path))
    print(f"Total nodes visited (DFS): {cnt}")
    return None

start = (3, 3, 1)
goal = (0, 0, 0)

ans = dfs(start, goal)

if ans:
    print("Traversal path to goal:")
    for s in ans:
        print(s)
else:
    print("Goal not reachable.")
