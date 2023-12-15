# AdventOfCode2023_Day15
# Day 15: Lens Library
# https://adventofcode.com/2023/day/15

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 1320，在 Part 2 會輸出 145
lines = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

all = lines[0].split(',')

def hash(line):
    ans = 0
    for c in line:
        #print(ord(c))
        ans += ord(c)
        #print(ans)
        ans = ans * 17 
        #print(ans)
        ans = ans % 256
    return ans
# Sample Input 1 用來測試 hash() 函式是否正確
# line = 'HASH'
# print(hash(line)) # output: 52

ans = 0
for a in all:
    now = hash(a)
    #print(now)
    ans += now
print(ans) # Part 2 我的 Puzzle Input 對應答案 517315



