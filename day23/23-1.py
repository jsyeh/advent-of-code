# AdventOfCode2023_Day23
# Day 23: A Long Walk
# https://adventofcode.com/2023/day/23

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 94，在 Part 2 會輸出 154
lines = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
from collections import defaultdict
import sys
lines = sys.stdin.read().splitlines()
sys.setrecursionlimit(10000) # 又超過了，再加大吧！

# 如果您踏上斜坡磁磚，下一步必須是下坡，切勿兩次踏上同一塊地磚
# 您可以進行最長的徒步旅行，因為有開始點，所以直接用DFS就可以做出來了
# 但函式長度不能太長的話，很麻煩
ans = 0
M, N = len(lines), len(lines[0])
# print(M,N) # 141x141 or 23x23 的矩陣，函式最多呼叫 19881 層，超過！
# 函式可能不夠用，或是可能性太高，所以要用 stack

visited = [[False]*N for _ in range(M)]

def testAndRun(i,j, step, dd): # 座標、步數、方向
    if i<0 or j<0 or i>=M or j>=N: return
    if lines[i][j]=='#': return # 卡住不能走
    if visited[i][j]: return
    # 處理上下坡的問題
    if lines[i][j]=='>' and dd!=0: return # 不可 
    if lines[i][j]=='v' and dd!=1: return # 不可 
    if lines[i][j]=='<' and dd!=2: return # 不可 
    if lines[i][j]=='^' and dd!=3: return # 不可 
    global ans
    if i==M-1 and j==N-2: ans = max(ans, step) # 走到目標才行
    #ans = max(ans, step)
    DFS(i,j,step)

def DFS(i,j,step):
    visited[i][j]=True
    testAndRun(i,j+1,step+1,0) # 右
    testAndRun(i+1,j,step+1,1) # 下
    testAndRun(i,j-1,step+1,2) # 左
    testAndRun(i-1,j,step+1,3) # 上
    visited[i][j]=False

DFS(0,1,0) # step=0 因為還沒開始走

print(ans) # Part 1 我的 Puzzle Input 對應答案 2050



