# AdventOfCode2024_Day03
# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/3

# 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 161，在 Part 2 會輸出 48
lines = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
'''.splitlines()

lines = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
'''.splitlines()
# 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 171183089，在 Part 2 會輸出 63866497

import re
ans = 0
for line in lines:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # 程式會比對出 mul(a,b)
    matches = re.findall(pattern, line)  # 會把 a b 放入 matches 裡
    for a, b in matches:
        ans += int(a) * int(b)

print(ans)

print("====Part 2====")

ans = 0
enable = True
for line in lines:
    tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", line)
    # 先將3種有效字串取出： mul(a,b)             或 do() 或don't()  
    # 符合的(用圓括號括起)會放入tokens

    for token in tokens:
        if token=="do()":  # 符合 do()
            enable = True
        elif token=="don't()":  # 符合 don't()
            enable = False
        elif re.fullmatch(r"mul\((\d{1,3}),(\d{1,3})\)" , token):  # 符合 mult(a,b)
            if enable:  # 而且 eenable 開啟
                matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", token);
                a, b = matches[0]
                ans += int(a) * int(b)
print(ans)

