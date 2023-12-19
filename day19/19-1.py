# AdventOfCode2023_Day19
# Day 19: Aplenty
# https://adventofcode.com/2023/day/19

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 19114，在 Part 2 會輸出 167409079868000
lines = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''.splitlines()
#""" # 上面是 Sample Input

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import defaultdict

# 看起來是模擬 if 判斷，從in規則開始
state = 1 # 1:rules, 2:data
rules = {}
ans = 0
inv = defaultdict(list)

def buildInv(tag, rule): # rules[tag] = rule 裡面有一堆規則
    for x in rule: # 每個 x 是有冒號的
        #print('x is', x, 'and last rule[-1] is', rule[-1])
        if x == rule[-1]: # 最後一條規則
            inv[x].append(tag) # 最後一條規則加入
            #print(rule, x, inv[x])
            continue
        x, result= x.split(':')
        inv[result].append(tag) # 把前面的規則加入
        #print(rule, result, inv[result])
    
for line in lines:
    if line == '': # 空字串，後面是
        state = 2
        continue
    if state==1: # rules
        line = line.replace('}', '') # 把結尾的大括號刪掉
        tag, others = line.split('{') # 先把名字斷出來
        rule = others.split(',') # 後面是斷開 if 判斷
        rules[tag] = rule # 裡面有整套 if 判斷
        buildInv(tag, rule)
    if state==2: # data
        data = {}
        line = line.replace('{', '')
        line = line.replace('}', '')
        a = line.split(',')
        #print(a)
        for p in a: # k=v pair
            k,v = p.split('=')
            #print(k,v)
            data[k] = int(v) # 完成 data
        
        # 開始跑 rules
        now = 'in'
        while now!='A' and now!='R': # 還沒到 Accept or Reject 的話
            rule = rules[now]
            for x in rule: # 每個 x 是有冒號的
                #print('x is', x, 'and last rule[-1] is', rule[-1])
                if x == rule[-1]: # 最後一條規則
                    now = x
                    break # 離開此rule的迴圈
                x, result= x.split(':')
                c = x[0] # 某個字母
                cmp = x[1] # 比大小
                val = int(x[2:])
                #print(c, cmp, val)
                if cmp=='>' and data[c]>val: # 太好了，找到規則
                    now = result
                    break  # 離開此rule的迴圈
                if cmp=='<' and data[c]<val:
                    now = result
                    break  # 離開此rule的迴圈
        #print(now)
        if now=='A':
            hello = data['x']+data['m']+data['a']+data['s']
            #print(hello)
            ans += hello
print(ans) # Part 1 我的 Puzzle Input 對應答案 263678



