from collections import deque

def valid(st):
    return -1 <= st.index(0) <= 6

def next_states(st):
    res = []
    e = st.index(0)
    for m in [-1, -2, 1, 2]:
        n = e + m
        if 0 <= n <= 6:
            ns = list(st)
            ns[e], ns[n] = ns[n], ns[e]
            res.append(tuple(ns))
    return res

def dfs(start, goal):
    stk = [(start, [])]
    seen = set()
    cnt = 0
    while stk:
        st, path = stk.pop()
        if st in seen:
            continue
        seen.add(st)
        cnt += 1
        path = path + [st]
        if st == goal:
            print(f"Total nodes visited (DFS): {cnt}")
            return path
        for nxt in next_states(st):
            stk.append((nxt, path))
    print(f"Total nodes visited (DFS): {cnt}")
    return None

start = (-1, -1, -1, 0, 1, 1, 1)
goal = (1, 1, 1, 0, -1, -1, -1)

ans = dfs(start, goal)

if ans:
    print("Traversal path to goal:")
    for s in ans:
        print(s)
else:
    print("Goal not reachable.")
