# AdventOfCode2023_Day17
# Day 17: Clumsy Crucible
# https://adventofcode.com/2023/day/17

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 102，在 Part 2 會輸出 94
lines = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from math import inf
from heapq import *

M, N = len(lines), len(lines[0])

dI = [0,1,0,-1]
dJ = [1,0,-1,0]
val = [[[[inf]*4 for _ in range(4)] for _ in range(N)] for _ in range(M)]
visited = [[[[False]*4 for _ in range(4)] for _ in range(N)] for _ in range(M)]
# 超級暴力的4維陣列，以便存全部的狀況

heap = [] # 進行 BFS 的 heap
def visiting(prev_heat, i, j, d, dN):
    if i<0 or j<0 or i>=M or j>=N: return
    if dN>=3: return # Part 1 限定「直線不能走超過3格」又我程式從0開始數，故>=3
    now_heat = prev_heat + int(lines[i][j]) # 加上本格後的 heat 值
    if visited[i][j][d][dN]: return # 走過，就不能再走
    
    if now_heat>val[i][j][d][dN]: return # 更差的值，就不要用

    now = (now_heat, i, j, d, dN)
    heappush(heap, now)

visiting(0, 0, 1, 0, 0) # 往右 參數是 heat, i, j, d, dN
visiting(0, 1, 0, 1, 0) # 往下 參數是 heat, i, j, d, dN

while len(heap)>0:
    heat, i, j, d, dN = heappop(heap) # 只放合理的值
    if i==M-1 and j==N-1:
        ans = heat
        val[i][j][d][dN] = heat
        break
    if heat>val[i][j][d][dN]: continue # 不能用
    if visited[i][j][d][dN]: continue
    visited[i][j][d][dN] = True
    val[i][j][d][dN] = heat
        
    d1, d2 = (d+1)%4, (d+3)%4
    visiting(heat, i+dI[d], j+dJ[d], d, dN+1)
    visiting(heat, i+dI[d1], j+dJ[d1], d1, 0)
    visiting(heat, i+dI[d2], j+dJ[d2], d2, 0)

''' # Debug用，把資料印出來的迴圈
for i in range(M):
    for j in range(N):
        now = inf
        for d in range(4):
            now = min(now, min(val[i][j][d]))
        print(now, end=',')
    print()
'''

print(ans) # Part 1 我的 Puzzle Input 對應答案 1110



