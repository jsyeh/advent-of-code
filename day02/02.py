# AdventOfCode2024_Day02
# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/2

# 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 2，在 Part 2 會輸出 4
lines = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''.splitlines()
# 上面是 Sample Input
# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
# 上面兩行不要註解，便能使用我的 Puzzle Input
# Puzzle Input 在 Part1 會輸出 534，在 Part 2 會輸出 577

ans = 0
for line in lines:
    a = list(map(int, line.split()))
    N = len(a)
    diff = a[1]-a[0]
    good = 0
    for i in range(N-1):
        if diff>0 :
            if 3>=a[i+1]-a[i]>=1: good+=1
        elif diff<0:
            if -3<=a[i+1]-a[i]<=-1: good+=1
    if good==N-1: ans+=1
    # 全增加 or 全減少, 距離介於 1-3之間
print(ans)

print("====Part 2====")
# 可以去掉1個

ans = 0
for line in lines:
    a = list(map(int, line.split()))
    N = len(a)
    for bad in range(N): # 可以去掉1個
        a = a[:bad] + a[bad+1:] # 去掉 a[bad] 這個數
        N = N-1 # 少1個
        # 去除後, 試試看(作法和 Part 1 一樣)
        diff = a[1]-a[0]
        good = 0
        for i in range(N-1):
            if diff>0 :
                if 3>=a[i+1]-a[i]>=1: good+=1
            elif diff<0:
                if -3<=a[i+1]-a[i]<=-1: good+=1
        if good==N-1:
            ans+=1
            break  # 一旦試成功, 就不用再試其他 a[bad] 了
print(ans)

