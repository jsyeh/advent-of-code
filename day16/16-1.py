# AdventOfCode2023_Day16
# Day 16
# https://adventofcode.com/2023/day/16

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 46，在 Part 2 會輸出 51
lines = '''.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
'''.splitlines()
#""" # 上面是 Sample Input

#for line in lines: print(line) # 檢查發現 \ 的問題，要補成 \\

# 下面四行不要註解，便能使用我的 Puzzle Input
import sys
lines = []
for line in sys.stdin: # 因為資料裡有「反斜線\」所以不能用splitlines()
    lines.append(line.replace('\n','')) # 只好逐行apppend()
sys.setrecursionlimit(10000) # 因為太多層，要開大一點

# 模擬題，看光走過哪些地方，再用 recursion 一分為二，visited[i][j][d]重覆就避開
# | 分成上下兩邊 - 繼續往前
M, N = len(lines), len(lines[0])
#print(M,N)
dI = [0,1,0,-1]
dJ = [1,0,-1,0]
def visiting(i, j, d): # d:0右 1下 2左 3上
    if i<0 or j<0 or i>=M or j>=N: return
    
    if visited[i][j][d]: return
    visited[i][j][d] = True
    
    if lines[i][j]=='.':
        visiting(i+dI[d], j+dJ[d], d)
    if lines[i][j]=='|':
        if d==1 or d==3:
            visiting(i+dI[d], j+dJ[d], d)
        else:
            visiting(i+dI[1], j+dJ[1], 1)
            visiting(i+dI[3], j+dJ[3], 3)
    if lines[i][j]=='-':
        if d==0 or d==2:
            visiting(i+dI[d], j+dJ[d], d)
        else:
            visiting(i+dI[0], j+dJ[0], 0)
            visiting(i+dI[2], j+dJ[2], 2)
    if lines[i][j]=='/':
        if d==0: visiting(i-1,j,3)
        if d==1: visiting(i,j-1,2)
        if d==2: visiting(i+1,j,1)
        if d==3: visiting(i,j+1,0)
    if lines[i][j]=='\\':
        if d==0: visiting(i+1,j,1)
        if d==1: visiting(i,j+1,0)
        if d==2: visiting(i-1,j,3)
        if d==3: visiting(i,j-1,2)

def countAns():    
    ans = 0
    for i in range(M):
        for j in range(N):
            if visited[i][j][0] or visited[i][j][1] or visited[i][j][2] or visited[i][j][3]:
                ans += 1
    return ans

visited = [[[False]*4 for j in range(N)] for i in range(M)]
visiting(0,0,0)
print(countAns()) # Part 1 我的 Puzzle Input 對應答案 7034



