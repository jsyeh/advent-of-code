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


print("====Part 2====")
# 第二部分，要把*附近的數字乘起來
# visited2 = [[False]*M for _ in range(N)]
def visiting2(i,j):
    if i<0 or j<0 or i>=N or j>=M: return None
    # if visited2[i][j]: return None
    # visited2[i][j] = True
    if not lines[i][j].isdigit(): return None
    ans = visiting2(i,j-1) # 一直往左走，走到數字字串開頭的位置
    if ans==None: return (i,j)
    else: return ans
    
ans = 0
for i in range(N):
    for j in range(M):
        if lines[i][j] == '*':
            s = set()
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    now = visiting2(ii,jj)
                    if now!=None: s.add(now)
            # print(s)
            if len(s)==2:
                now2 = 1
                for ii,jj in s:
                    now = int(lines[ii][jj:].replace('*','.').split('.')[0].replace('*',''))
                    now2 *= now
                ans += now2
print(ans) # Part 2 我的 Puzzle Input 對應答案 81463996


