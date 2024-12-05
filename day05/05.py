# AdventOfCode2024_Day05
# Day 5: Print Queue
# https://adventofcode.com/2024/day/5

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 143，在 Part 2 會輸出 123
lines = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''.splitlines()
#""" # 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 6242，在 Part 2 會輸出 5169

# Input 「前面」先給 a|b 的前後關係
# 「後面」 list 對應的「頁數」是不是排好順序？找正確的那些 list 的中間的數，再加起來

# 後來發現 Part 2 和 Part 1 非常相關，所以合在一起、重寫。
from collections import defaultdict
from functools import cmp_to_key
state = 1  # 用來分開「前面」與「後面」的資料
ans, ans2 = 0, 0
path = defaultdict(list)  # 記錄「前面」的 a|b 前後關係

def compare(a, b):  # 利用「前後關係」來排序，供後面 key=cmp_to_key(compare)
    if b in path[a]: return -1  # a前、b後，正確、不用調順序
    if a in path[b]: return +1  # b前、a後，不正確，要調順序
    return 0  # 沒有任何限制

for line in lines:
    if line=='':  # 遇到空白行，就切換到 state 2 讀「後面」list 對應的「頁數」
        state = 2
    elif state==1:
        a, b = list(map(int, line.split('|') ))  # 斷開、變成整數
        path[a].append(b)  # 建立「前後關係」
    elif state==2:
        a = list(map(int, line.split(',')))  # 後面的數字，對應故事裡的「頁數」
        b = sorted(a, key=cmp_to_key(compare))  # 利用「前後關係」來排序
        if a==b: ans += a[len(a)//2]  # 順序正確，取出中間的數，加到 Part 1
        else: ans2 += b[len(b)//2]  # 順序錯誤，取「排序後」中間的數，加到 Part 2

print(ans) # Part 1 我的 Puzzle Input 對應答案 6242

print("====Part 2====")

print(ans2) # Part 2 我的 Puzzle Input 對應答案 5169

