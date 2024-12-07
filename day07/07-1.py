# AdventOfCode2024_Day07
# Day 7: 
# https://adventofcode.com/2024/day/7

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 3749
lines = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''.splitlines()
#""" # 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 66343330034722

# 可行的方程式（數字間可插入 '+' 或 '*'），把答案加起來
debugAns = []
def helper(target, ans, arr, i, N):  # 要做加法、乘法（左到右）
    if i==N:
        if target==ans: return target
        else: return 0
    ans1 = helper(target, ans+int(arr[i]), arr, i+1, N)
    if ans1>0: return ans1
    
    ans2 = helper(target, ans*int(arr[i]), arr, i+1, N)
    return ans2
    
ans = 0
for line in lines:
    target, eq = line.split(':')
    target, a = int(target), eq.split()
    
    # 使用 DFS 把全部可能都試一次，a[0]是最前面項
    ans += helper(target, int(a[0]), a, 1, len(a))

print(ans) # Part 1 我的 Puzzle Input 對應答案 66343330034722
