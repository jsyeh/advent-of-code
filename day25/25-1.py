# AdventOfCode2023_Day25
# Day XX
# https://adventofcode.com/2023/day/25

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 XX，在 Part 2 會輸出 XX
lines = '''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import *

# 2023-12-25 20:03 開始寫
# @蔡濬帆 找到解法了 任選兩點把最短路徑刪掉 重複3次
# 做完如果graph被分成2個connected component則要找的3個edge分別在被刪掉的3條路徑上
edges = defaultdict(list)
nodes = set()
for line in lines:
    src, dsts = line.split(': ')
    dsts = dsts.split()
    for dst in dsts:
        edges[src].append(dst)
        edges[dst].append(src)
        nodes.add(src)
        nodes.add(dst)
#print(len(nodes))
#print(len(edges))
nodesList = list(nodes)
nodeN = len(nodesList)

def BFS():
    return 0

from copy import copy
import random

while True: # 亂數挑2個數
    a = random.randint(0,nodeN-1)
    b = random.randint(0,nodeN-1)
    if b==a: b = (b+1)%nodeN
    a, b = nodesList[a], nodesList[b]
    print('random', a, b)
    
    edges2 = copy(edges)
    for k in range(3): # 做3次，挑3次 shortest path
        queue = deque()
        queue.append((a, [a])) # 現在是誰，path如何
        visited = defaultdict(bool)
        visited[a] = True
        while len(queue)>0:
            now, path = queue.popleft()
            if now == b: # 找到終點了，可以離開迴圈了
                #print(path)
                for i in range(len(path)-1): # remove path
                    a2, b2 = path[i], path[i+1]
                    edges2[a2].remove(b2)
                    edges2[b2].remove(a2)
                break # 離開 while 迴圈
            # 下面照著 edges 去逐一連線
            for n2 in edges[now]: # now 的下一家
                if visited[n2]: continue # 跳開
                visited[n2] = True
                path2 = path.copy()
                path2.append(n2)
                queue.append((n2, path2))
    # 接下來算 connected component
    queue = deque() # 新的 BFS 找 connected component
    queue.append(a)
    setA = set()
    setA.add(a)
    while len(queue)>0:
        a2 = queue.popleft()
        for b2 in edges[a2]:
            if b2 in setA: continue # 避開
            setA.add(b2)
            queue.append(b2)
    sizeA = len(setA)
    sizeB = nodeN - sizeA
    print('nodeN', nodeN, 'sizeA', sizeA, 'sizeB', sizeB)
    if sizeA==0 or sizeB==0: 
        continue
    break
    
ans = sizeA*sizeB
print(ans) # Part 1 我的 Puzzle Input 對應答案 562912


