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


print('====Part 2====')
# 要先把 = 和 - 切開
# After "ot=7":
# Box 0: [rn 1] [cm 2]
# Box 3: [ot 7] [ab 5] [pc 6]
# 1*1*1
# 1+2*2
# 4*1*7
# 4*2*5
# 4*3*6
# 加起來是 72
def printBox():
    for i,b in enumerate(box):
        if len(b)==0: continue # 避開不印
        print('Box', i, ':', end='')
        print(b)
    print()
    
box = [[] for i in range(256)]
for a in all:
    if a.find('-') != -1: # 有減號, 要刪
        tag = a[:-1]
        b = hash(tag) # 對應的 box
        #print('Box', hash(tag)+1, tag, '-')
        for i,t in enumerate(box[b]):
            if t[0] == tag: # 找到相同的 tag
                box[b].remove(t) # 刪掉它
                break
    else: # 有等號, 要加入
        tag = a[:-2]
        val = int(a[-1:])
        b = hash(tag) # 對應的 box
        #print('Box', hash(tag)+1, tag, val)
        found = False
        for i, t in enumerate(box[b]):
            if t[0] == tag: #有找到相同的 tag
                box[b][i] = (tag,val)
                found = True
                break
        if found==False: box[b].append((tag,val))
    #print('After', a)
    #printBox()

ans = 0
for i,b in enumerate(box):
    for slot,t in enumerate(b):
        now = (i+1)*(slot+1)*t[1]
        #print(now)
        ans += now
print(ans) # Part 2 我的 Puzzle Input 對應答案 247763


