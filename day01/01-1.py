# AdventOfCode2024_Day01
# Day 1: Historian Hysteria
# https://adventofcode.com/2024/day/1

# 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 11
lines = '''3   4
4   3
2   5
1   3
3   9
3   3
'''.splitlines()
# 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 276967

a0, b0 = [], []
for line in lines:
    a, b = list(map(int, line.split() ))
    a0.append(a)
    b0.append(b)

a1 = sorted(a0)  # 小到大排好
b1 = sorted(b0)  # 小到大排好
#print(a1)  # 確認有排好
#print(b1)  # 確認有排好
ans = 0  # 將 Part 1 的答案加好
for a,b in zip(a1,b1):  # 逐一取出
    ans += abs(a-b)  # 距離
print(ans)
