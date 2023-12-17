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


''' # 寫失敗(第2次)，找不到 Bug 很煩，決定註解掉、重寫第3次
heap = []
val = [[inf]*N for _ in range(N)] # 只要 val[i][j]沒有更大，就繼續做
# 為了簡化，我想讓 heat 值在 heap 裡就對應正確
def visiting(prev_heat, i, j, d, dN):
    if i<0 or j<0 or i>=M or j>=N: return
    if dN>=3: return
    now_heat = prev_heat + int(lines[i][j])
    if now_heat>val[i][j]: return # 不能用
    
    now = (now_heat, i, j, d, dN)
    heappush(heap, now)

visiting(0, 0, 0, 0, -1)
while len(heap)>0:
    heat, i, j, d, dN = heappop(heap) # 只放合理的值
    if i==M-1 and j==N-1:
        ans = heat
        break
    if heat>val[i][j]: continue # 不能用
    val[i][j] = heat
        
    d1, d2 = (d+1)%4, (d+3)%4
    visiting(heat, i+dI[d], j+dJ[d], d, dN+1)
    visiting(heat, i+dI[d1], j+dJ[d1], d1, 0)
    visiting(heat, i+dI[d2], j+dJ[d2], d2, 0)
for i in range(M):
    print(val[i])

print(ans)
'''

''' # 寫失敗(第1次)，找不到 Bug 很煩，決定註解掉、重寫第2次
M, N = len(lines), len(lines[0])
#print(M,N)

dI = [0,1,0,-1]
dJ = [1,0,-1,0]

# 左上角，走到右下角
# heap 找最小, 同不能同方向走3格
visited = [[False]*N for _ in range(M)]
heap = [] # 裡面要放 (heat, i,j, dir, 累積次數) 在 i,j這格的heat,同時之前走幾步了
now = ( int(lines[0][0]), 0, 0, 0, -1 ) # 往右走0步
heappush(heap,  now )

def testAndPush(prev_heat, i, j, d, dN):
    if i<0 or j<0 or i>=M or j>=N: return
    if dN>=4: return
    #if visited[i][j]: return  #??  
    heappush(heap, (prev_heat+int(lines[i][j]), i, j, d, dN))

table = [[inf]*N for _ in range(M)]
count = 0
while len(heap)>0:
    heat, i, j, d, dN = heappop(heap)
    if count<20:
        print(heat,i,j,d,dN)
        count+=1

    if heat>table[i][j]: continue # 如果值沒有更大，就當做沒看到
    #if visited[i][j]: continue
    #visited[i][j] = True
    table[i][j] = heat # debug用
    
    if i== M-1 and j == N-1: # 走到終點
        ans = heat # heat 值
        break
    d1, d2 = (d+1)%4, (d+3)%4
    testAndPush(heat, i+dI[d], j+dJ[d], d, dN+1 )
    testAndPush(heat, i+dI[d1], j+dJ[d1], d1, 1 )
    testAndPush(heat, i+dI[d2], j+dJ[d2], d2, 1 )

for i in range(M):
    print(table[i])
print(ans) # Part 1 我的 Puzzle Input 對應答案 1110
'''


print("====Part 2====")
# 連續4次直線後，才能轉彎。最多連續10格直線同方向。

""" # 下面是簡單的 Sample Input 2 測資，在 Part 2 會輸出 71
lines = '''111111111111
999999999991
999999999991
999999999991
999999999991
'''.splitlines()
"""

M, N = len(lines), len(lines[0])

val = [[[[inf]*11 for _ in range(4)] for _ in range(N)] for _ in range(M)]
visited = [[[[False]*11 for _ in range(4)] for _ in range(N)] for _ in range(M)]

heap = []
def visiting2(prev_heat, i, j, d, dN):
    if i<0 or j<0 or i>=M or j>=N: return
    if dN>=10: return
    now_heat = prev_heat + int(lines[i][j])
    if visited[i][j][d][dN]: return
    
    if now_heat>val[i][j][d][dN]: return # 不能用

    now = (now_heat, i, j, d, dN)
    heappush(heap, now)

visiting(0,0,1,0,0) # 往右
visiting(0,1,0,1,0) # 往下

while len(heap)>0:
    heat, i, j, d, dN = heappop(heap) # 只放合理的值
    if i==M-1 and j==N-1 and dN>=3: # 要走夠走，才平衡
        ans = heat
        val[i][j][d][dN] = heat
        break
    if heat>val[i][j][d][dN]: continue # 不能用
    if visited[i][j][d][dN]: continue
    visited[i][j][d][dN] = True
    val[i][j][d][dN] = heat
        
    d1, d2 = (d+1)%4, (d+3)%4
    if dN<10: # 可以繼續直走 最多連續10格直線同方向。
        visiting2(heat, i+dI[d], j+dJ[d], d, dN+1)
    if dN>=3: # 可以轉向，連續4次直線後，才能轉彎。
        visiting2(heat, i+dI[d1], j+dJ[d1], d1, 0)
        visiting2(heat, i+dI[d2], j+dJ[d2], d2, 0)


''' # 印出4維的表格
for i in range(M): # Debug用，把資料印出來的迴圈
    for j in range(N):
        now = inf # 預設值
        for d in range(4): # 將裡面兩層合併
            for dN in range(10): # 將裡面兩層合併
                now = min(now, val[i][j][d][dN])
        print(now, end=',')
        # 將裡面兩層合併
    print()
'''

print(ans) # Part 2 我的 Puzzle Input 對應答案 1294


