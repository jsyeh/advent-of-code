# AdventOfCode2024_Day06
# Day XX
# https://adventofcode.com/2024/day/6

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 42，在 Part 2 會輸出 6
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
# Puzzle Input 在 Part1 會輸出 5404，在 Part 2 會輸出 1984

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

print("====Part 2====")

lines = [[lines[i][j] for j in range(N)] for i in range(M)]

def drawGrid(grid):  # debug 用，可畫出現在 grid 的內容
    for i in range(M):
        for j in range(N):
            if grid[i][j]==[]: print(lines[i][j], end='')  # 沒走過：原狀
            else: print(len(lines[i][j]), end='')  # 走過幾次
        print()  # 跳行
        
def testPos():
    grid = [ [[] for j in range(N)] for i in range(M)]
    d = 3  # 警衛一開始「向上」
    guardI, guardJ = startI, startJ  # 將警衛「放回」原本「出發點」
    grid[guardI][guardJ].append(d)
    #drawGrid(grid)  # debug 用
    while True:
        ii, jj = guardI + dI[d], guardJ + dJ[d]
        if ii<0 or jj<0 or ii>=M or jj>=N: break
        if lines[ii][jj]=='#':  # 遇到障礙物
            d = (d+1) % 4  # 就右轉90度
            continue  # 並換「下一輪模擬」
        if d in grid[ii][jj]:  # 以「相同姿勢」走過的話
            #drawGrid(grid)  # debug 用
            return 1  # 就循環了
        grid[ii][jj].append(d)  # 記錄「走過」的方向/姿勢
        guardI, guardJ = ii, jj  # 移到下一格
    return 0
ans = 0
for i in range(M):  # 因程式太暴力了，在 LeetCode Playground 執行會「超時」
    for j in range(N):  # 就把程式 copy 到其他地方執行，「等久一點」就可以了
        if lines[i][j] != '.': continue
        lines[i][j] = '#'  # 用石頭卡住 i,j 位置
        ans += testPos()  # 測試會不會有迴圈
        lines[i][j] = '.'  # 再把石頭移走

print(ans) # Part 2 我的 Puzzle Input 對應答案 1984

