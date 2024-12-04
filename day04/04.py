# AdventOfCode2024_DayXX
# Day XX
# https://adventofcode.com/2024/day/XX

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 18，在 Part 2 會輸出 9
lines = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''.splitlines()
#""" # 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 2532，在 Part 2 會輸出 1941
M, N = len(lines), len(lines[0])
ans = 0
dI = [0,1,0,-1,1,-1,1,-1]
dJ = [1,0,-1,0,1,1,-1,-1]
xmas = "XMAS"
for i in range(M):
    for j in range(N):
        if lines[i][j]=='X': # 開頭是對的
            for d in range(8):
                match = 0
                for k in range(4):
                    ii, jj = i+dI[d]*k, j+dJ[d]*k
                    if 0<=ii<M and 0<=jj<N and lines[ii][jj]==xmas[k]: match+=1
                if match==4: ans+=1
print(ans) # Part 1 我的 Puzzle Input 對應答案 2532

print("====Part 2====")

ans = 0
for i in range(1,M-1):
    for j in range(1,N-1):
        if lines[i][j]=='A': # 中間是對的
            match = 0
            if lines[i-1][j-1]=='M' and lines[i+1][j+1]=='S': match+=1
            if lines[i-1][j-1]=='S' and lines[i+1][j+1]=='M': match+=1
            if lines[i-1][j+1]=='M' and lines[i+1][j-1]=='S': match+=1
            if lines[i-1][j+1]=='S' and lines[i+1][j-1]=='M': match+=1
            if match==2: ans+=1
print(ans) # Part 2 我的 Puzzle Input 對應答案 1941
