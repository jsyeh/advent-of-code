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


print("====Part 2====")
# Part 2 有點奇怪，要模擬ghost走路的方式，把所有 xxA 一起走到 xxZ 的步數找出來
# 使用暴力迴圈太慢，所以「每個鬼」的 steps 找出來，並更新「最小公倍數」即可
def gcd(a, b): # 最大公因數
    if a==0: return b
    if b==0: return a
    return gcd(b, a%b)

def lcm(a, b): # 最小公倍數
    return a*b//gcd(a,b)

# 以下第71行、第85行註解後，便可在 Part 2 使用 Sample Input 3
""" # 下面是 Sample Input 3 測資，「只為 Part 2 設計」，在 Part 2 會輸出 6
lines = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''.splitlines()
RL = lines[0]
lines = lines[2:]
""" # 上面是 Sample Input 3 的測資及檔案讀取

ghostStart = [] # 供 Part 2 使用
L = defaultdict(str)
R = defaultdict(str)
for line in lines:
    a, b, c = line.replace('= (','').replace(',','').replace(')','').split()
    # print(a,b,c)
    if a[2]=='A': # 是鬼要開始的點
        ghostStart.append(a) # 供 Part 2 使用
        # print(a)
    L[a] = b
    R[a] = c

ans2 = 1 # 「最小公倍數」的基礎答案1，不能是0哦！
# print(ghostStart) # 每個鬼的出發點 'xxA'
for k in range(len(ghostStart)):
    now = ghostStart[k]
    bOver=False
    steps = 0
    while bOver==False:
        for c in RL:
            steps += 1
            if c == 'R':
                now = R[now]
            else:
                now = L[now]
            if now[2]=='Z': # 找到第k筆的終點
                bOver = True # 可以離開 while 迴圈
                break
    # print(ghostStart[k], now, steps)
    ans2 = lcm(ans2, steps) # 持續更近「最小公倍數」

print(ans2) # Part 2 我的 Puzzle Input 對應答案 10371555451871


