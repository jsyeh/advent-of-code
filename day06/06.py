# AdventOfCode2023_Day06
# Day 6: Wait For It
# https://adventofcode.com/2023/day/6

#""" # 下面是簡單的 Sample Input 1 測資，在 Part 1 會輸出 288，在 Part 2 會輸出 71503
line1, line2 = '''Time:      7  15   30
Distance:  9  40  200
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
line1, line2 = sys.stdin.read().splitlines()

t = list(map(int, line1.split()[1:] ))
d = list(map(int, line2.split()[1:] ))

ans = 1
for i in range(len(t)):
    now = 0
    for k in range(1,t[i]): # 按k,速度變成k
        if (t[i]-k)*k>d[i]: now += 1
    ans *= now

print(ans) # Part 1 我的 Puzzle Input 對應答案 170000


print("====Part 2====")
t = int( ''.join(line1.split()[1:]) ) # 數字太大，會超時
d = int( ''.join(line2.split()[1:]) )
# print(t,d)
now = 0
start, end = 0, 0
for k in range(1,t):
    if (t-k)*k>d: 
        start = k
        break
for k in range(t-1, 0, -1):
    if(t-k)*k>d:
        end = k
        break
# print(start, end)
print(end-start+1) # Part 2 我的 Puzzle Input 對應答案 20537782


