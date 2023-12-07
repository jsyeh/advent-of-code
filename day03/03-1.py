# AdventOfCode_Day03
# Day 3: Gear Ratios
# https://adventofcode.com/2023/day/3
# """

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 4361，在 Part 2 會輸出 467835
lines = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

N, M = len(lines), len(lines[0].replace('\n',''))
possible = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not lines[i][j].isdigit() and lines[i][j] != '.':
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if ii>=0 and ii<N and jj>=0 and jj<M:
                        possible[ii][jj] = True
visited = [[False]*M for _ in range(N)]
table = [[' ']*M for _ in range(N)] # 裡面將會放數字
def visiting(i,j):
    if i<0 or j<0 or i>=N or j>=M: return
    if visited[i][j]: return
    visited[i][j] = True
    if lines[i][j].isdigit():
        table[i][j] = lines[i][j]
        visiting(i,j-1)
        visiting(i,j+1)

for i in range(N):
    for j in range(M):
        if possible[i][j]:
            visiting(i,j)
# print(table)
ans = 0
for i in range(N):
    a = "".join(table[i]).split()
    for now in a:
        if now.isdigit(): ans += int(now)
print(ans) # Part 1 我的 Puzzle Input 對應答案 527144



