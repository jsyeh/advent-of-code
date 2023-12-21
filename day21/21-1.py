# AdventOfCode2023_Day21
# Day 21: Step Counter
# https://adventofcode.com/2023/day/21

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 16，在 Part 2 會輸出 XX
lines = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''.splitlines()
#""" # 上面是 Sample Input

stepAns=6 # 要小心，Sample Input 用的 stepAns 是 6 不是 64
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
stepAns=64 # 題目要求的 Input 對應的 stepAns 是 64

from collections import *

# 題目看起來像是 BFS 的題目
M, N = len(lines), len(lines[0])
for i,line in enumerate(lines):
    S = line.find('S')
    if S!=-1:
        startI, startJ = i, S
        break
# 走6步,可以到16個格子
# 題目如果是比較大的地圖, 走 64步後, 可以站在多少個格子上
queue = deque()
queue.append((0, startI, startJ)) # 一開始第0步, 站在出發點
setAns = set()

def testAndPush(step, i, j):
    if i<0 or j<0 or i>=M or j>=N: return
    if lines[i][j]=='#': return
    
    posStr = str(i)+' '+str(j)
    if posStr in setAns: return # 這次這個位子走過, 就不要再走
    
    setAns.add(posStr)
    queue.append((step, i, j))
    if step==stepAns: setAns.add(posStr)
        
stepPrev=0
while len(queue)>0:
    step, i, j = queue.popleft()
    if step==stepAns: break # 完成答案的統計了, 離開
        
    if step>stepPrev:
        stepPrev = step
        setAns = set()
    testAndPush(step+1, i-1, j)
    testAndPush(step+1, i+1, j)
    testAndPush(step+1, i, j-1)
    testAndPush(step+1, i, j+1)

#print(setAns)
ans = len(setAns)

print(ans) # Part 1 我的 Puzzle Input 對應答案 3830



