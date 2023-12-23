# 2023-12-23 16:13 全部重寫 Part 2 目前有人解出的 二星2281 一星2306
# 2023-12-23 17:17 成功 rank 2737(程式跑36秒), 此時 二星2758 一星2600
# AdventOfCode2023_Day23_again
# Day 23: A Long Walk
# https://adventofcode.com/2023/day/23

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 94，在 Part 2 會輸出 154
lines = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import defaultdict

print('====Part 2====')
M, N = len(lines), len(lines[0])
startI, startJ = 0, 1
endI, endJ = M-1, N-2

nodeSet = set()
nodeDict = defaultdict(str)

def posStr(i, j): return str(i)+' '+str(j)

def findNodeSet(): # 找到全部的「重要節點」
    slopSign = {'>','v','<','^'}
    for i in range(1,M-1):
        for j in range(1,N-1):
            slopN = 0
            if lines[i-1][j] in slopSign: slopN += 1
            if lines[i+1][j] in slopSign: slopN += 1
            if lines[i][j-1] in slopSign: slopN += 1
            if lines[i][j+1] in slopSign: slopN += 1
            if slopN>=3: 
                nodeSet.add(posStr(i,j))
                nodeDict[len(nodeDict)] = posStr(i,j)
            # 順便檢查有沒有3叉路 or 4叉路
            if lines[i][j]=='.': #  接下來要檢查4個方向
                crossN = 0
                if lines[i-1][j]=='.': crossN += 1
                if lines[i+1][j]=='.': crossN += 1
                if lines[i][j-1]=='.': crossN += 1
                if lines[i][j+1]=='.': crossN += 1
                if crossN > 2: 
                    print("CROSS", i, j) # 放心，沒有其他cross

# 這裡把 slop 交叉路口的節點，都找出來
nodeSet.add(posStr(startI,startJ)) # 起點
nodeDict[len(nodeDict)] = posStr(startI,startJ)

findNodeSet() # 所有的中間點

nodeSet.add(posStr(endI,endJ)) # 終點
nodeDict[len(nodeDict)] = posStr(endI,endJ)

nodeN = len(nodeSet)
#print('len(nodeSet)', len(nodeSet)) # 9 或 36 個重要節點

# 接下來，逐一測試

visited = [[False]*N for _ in range(M)] # 兩者挑1種
#visitedSet = set() # 兩者挑1種
nodeDist = [[0]*nodeN for _ in range(nodeN)] # 存 nodeDist[k1][k2]距離
nodeNext = defaultdict(list
                      )
def DFS3(step, i, j, startI, startJ, i2, j2):
    if i<0 or j<0 or i>=M or j>=N: return 0 # 超過範圍，無效
    if lines[i][j]=='#': return 0 # 撞牆，無效
    if i==i2 and j==j2:
        return step # 走到目的地，成功(終止條件)
    if not (i==startI and j==startJ) and posStr(i,j) in nodeSet: return 0 # 別人的結點，無效，
    # 但出發點會出事
    
    #if posStr(i,j) in visitedSet: return 0 # 走過，無效
    #visitedSet.add(posStr(i,j)) # 走過囉
    if visited[i][j]: return 0
    visited[i][j] = True # 走過囉

    ans = 0
    ans = max(ans, DFS3(step+1, i+1, j, startI, startJ, i2, j2))
    ans = max(ans, DFS3(step+1, i-1, j, startI, startJ, i2, j2))
    ans = max(ans, DFS3(step+1, i, j+1, startI, startJ, i2, j2))
    ans = max(ans, DFS3(step+1, i, j-1, startI, startJ, i2, j2))
    visited[i][j] = False # 又退回去囉
    return ans

for k1 in range(nodeN):
    for k2 in range(k1+1, nodeN): # 想知道 k1...k2 的 steps
        # 利用 DFS 來走走看(但要小心是否會繞到有重覆的位置)
        # 因為是單行道，所以保證不會有重覆的路
        #visitedSet = set()
        dist = 0 # 一開始距離是0
        i, j = list(map(int, nodeDict[k1].split() ))
        i2, j2 = list(map(int, nodeDict[k2].split() ))
        now = DFS3(0, i,j, i,j, i2,j2)
        if now==0: continue # 沒有連線，跳過
        nodeDist[k1][k2] = now
        nodeDist[k2][k1] = now
        nodeNext[k2].append(k1)
        nodeNext[k1].append(k2)
#print(nodeDist)    
#for i in range(nodeN):
#    print(' '.join(list(map(str, nodeDist[i]))))
    
# 最後要走到終點
visitedNode = [False]*nodeN
def DFS4(steps, k): # 現在走到k
    if nodeDict[k] == nodeDict[nodeN-1]: # 走到終點
        return steps
        
    if visitedNode[k]: return 0 # 走過，無法走
    visitedNode[k] = True
    
    ans = 0
    for k2 in nodeNext[k]: # k的下一步 k2
        ans = max(ans, DFS4(steps + nodeDist[k][k2], k2))
    visitedNode[k] = False
    return ans

ans = DFS4(0, 0)
print(ans) # Part 2 我的 Puzzle Input 對應答案 6262


