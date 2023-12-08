# AdventOfCode2023_Day01
# Day 1: Trebuchet?!
# https://adventofcode.com/2023/day/1

#""" # 下面是簡單的 Sample Input 1 測資，在 Part 1 會輸出 142（Part 2用另一組）
lines = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''.splitlines()
#""" # 上面是 Sample Input 1

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

ans = 0
for line in lines:
    first, last = -1, -1
    for c in line:
        if c.isdigit():
            if first==-1:
                first = int(c)
            last = int(c)
    # print(first, last, first*10+last)
    ans += first*10 + last
print(ans) # Part 1 我的 Puzzle Input 對應答案 54331


print("====Part 2====")
# 要把 one two three four five six seven eight nine 也讀入

""" # 以下是 Sample Input 2 測資，在 Part 2 會輸出 281
lines = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''.splitlines()
""" # 上面是 Sample Input 2

ans = 0
table = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in lines:
    first, last = -1, -1
    firstI, lastI = -1, -1
    for i,c in enumerate(line):
        if c.isdigit():
            if first==-1:
                first = int(c)
                firstI = i
            last = int(c)
            lastI = i
    # 上方與 Part 1 相同
    # 下方則針對 one two three four five six seven eight night
    for tableI, word in enumerate(table):
        first2I, last2I = line.find(word), line.rfind(word)
        #if line=="eightwothree": print('last2I', last2I, 'lastI', lastI)
        if first2I != -1 and (firstI==-1 or first2I < firstI): # 之前沒有，或更左邊
            firstI = first2I
            first = tableI # 會對應一個數字
        if last2I != -1 and (lastI==-1 or lastI < last2I): # 之前沒存過，或更右邊
            lastI = last2I
            last = tableI # 會對應一個數字
    #print(first, last, first*10+last)
    ans += first*10 + last
print(ans) # Part 2 我的 Puzzle Input 對應答案 54518


