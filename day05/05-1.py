# AdventOfCode2023_Day05
# Day 5: If You Give A Seed A Fertilizer
# https://adventofcode.com/2023/day/5

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 35，在 Part 2 會輸出 46
lines = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

# 要找到最小的location number
# seeds:
# 接下來的 map 順序 seed, soil, ferti, water, light, temp, humid, location

table = []
for line in lines:
    a = line.split()
    if len(a)>0 and a[0]=='seeds:': # 遇到種子，就把全部值讀入
        seed = list(map(int, a[1:])) # 右邊的全部數字
    elif len(a)==2 and a[1]=='map:': # 右邊是 map: 時，做新的對照表
        table = [] # 新的對照表
    elif len(a)==0: # 遇到空白行，就照著對照表，逐個做翻譯
        seed2 = [] # 轉換結果先放到 seed2
        for s in seed: # 每一個種子
            seed2.append(s)
            for dst,src,ran in table:
                if src<=s<src+ran: # 若 seed 在範圍內
                    seed2[-1] = (s-src+dst) # 就照著公式轉換
                    break
        seed = seed2 # 再把 seed2 放回 seed
    else:
        table.append( (int(a[0]), int(a[1]), int(a[2])) )

print(min(seed)) # Part 1 我的 Puzzle Input 對應答案 535088217


