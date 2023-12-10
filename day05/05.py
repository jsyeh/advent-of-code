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


print("====Part 2====")
# 超難，因為數字實在是太多了！！不能逐個去測。
# 可利用 seed 的範圍版本，切、再切！ 越切越細、越多群！
table = []
for line in lines:
    a = line.split()
    if len(a)>0 and a[0]=='seeds:':
        seed = list(map(int, a[1:]))
        seed2 = []
        for i in range(0, len(seed), 2):
            seed2.append([seed[i], seed[i+1]])
        seed = seed2
        #print(seed)
    elif len(a)==2 and a[1]=='map:': # 準備做新的對照表
        table = []
    elif len(a)==0: # 遇到空白行，就開始照對照表，做翻譯
        seed2 = []
        seed.sort()
        #print(seed)
        # 如果 seed 全部在外面的話，要再推回 seed 裡
        #print('len(table)',len(table))
        for dst,src,ran in table: # 以表格為主
            remain_seed = []
            for a1,r in seed: # 許多連續的區間, 逐一看能不能被切到
                #print("for seed", a1, r)
                a2 = a1 + r - 1
                b1, b2 = src, src+ran-1
                # 關於 overlapping 有幾種狀況：a1 b1 a2 b2 要切2段
                # a1 b1 b2 a2 要切3段, b1 a1 b2 a2 要切2段
                # b1 a1 a2 b2 就只有1段 （ a1 a2 b1 b2 或 b1 b2 a1 a2 不處理）
                if a1<b1<a2<=b2: # 要切2段
                    # [a1..b1) 不動
                    remain_seed.append([a1, b1-a1])
                    # [b1..a2] 要轉 b1就是src,換成dst
                    seed2.append([dst, a2+1-b1])
                elif a1<b1<b2<a2: # 要切3段
                    # [a1..b1) 不動
                    remain_seed.append([a1, b1-a1])
                    # [b1..b2] 要動
                    seed2.append([dst, b2+1-b1])
                    # (b2..a2] 不動
                    remain_seed.append([dst+ran, a2-b2])
                elif b1<=a1<a2<=b2: # 就只有1段
                    # [a1..a2] 要動
                    seed2.append([a1-b1+dst, r])
                elif b1<=a1<b2<a2: # 要切2段
                    # [a1..b2] 要動
                    seed2.append([a1-b1+dst, b2-a1+1])
                    # b2..a2 不動
                    remain_seed.append([b2, a2+1-b2])
                else:
                    remain_seed.append([a1,r])
            seed = remain_seed
        seed2 += seed
        seed = seed2
    else:
        table.append( (int(a[0]), int(a[1]), int(a[2])) )
        # print('table append', len(table))
seed.sort()
print(seed[0][0]) # Part 1 我的 Puzzle Input 對應答案 51399228


