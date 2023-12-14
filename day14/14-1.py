# AdventOfCode2023_Day14
# Day 14: Parabolic Reflector Dish
# https://adventofcode.com/2023/day/14

# 題目看起來好像 2048 4096 這類的遊戲, 可以把石頭 推向某一側
# 題目 Part 1 只往上方推, 每個圓石重量是「岩石到平台南邊緣的行數，包括岩石所在行」
# 「總荷載是所有圓形岩石產生的荷載總和」

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 136，在 Part 2 會輸出 64
lines = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''.splitlines()
#""" # 上面是 Sample Input

# 下面是從 stdin 讀入 我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

M, N = len(lines), len(lines[0])

def showTable():
    for i in range(M):
        print(''.join(table[i]))
    print()

def part1(table):
    colLoad = [M]*N # 每個 col 目前將放的石頭的重量
    ans = 0
    for i in range(M):
        for j in range(N):
            if table[i][j] == 'O': # 要把石頭放在 colLoad[j] 的位置
                ans += colLoad[j]
                colLoad[j] -= 1 # 用掉一格,下一格的重量少1
            if table[i][j] == '#': # 要更新 colLoad[j]
                colLoad[j] = M-i-1 # 格子的再下一格可以放
    return ans

# 先把 str 變成 list，方便移動石頭時，可改變內容
table = [[lines[i][j] for j in range(N)] for i in range(M)]
ans = part1(table)
print(ans) # Part 1 我的 Puzzle Input 對應答案 112048



