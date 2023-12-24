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


print("====Part 2====")
# 使岩石與每個冰雹完美碰撞
# 找到 x,y,z, vx,vy,vz 去撞全部的冰雹
# 隨著時間流逝，難道是要解300個式的方程式組嗎？
# 有沒有公式，能把 x+vx*t == x[i]+vx[i]*t
#               y+vy*t == y[i]+vy[i]*t
#.              z+vz*t == z[i]+vy[i]*t
# 也就是，這些射線，必定與某個角度的投影中「交於1點」
# 要畫出來嗎？
# 平行的部分，按示要怎麼走
#for i in range(N):
#    x1, y1, z1 = pos[i]
#    vx1, vy1, vz1 = v[i]
#    for j in range(i+1,N):
#        x2, y2, z2 = pos[j]
#        vx2, vy2, vz2 = v[j]
#        if vx1*vy2==vx2*vy1: # 平行，不相交
#            print(v[i], v[j], 'parallel', pos[i], pos[j]) # sorry 只有
# [14, -19, 7] [14, -19, -5] parallel
# [68, 34, -77] [40, 20, -44] parallel
# 沒有任2條線是(dx,dy,dz)都平行的，好可惜

# 每次撞到，都是在整數的位置、整數的時間
# 有人分享： 其實3條線，就若在某方向交於1點，那個方向便是direction方向的答案
# 原本向量 vx,vy,vz ，nx,ny,nz 要轉到 0,0,z 需要 from-to rotation
# cross(N,Z) 是轉動軸，轉動角度是t，就是用內積可以得到角度，

# 但是，我的作法，沒有信心能得到正確的答案
# 最後只好屈服，第一次去看 reddit 上面別人的寫法，使用 Microsoft Z3 來解答案
'''
# python3.9 a.py
# 在電腦裡，先 pip install z3-solver 安裝好後，才能使用 z3
from z3 import *
x = Int('x')
y = Int('y')
z = Int('z')
vx = Int('vx')
vy = Int('vy')
vz = Int('vz')
t1 = Int('t1')
t2 = Int('t2')
t3 = Int('t3')
solve(x+vx*t1 == 19-2*t1, y+vy*t1 == 13+1*t1, z+vz*t1 == 30-2*t1, x+vx*t2 == 18-1*t2, y+vy*t2 == 19-1*t2, z+vz*t2 == 22-2*t2, x+vx*t3 == 20-2*t3, y+vy*t3 == 25-2*t3, z+vz*t3 == 34-4*t3)
print('====Part 2====')
x = Int('x')
y = Int('y')
z = Int('z')
vx = Int('vx')
vy = Int('vy')
vz = Int('vz')
t1 = Int('t1')
t2 = Int('t2')
t3 = Int('t3')
solve(x+vx*t1 == 246694783951603+54*t1, y+vy*t1 == 201349632539530-21*t1, z+vz*t1 == 307741668306846+12*t1, x+vx*t2 == 220339749104883+77*t2, y+vy*t2 == 131993821472398+7*t2, z+vz*t2 == 381979584524072-58*t2, x+vx*t3 == 148729713759711+238*t3, y+vy*t3 == 225554040514665+84*t3, z+vz*t3 == 96860758795727+360*t3)
# 它會印出
# [y = 463714142194110,
# vx = 26,
# t3 = 573879763083,
# x = 270392223533307,
# vy = -331,
# t1 = 846337127918,
# t2 = 981421067224,
# vz = 53,
# z = 273041846062208]
z = 273041846062208
x = 270392223533307
y = 463714142194110
print(x,y,z,x+y+z)
# 270392223533307 463714142194110 273041846062208 1007148211789625
'''
int ans = 1007148211789625
print(ans) # Part 2 我的 Puzzle Input 對應答案 1007148211789625


