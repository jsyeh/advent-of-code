# AdventOfCod2023_Day12
# Day 12: Hot Springs
# https://adventofcode.com/2023/day/12

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 21，在 Part 2 會輸出 525152
lines = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

from functools import cache
# print(len(lines)) # 1000 行

# 接下來用 DP 來看 good 是否為 records 的子字串
# 能走到最後, 就是成功
# 利用 Top-Down Dynamic Programming 的方法 (好像倒過來寫更漂亮)
@cache
def dp(records:str, good:str, i:int, j:int, M:int, N:int)->int:
    if i==M and j==N: return 1 # 順利結束
    if j==N and records[i:].find('#')==-1: return 1
    if i>=M or j>=N: return 0 # 失敗
    ans = 0
    if records[i]=='#' and good[j]=='#':
        ans += dp(records, good, i+1, j+1, M, N)
    if records[i]=='.' and good[j]=='.':
        ans += dp(records, good, i+1, j+1, M, N)
    if records[i]=='?' and good[j]=='#':
        ans += dp(records, good, i+1, j+1, M, N)
    if records[i]=='?' and good[j]=='.':
        ans += dp(records, good, i+1, j+1, M, N)
    if records[i]=='?' and good[j]=='#' and (j==0 or good[j-1]!='#'):
        ans += dp(records, good, i+1, j, M, N)
    if records[i]=='.' and good[j]=='#' and (j==0 or good[j-1]!='#'):
        ans += dp(records, good, i+1, j, M, N)
    return ans

ans = 0
for line in lines:
    records, a = line.split()
    a = list(map(int, a.split(',') ))
    good = ''
    for d in a:# Idea: 可以先生成字串, 再看字串能怎麼排列組合
        if good!='': good += '.'
        good += '#'*d # 有幾個數字
    #print(records, good)
    now = dp(records, good, 0, 0, len(records), len(good))
    ans += now
print(ans) # Part 2 我的 Puzzle Input 對應答案 7633



