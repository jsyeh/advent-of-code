# AdventOfCode_Day04
# Day 4: Scratchcards
# https://adventofcode.com/2023/day/4

#""" # 下面是簡單的 Sample Input 1 測資，在 Part 1 會輸出 13，在 Part 2 會輸出 30
lines = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

ans = 0
for line in lines:
    a = line.split()
    s = set()
    state = 1 # 1: winning numbers, 2: your numbers 
    now = 1
    for i in range(2,len(a)):
        if state==1:
            if a[i]=='|': state=2
            else: s.add(a[i])
        if state==2:
            if a[i] in s: now*=2
    ans += now//2
print(ans) # Part 1 我的 Puzzle Input 對應答案 24175



