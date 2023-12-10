# AdventOfCode2023_Day10
# Day 10: Pipe Maze
# https://adventofcode.com/2023/day/10

#""" # 下面是簡單的 Sample Input 1 測資，在 Part 1 會輸出 4，在 Part 2 會輸出 XXX
lines = '''.....
.S-7.
.|.|.
.L-J.
.....
'''.splitlines()
#""" # 上面是 Sample Input 1

""" # 下面是簡單的 Sample Input 2 測資，在 Part 1 會輸出 4，在 Part 2 會輸出 XXX
lines = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF
'''.splitlines()
""" # 上面是 Sample Input 2

""" # 下面是簡單的 Sample Input 3 測資，在 Part 1 會輸出 8，在 Part 2 會輸出 XXX
lines = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''.splitlines()
""" # 上面是 Sample Input 3

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import deque

# 使用 BFS 即可找到
M, N = len(lines), len(lines[0])
#print(M,N)
item = list(list(line) for line in lines) # 將字母變成 item[i][j]
#print(item)

# 要先找到起點 & 哪個鄰居「可以走過去」
def findStart():
    for i in range(M): # 先找出開始點 'S'
        for j in range(N):
            if lines[i][j]=='S':
                startI = i
                startJ = j
                return startI, startJ
startI, startJ = findStart()
# print('startI', startI, 'startJ', startJ) # 確認座標正確

d = {}
d['|'] = [-1,0,+1,0] # 往 上，下。
d['-'] = [0,-1,0,+1] # 往 左，右。
d['L'] = [-1,0,0,+1] # 往 上，右。
d['J'] = [-1,0,0,-1] # 往 上，左。
d['7'] = [0,-1,+1,0] # 往 左，下。
d['F'] = [0,+1,+1,0] # 往 右，下。

#d = {'|':[-1,0,+1,0], '-':[0,-1,0,+1], 'L':[-1,0,0,+1], 'J':[-1,0,0,-1], '7':[0,-1,+1,0], 'F':[0,+1,+1,0]}

visited = [[False]*N for _ in range(M)]
visited[startI][startJ] = True
queue = deque()

# test startI,startJ's neighbors
def testStartNeighbor(startI, startJ, di, dj):
    nI, nJ = startI + di, startJ + dj
    if nI<0 or nJ<0 or nI>=M or nJ>=N: return
    if item[nI][nJ] not in d: return
    p1, p2, p3, p4 = d[item[nI][nJ]]
    if p1+di==0 and p2+dj==0: queue.append((startI, startJ, di, dj, 0))
    if p3+di==0 and p4+dj==0: queue.append((startI, startJ, di, dj, 0))
testStartNeighbor(startI, startJ, +1, 0)
testStartNeighbor(startI, startJ, -1, 0)
testStartNeighbor(startI, startJ, 0, +1)
testStartNeighbor(startI, startJ, 0, -1)

# 下面的4個方向，只會有2個方向是合理的，因為要接起來（我比賽時，是用手動註解切換）
#queue.append((startI, startJ, -1,0, 0)) # 座標i,j，出去的方向dI,dJ, step
#queue.append((startI, startJ, +1,0, 0)) # 座標i,j，出去的方向dI,dJ, step
#queue.append((startI, startJ, 0,-1, 0)) # 座標i,j，出去的方向dI,dJ, step
#queue.append((startI, startJ, 0,+1, 0)) # 座標i,j，出去的方向dI,dJ, step

ans = 1 # steps
while len(queue)>0:
    i,j,di,dj, s = queue.popleft() # 新的目的地
    item[i][j] = str(s%10) 
    
    # print(i,j,di,dj,s)
    ans = max(ans, s)
    i2, j2 = i+di, j+dj
    if i2<0 or j2<0 or i2>=M or j2>=N: continue
    if visited[i2][j2]: continue
    visited[i2][j2] = True
    if lines[i2][j2]=='.' or lines[i2][j2]=='S': continue
        
    p1, p2, p3, p4 = d[lines[i2][j2]]
    if p1+di==0 and p2+dj==0: # 左右上下 順利相接
        queue.append( (i2,j2, p3, p4, s+1))
    if p3+di==0 and p4+dj==0:
        queue.append( (i2,j2, p1, p2, s+1))

# for line in item: # debug 用的迴圈，印出水管的字串
#     print(''.join(line), end='')
# print()
print(ans) # Part 1 我的 Puzzle Input 對應答案 7093



