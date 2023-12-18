# AdventOfCode2023_Day18
# Day 18
# https://adventofcode.com/2023/day/18

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 62，在 Part 2 會輸出 952408144115
lines = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
sys.setrecursionlimit(30000) # 又超過範圍，只好設大一點

# 先了解M，N有多大
dI = {'R':0, 'D':1, 'L':0, 'U':-1}
dJ = {'R':1, 'D':0, 'L':-1, 'U':0}
maxI, maxJ, minI, minJ = 0, 0, 0, 0
I, J = 0, 0
for line in lines:
    a, b, c = line.split()
    I += dI[a]*int(b)
    J += dJ[a]*int(b)
    maxI = max(maxI, I)
    maxJ = max(maxJ, J)
    minI = min(minI, I)
    minJ = min(minJ, J)
#print(minI, minJ, maxI, maxJ)

M, N = maxI-minI+1, maxJ-minJ+1
#print(M,N)
I, J = -minI, -minJ # 出發點
#print(I, J)
# 要挖洞
hole = [['.']*N for _ in range(M)]

for line in lines:
    a, b, c = line.split()
    di, dj, d = dI[a], dJ[a], int(b)
    for k in range(d):
        hole[I][J] = '#'
        I += di
        J += dj
hole[I][J] = '#'

# 要把「邊界的'.'」加到 stack裡DFS
ans = M*N
def DFS(i, j):
    if i<0 or j<0 or i>=M or j>=N: return
    if hole[i][j] != '.': return
    hole[i][j] = 'o' # outside area
    global ans
    ans -= 1
    DFS(i+1,j)
    DFS(i-1,j)
    DFS(i,j+1)
    DFS(i,j-1)

for i in range(M):
    DFS(i,0)
    DFS(i,N-1)
for j in range(N):
    DFS(0,j)
    DFS(M-1,j)

'''
for i in range(M):
    for j in range(N):
        print(hole[i][j], end='')
    print()
'''

print(ans) # Part 1 我的 Puzzle Input 對應答案 106459



