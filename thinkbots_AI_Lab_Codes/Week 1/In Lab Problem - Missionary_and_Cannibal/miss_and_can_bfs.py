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
        if b == 1:
            ns = (m - dm, c - dc, 0)
        else:
            ns = (m + dm, c + dc, 1)
        if valid(ns):
            res.append(ns)
    return res

def bfs(start, goal):
    q = deque([(start, [])])
    seen = set()
    count = 0
    while q:
        st, path = q.popleft()
        if st in seen:
            continue
        seen.add(st)
        count += 1
        path = path + [st]
        if st == goal:
            print(f"Total nodes visited: {count}")
            return path
        for nxt in next_states(st):
            q.append((nxt, path))
    print(f"Total nodes visited (BFS): {count}")
    return None

start = (3, 3, 1)
goal = (0, 0, 0)

ans = bfs(start, goal)

if ans:
    print("Traversal path to goal:")
    for s in ans:
        print(s)
else:
    print("Goal not reachable.")
