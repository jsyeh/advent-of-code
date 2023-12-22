# AdventOfCode2023_Day22
# Day 22: Sand Slabs
# https://adventofcode.com/2023/day/22

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 5，在 Part 2 會輸出 7
lines = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import *

# 很像 Tetris 一樣, 格子慢慢往下掉
# 要以 z 的值排序,以便從低到高慢慢增加, 並更新 height map
# 把格子準備, 以便填資料

# 兩邊包含的長方體, z=0是地板, z=1是最下面的方塊
# 疊在一起的方塊,如果沒有人壓到它, 那它就是安全的、可以拆解的
# 如果兩個以上的人「合作」撐住,那也是安全「可拆解」的, 因為只是確定是否安全。
N = len(lines) # 有幾個 brick
brick = [] # 裡面要放全部的 brick

a, b = lines[0].split('~') # 先拿其中一組, 計算 max1, max2, min1, min2 分別為 x,y的極值
x,y,z = list(map(int, a.split(',') )) # 先拿一組來當max/min 的值
max1, min1, max2, min2, max3, min3= x,x, y,y, z, z

for line in lines: # 最多有1455行, 沒有負的
    a, b = line.split('~') # 兩個頂點的方向
    x,y,z = list(map(int, a.split(',') ))
    x2,y2,z2 = list(map(int, b.split(',') ))
    x,x2 = min(x,x2), max(x,x2) # 小到大
    y,y2 = min(y,y2), max(y,y2)
    z,z2 = min(z,z2), max(z,z2)
    brick.append([x,y,z,x2,y2,z2])
    # 找到最大值、最小值, 方便開 height array
    min1 = min(min1, x)
    max1 = max(max1, x2)
    min2 = min(min2, y)
    max2 = max(max2, x2)
    min3 = min(min3, z)
    max3 = max(max3, z2)
#print(min1,min2,min3, max1,max2,max3) # 印出空間的大小範圍

brick.sort(key=lambda x:x[2])
#for b in brick:
#    print(b)
# 有了 brick資料, 接下來「逐一往下掉」
space = space = [[[-1]*(max3+1) for y in range(max2+1)] for x in range(max1+1)]
height = [[0]*(max2+1) for _ in range(max1+1)]
max33 = 0
for i,b in enumerate(brick):
    x,y,z, x2,y2,z2 = b
    posZ = 0
    for xx in range(x,x2+1):
        for yy in range(y,y2+1): # 先看目前 height[xx][yy] 的最大值
            posZ = max(posZ, height[xx][yy])
    # 找到最大值後, 要把整個方塊,逐一放上去, 並更新 height[xx][yy]
    posZ += 1 # 上面一格,開始放
    for xx in range(x,x2+1):
        for yy in range(y,y2+1):
            height[xx][yy] = posZ + (z2-z) # 抬高
            for zz in range(z2-z+1):
                space[xx][yy][posZ+zz] = i
            max33 = max(max33, height[xx][yy])
                
    brick[i] = [x,y,posZ, x2,y2, z2-z+posZ] # 更新, 小心右邊是否正確
    #print(brick[i])
# 放好 brick 後, 便可以開始逐一檢查上方有沒有人
#for b in brick:
#    print(b)

'''
for zz in range(max33,0,-1): # 印出 z-x 平面
    for xx in range(max1+1):
        now = '.'
        for yy in range(max2+1):
            i = space[xx][yy][zz]
            if i==-1: continue
            if now=='.': now = chr(ord('A')+i)
            elif now==chr(ord('A')+i): now = now # 不變
            else: now = '?'
        print(now, end='')
    print()
print()
for zz in range(max33,0,-1): # 印出 z-y 平面
    for yy in range(max2+1):
        now = '.'
        for xx in range(max1+1):
            i = space[xx][yy][zz]
            if i==-1: continue
            if now=='.': now = chr(ord('A')+i)
            elif now==chr(ord('A')+i): now = now # 不變
            else: now = '?'
        print(now, end='')
    print()
print()
'''
aboves = [set() for i in range(N)] # aboves[i] 表示 i上面的人有誰
below = defaultdict(list) # below['B'] = {'A'}  表示 'B'下面只有1個
#print('N',N,len(brick))
for i in range(N): # 針對每個 brick 去做處理
    x,y,z, x2,y2,z2 = brick[i]
    #print(x,y,z, x2,y2,z2)
    above = set()
    for xx in range(x,x2+1):
        for yy in range(y,y2+1):
            for zz in range(z,z2+1):
                up = space[xx][yy][zz+1] # 上方的方塊
                if up!=i and up!=-1: # 上方方塊,不是本人本方塊
                    above.add(up)
    #print(i, above)
    #if len(above)==0 or len(above)>1: # 沒有人
    #    ans += 1
    aboves[i] = above
    for k in above:
        below[k].append(i)
ans = 0
mustHave = set()
for k in below:
    #print(chr(k+ord('A')), below[k])
    if len(below[k])==1: 
        mustHave.add(below[k][0])
        #print(below[k][0])

ans = N - len(mustHave)
print(ans) # Part 1 我的 Puzzle Input 對應答案 505



