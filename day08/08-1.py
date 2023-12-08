# AdventOfCode2023_Day8
# Day 8: Haunted Wasteland
# https://adventofcode.com/2023/day/8

# 這題的測資比較多，Sample Input 1 和 2 可在 Part 1 和 Part 2 執行
# 但 Sample Input 3 只為 Part 2 設計，使用時要小心！

""" # 下面是簡單的 Sample Input 1 測資，在 Part 1 和 Part 2 會輸出 2
lines = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''.splitlines()
""" # 上面是簡單的 Sample Input 1

#""" # 下面是簡單的 Sample Input 2 測資，在 Part 1 和 Part 2 會輸出 6
lines = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''.splitlines()
#""" # 上面是簡單的 Sample Input 2

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import defaultdict

RL = lines[0]
lines = lines[2:]

L = defaultdict(str)
R = defaultdict(str)
for line in lines:
    a, b, c = line.replace('= (','').replace(',','').replace(')','').split()
    L[a] = b
    R[a] = c

steps = 0
now = 'AAA'
bOver = False
while bOver==False:
    for c in RL:
        steps += 1
        if c=='R':
            # print(c, now, '-', R[now])
            now = R[now]
        else: 
            # print(c, now, '-', L[now])
            now = L[now]
        if now=='ZZZ': # 找到終點
            ans = steps # 存下答案
            bOver = True # 離開兩層迴圈
            break
print(ans) # Part 1 我的 Puzzle Input 對應答案 22357



