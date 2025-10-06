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

def bfs(start, goal):
    q = deque([(start, [])])
    seen = set()
    cnt = 0
    while q:
        st, path = q.popleft()
        if st in seen:
            continue
        seen.add(st)
        cnt += 1
        path = path + [st]
        if st == goal:
            print(f"Total nodes visited (BFS): {cnt}")
            return path
        for nxt in next_states(st):
            q.append((nxt, path))
    print(f"Total nodes visited (BFS): {cnt}")
    return None

start = (-1, -1, -1, 0, 1, 1, 1)
goal = (1, 1, 1, 0, -1, -1, -1)

ans = bfs(start, goal)

if ans:
    print("Traversal path to goal:")
    for s in ans:
        print(s)
else:
    print("Goal not reachable.")
