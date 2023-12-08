# AdventOfCode2023_Day07
# Day 7: Camel Cards
# https://adventofcode.com/2023/day/7

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 6440，在 Part 2 會輸出 5905
lines = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import defaultdict

# 可惡，A>K>Q>J>T>數字 所以也要改一下 （不能照字串 ASCII來排）
#      Z Y X W V 9 8 7 ...
def convert(h):
    d = defaultdict(int)
    h = h.replace('A','Z')
    h = h.replace('K','Y')
    h = h.replace('Q','X')
    h = h.replace('J','W')
    h = h.replace('T','V')
    # print(h)
    for c in h:
        d[c] += 1
    pair, triple = 0, 0
    for k in d:
        if d[k]==5: return '7'+h # Five
        if d[k]==4: return '6'+h # Four
        if d[k]==3: triple += 1
        if d[k]==2: pair += 1
    if triple==1 and pair==1: return '5'+h # Full house
    if triple==1: return '4'+h # Three
    if pair==2: return '3'+h # Two pair
    if pair==1: return '2'+h # One pair
    return '1'+h

all = []
for line in lines:
    h, c = line.split()
    all.append( [convert(h),int(c)] )
# 接下來比大小，想到可以把 hands[i] 
all.sort()
# print(all)
ans = 0
N = len(all)
for i in range(N):
    # print(i+1, all[i][0][1:], all[i][1])
    ans += (i+1)*all[i][1]
print(ans) # Part 1 我的 Puzzle Input 對應答案 253933213


print("====Part 2====")
# 新的 J 規則
def convert2(h):
    d = defaultdict(int)
    h = h.replace('A','Z')
    h = h.replace('K','Y')
    h = h.replace('Q','X')
    h = h.replace('J','1') # J要變最弱
    h = h.replace('T','V')
    # print(h)
    for c in h:
        d[c] += 1
    pair, triple = 0, 0
    # d['J'] 萬用,現在叫 d['1']
    if '1' not in d:
        for k in d:
            if d[k]==5: return '7'+h # Five
            if d[k]==4: return '6'+h # Four
            if d[k]==3: triple += 1
            if d[k]==2: pair += 1
        if triple==1 and pair==1: return '5'+h # Full house
        if triple==1: return '4'+h # Three
        if pair==2: return '3'+h # Two pair
        if pair==1: return '2'+h # One pair
        return '1'+h
    # 以下是有 d['1'] 的狀況
    
    for k in d:
        if d[k]==5 or (k!='1' and d[k]+d['1']==5): return '7'+h # Five
    for k in d:
        if d[k]==4 or (k!='1' and d[k]+d['1']==4): return '6'+h # Four
        # 以上是 J 3張能做的事，必然晉級
        # J 2張的話，JJ123 JJ113(不可能)
        # J 1張的話，J1122 J1123 J1234
    for k in d:
        if k!='1' and d[k]==3: triple += 1
        if k!='1' and d[k]==2: pair += 1
    if d['1']==2: return '4'+h # 新規則
    if d['1']==1 and pair==2: return '5'+h # 新規則
    if triple==1 and pair==1: return '5'+h # Full house
    if d['1']==1 and pair==1: return '4'+h # 新規則
    if d['1']==1: return '2'+h # 新規則
    if triple==1: return '4'+h # Three
    if pair==2: return '3'+h # Two pair
    if pair==1: return '2'+h # One pair
    return '1'+h

all = []
for line in lines:
    h, c = line.split()
    all.append([convert2(h), int(c)])
all.sort()
ans = 0
N = len(all)
for i in range(N):
    ans += (i+1)*all[i][1]
print(ans) # Part 2 我的 Puzzle Input 對應答案 253473930


