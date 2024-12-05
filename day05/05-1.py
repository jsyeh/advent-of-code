# AdventOfCode2024_Day05
# Day 5: Print Queue
# https://adventofcode.com/2024/day/5

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 143
lines = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''.splitlines()
#""" # 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 6242

# Input 「前面」先給 a|b 的前後關係
# 「後面」 list 對應的「頁數」是不是排好順序？找正確的那些 list 的中間的數，再加起來
from collections import defaultdict
state = 1  # 用來分開「前面」與「後面」的資料
ans = 0
path = defaultdict(list)  # 記錄「前面」的 a|b 前後關係
for line in lines:
    if line=='': 
        state=2
    elif state==1:
        a, b = line.split('|')
        a, b = int(a), int(b)
        path[a].append(b)
    elif state==2:
        pages = list(map(int, line.split(',')))  # 後面的數字，對應故事裡的「頁數」
        bad = 0
        for i1,p1 in enumerate(pages):
            for p2 in path[p1]:
                if p2 in pages: # p1...p2 都在裡面
                    i2 = pages.index(p2)
                    if i1>=i2: 
                        bad = 1
        if bad==0: ans += pages[len(pages)//2]

'''
# 下面是 topo sort 的版本，但本題不能用這個版本，所以註解掉
counter = Counter()
inDegree = Counter()
outDegree = Counter()
allNode = set()
# topo sort 要先找到 leading one
def possible(a, b):
    visited = set()

order = []
def toposort():
    queue = deque()
    for c in allNode:
        if inDegree[c]==0: 
            queue.append(c) #print(c, 'inDegree() is zero')
    print(queue) # 完蛋了，好像有巡環，沒有人是0
    while queue:
        now = queue.popleft()
        order.append(now)
        for nextNode in path[now]:
            inDegree[nextNode] -= 1
            print('now',now,'nextNode',nextNode, 'inDegree[]', inDegree[nextNode])
            if inDegree[nextNode]==0:
                queue.append(nextNode)
                
for line in lines:
    if line=='': 
        state=2
        print(inDegree)
        toposort()
        print(order)
    elif state==1:
        a, b = line.split('|')
        a, b = int(a), int(b)
        path[a].append(b)
        inDegree[b]+=1
        #outDegree[a]+=1
        allNode.add(a)
        allNode.add(b)
    elif state==2:
        a = list(map(int, line.split(',')))
        bad = 0
        for i in range(len(a)-1):
            if a[i] not in order or a[i+1] not in order:
                continue
            i1 = order.index(a[i])
            i2 = order.index(a[i+1])
            if i1>i2: bad = 1
            #a[i] vs. a[i+1]
        if bad==0: ans += a[len(a)//2]
'''

print(ans) # Part 1 我的 Puzzle Input 對應答案 6242
