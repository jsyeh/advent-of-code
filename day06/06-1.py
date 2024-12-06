# AdventOfCode2024_Day06
# Day XX
# https://adventofcode.com/2024/day/6

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 42
lines = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''.splitlines()
#""" # 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 5404

M, N = len(lines), len(lines[0])
grid = [[0]*N for i in range(M)]  # 裡面會標注「有沒有走過」
# 先找到起點
for i in range(M):
    for j in range(N):
        if lines[i][j]=='^': # 找到警衛「一開始」的位置
            guardI, guardJ = i, j
            startI, startJ = i, j
grid[i][j] = 1  # 一開始的格子，要記得標「走過」，才不會漏算
dI = [0,1,0,-1]  # 4個方向：右、下、左、上
dJ = [1,0,-1,0]  # 對應index 0, 1, 2, 3
d = 3  # 一開始的方向，是向上
while True:
    ii, jj = guardI + dI[d], guardJ + dJ[d]  # 將前進的「下一格」
    if ii<0 or jj<0 or ii>=M or jj>=N: break
    if lines[ii][jj]=='#': # 遇到障礙物
        d = (d+1)%4  # 就右轉90度
        continue  # 再換下一筆
    grid[ii][jj] = 1  # 標「走過」
    guardI, guardJ = ii, jj  # 正式前進到「下一格」

ans = 0  # 最後統計「走過」幾格
for i in range(M):
    for j in range(N):
        if grid[i][j]==1:  # 走過的格子
            ans+=1
            #print('X', end='')  # 畫出結果、debug 用
        #else: print(lines[i][j], end='')  # 畫出結果、debug 用
    #print()  # 畫出結果、debug 用

print(ans) # Part 1 我的 Puzzle Input 對應答案 5404

