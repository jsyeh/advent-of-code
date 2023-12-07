# AdventOfCode2023_Day02
# Day 2: Cube Conundrum
# https://adventofcode.com/2023/day/2

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 8，在 Part 2 會輸出 2286
lines = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

ans = 0
# 這題麻煩在斷字
for line in lines:
    a = line.split()
    gameID = int(a[1][:-1])
    # print(gameID) #print(a[1].split(':'))
    bad = False
    for i in range(2,len(a), 2):
        n = int(a[i])
        if a[i+1].find('red')==0 and n>12: bad = True
        if a[i+1].find('green')==0 and n>13: bad = True
        if a[i+1].find('blue')==0 and n>14: bad = True
    if not bad:
        ans += gameID
print(ans) # Part 1 我的 Puzzle Input 對應答案 2771



