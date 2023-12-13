# AdventOfCode2023_Day13
# Day 13: Point of Incidence
# https://adventofcode.com/2023/day/13

#""" # 下面是簡單的 Sample Input 1 測資，在 Part 1 會輸出 405，在 Part 2 會輸出 400
lines = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

def findAns(scene, old):
    M, N = len(scene), len(scene[0])
    # 先測 row r, 也就是 
    for r in range(0,M-1): # 鏡子可能放的位置
        bad = 0
        for i in range(r+1):
            dist = r+1+(r-i) # 從 r+1 往下走 (r-i)格，便是 i 對應的鏡像層
            if dist<M and scene[i] != scene[dist]: # 竟然沒對稱，就錯了
                bad = 1
                break
        if bad==0 and (r+1)*100 !=old: # 避開某個位置
            #print('find row:', r, r+1)
            return (r+1)*100
    # 再測 col c
    for c in range(0,N-1):
        bad = 0
        for j in range(c+1):
            dist = c+1+(c-j)
            if dist<N:
                for i in range(M):
                    if scene[i][j] != scene[i][dist]:
                        bad = 1
                        break
            if bad==1: break
        if bad==0 and c+1 != old: # 避開某個位置
            #print('find col:', c, c+1)
            return c+1
    return -1

inv = {'#':'.', '.':'#'} # 用來將 # 及 . 互換的 inv[] 對照表

ans = 0
count = 0
scene = [] # 空 的 scene
for i,line in enumerate(lines):
    #print(len(line))
    if len(line)==0 or i==len(lines)-1: # 斷開（空白行or最後一行）
        if i==len(lines)-1:
            scene.append(line) # 最後一行，需要補齊最後一行
        M, N = len(scene), len(scene[0])
        part1 = findAns(scene, -1)
        ans += part1

        scene2 = [list(scene[k]) for k in range(M)]
        #print(scene) # 題目規定「一定要不同」所以一定要移動 ans 的值，不能相同
        #print(count)
        #print('part1', part1)
        count+=1
        scene = [] # 新的開始
    else:
        scene.append(line) # 加到 scene 裡

print(ans) # Part 1 我的 Puzzle Input 對應答案 30518



