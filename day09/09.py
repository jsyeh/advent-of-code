# AdventOfCode2023_Day9
# Day 9: Mirage Maintenance
# https://adventofcode.com/2023/day/9

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 114，在 Part 2 會輸出 2
lines = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

ans = 0
ans2 = 0
for line in lines:
    a = list(map(int, line.split() ))
    #print(a)
    N = len(a)
    table = [a]
    L = 0 # Level
    while True:
        b = [table[L][i+1]-table[L][i] for i in range(N-1-L)]
        table.append(b)
        L += 1
        if max(b)==min(b)==0: break
    # print(table)
    now = 0
    for LL in range(L-1, -1, -1): now += table[LL][-1]
    ans += now
    # ==== Part 2 ====
    now = 0
    for LL in range(L-1, -1, -1):
        #print('LL', LL, 'table[LL][0]', table[LL][0], '-', now, '=', table[LL][0] - now)
        now = table[LL][0] - now
    #print(table)
    #print('now:', now)
    ans2 += now
    
print("ans:", ans) # Part 1 我的 Puzzle Input 對應答案 1887980197


print("====Part 2====")
print('ans2:', ans2) # Part 2 我的 Puzzle Input 對應答案 990


