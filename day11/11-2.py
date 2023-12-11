# AdventOfCode2023_Day11
# Day 11: Cosmic Expansion
# https://adventofcode.com/2023/day/11

# 在 LeetCode Playground 裡執行會超時 Time Limit Exceeded
# 所以應該會有更快的解法
""" # 下面是簡單的 Sample Input 1 測資，在 Part 1 會輸出 374，在 Part 2 會輸出 8410
lines = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''.splitlines()
""" 
import sys
lines = sys.stdin.read().splitlines()
from collections import deque

'''
ans = 0
N, M = len(lines), len(lines[0])
for i in range(N-1,-1,-1): 
    line = lines[i]
    if line.find('#')==-1: # 全部都是井號
        lines.insert(i, str(line))
N = len(lines)

c = [[lines[i][j] for j in range(M)] for i in range(N)]
#for i in range(N):
#    print(''.join(c[i]))
for j in range(M-1,-1,-1):
    haveIt = False
    for i in range(N):
        if c[i][j]=='#': # 有找到
            haveIt = True
    if not haveIt:
        for i in range(N):
            c[i].insert(j, '.')
M = len(c[0])

#print("===")

#for i in range(N):
#    print(''.join(c[i]))

# 接下來進行 DFS 找答案
def testAndAdd(i,j,d):
    if i<0 or j<0 or i>=N or j>=M: return
    if visited[i][j]: return
    visited[i][j] = True
    queue.append((i,j,d))

for i in range(N):
    for j in range(M):
        if c[i][j]=='#': # 開始進行BFS
            queue = deque()
            queue.append((i,j,0))
            visited = [[False]*M for _ in range(N)]
            visited[i][j] = True
            while len(queue)>0:
                ii,jj,dd = queue.popleft()
                if c[ii][jj]=='#':
                    ans += dd
                testAndAdd(ii+1,jj,dd+1)
                testAndAdd(ii-1,jj,dd+1)
                testAndAdd(ii,jj+1,dd+1)
                testAndAdd(ii,jj-1,dd+1) 
print(ans//2) # Part 1 我的 Puzzle Input 對應答案 10228230 or 527144(可能是錯的)
'''

print("====Part 2====")
# 現在是要在每個空白行，要插入 1000,000 行，所以不能真的插入，要標示在list，以便快速解決
# 往左右時，要查是否「跨越1百萬的直線」。往上下時，要查是否「跨越1百萬的直線」
# 接下來進行 DFS 找答案
N, M = len(lines), len(lines[0]) # 重設
c = [[lines[i][j] for j in range(M)] for i in range(N)]

# 接下來 check一下 list
sI, sJ = set(), set()
for i,line in enumerate(lines):
    if line.find('#')==-1: sI.add(i)
for j in range(M):
    haveIt = False
    for i in range(N):
        if lines[i][j]=='#': haveIt = True
    if not haveIt: sJ.add(j)

#print(sI)
#print(sJ)

def testAndSlideIAdd(i,j,di,d):
    while True:
        i += di
        if i<0 or j<0 or i>=N or j>=M: return
        if visited[i][j]: return # 一直往di,dj方向滑
        
        if i not in sI: break # 可以跳離 while 迴圈
        else: d += 1000000 # 可離開的話，代表找到了
    visited[i][j] = True
    queue.append((i,j,d))
def testAndSlideJAdd(i,j,dj,d):
    while True:
        j += dj
        if i<0 or j<0 or i>=N or j>=M: return 
        if visited[i][j]: return
        
        if j not in sJ: break
        else: d += 1000000
    visited[i][j] = True
    queue.append((i,j,d))
            
ans = 0
for i in range(N):
    for j in range(M):
        if c[i][j]=='#': # 開始進行BFS
            queue = deque()
            queue.append((i,j,0))
            visited = [[False]*M for _ in range(N)]
            visited[i][j] = True
            while len(queue)>0:
                ii,jj,dd = queue.popleft()
                if c[ii][jj]=='#':
                    ans += dd
                testAndSlideIAdd(ii,jj,+1,dd+1)
                testAndSlideIAdd(ii,jj,-1,dd+1)
                testAndSlideJAdd(ii,jj,+1,dd+1)
                testAndSlideJAdd(ii,jj,-1,dd+1)
print(ans//2) # Part 2 我的 Puzzle Input 對應答案 447073334102 or 81463996

