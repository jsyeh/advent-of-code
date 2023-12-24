# AdventOfCode2023_Day24
# Day 24: Never Tell Me The Odds
# https://adventofcode.com/2023/day/24

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 2，在 Part 2 會輸出 47
lines = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input 300行
import sys
lines = sys.stdin.read().splitlines()

pos, v = [], []
for line in lines:
    line = line.replace(',', '')
    line = line.replace('@', '')
    x,y,z, vx,vy,vz = list(map(int, line.split() ))
    # print(x,y,z, vx,vy,vz)
    pos.append([x,y,z])
    v.append([vx,vy,vz])
# 冰雹相互path cross碰撞並粉碎，完全忽略 Z 軸。
# 單方向的射線, test area 不往回看

x0, x3 = 7, 27
x0, x3 = 200000000000000, 400000000000000

N = len(pos)
ans = 0
for i in range(N):
    x1, y1, z1 = pos[i]
    vx1, vy1, vz1 = v[i]
    for j in range(i+1,N):
        x2, y2, z2 = pos[j]
        vx2, vy2, vz2 = v[j]
        if vx1*vy2==vx2*vy1: 
            #print(pos[i], pos[j], 'parallel')
            continue # 平行，不相交
        # x1+s*vx1 == x2+t*vx2 都乘 vy2
        # y1+s*vy1 == y2+t*vy2 都乘 vx2
        # x1*vy2-y1*vx2 + s(vx1*vy2-vy1*vx2) = x2*vy2-y2*vx2  相減
        s = (x2*vy2-y2*vx2 - (x1*vy2-y1*vx2))/(vx1*vy2-vy1*vx2)
        t = (x1+s*vx1-x2)/vx2
        x, y = x1+s*vx1, y1+s*vy1
        # print(pos[i],pos[j], x1+s*vx1, y1+s*vy1, s, t)
        if s<0: continue # past
        if t<0: continue # past
        if x<200000000000000 or x>400000000000000 or y<200000000000000 or y>400000000000000: continue # outside
        # inside: 找出至少7和最多分別與 X 和 Y 位置發生的交叉點27
        ans += 1

print(ans) # Part 1 我的 Puzzle Input 對應答案 14799



