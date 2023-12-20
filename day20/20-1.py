# AdventOfCode2023_Day20
# Day 20: Pulse Propagation
# https://adventofcode.com/2023/day/20

#""" # 下面是簡單的 Sample Input 1 測資，只能在 Part 1 執行，在 Part 1 會輸出 32000000
lines = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''.splitlines()
#""" # 上面是 Sample Input 1

# In the first example, the same thing happens every time the button is pushed: 8 low pulses and 4 high pulses are sent. So, after pushing the button 1000 times, 8000 low pulses and 4000 high pulses are sent. Multiplying these together gives 32000000.

""" # 下面是簡單的 Sample Input 2 測資，只能在 Part 1 執行，在 Part 1 會輸出 11687500
lines = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''.splitlines()
""" # 上面是 Sample Input 2

# In the second example, after pushing the button 1000 times, 4250 low pulses and 2750 high pulses are sent. Multiplying these together gives 11687500.

# 下面兩行不要註解，便能使用我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()
from collections import *

# 先試著解決, 要做出 graph 連結的狀態, 以便模擬
ops = defaultdict(list) # ops['a']=['%', 'inv', 'con'] 表示動到 a 時, 會影收到 'inv' 及 'con'
conAll = set()
for line in lines:
    line = line.replace(',','')
    name = line.split()
    if name[0]=='broadcaster': # 有找到 broadcaster
        broadcaster = name[2:] # 把後面的op記起來, 是一開始要做事的人, 都會傳 Lo
    else:
        now, nowType = name[0][1:], name[0][0]
        name.insert(2, nowType)
        ops[now] = name[2:]
        # '%': # Flipflop 收到Hi不做事。收到Lo 時 Hi, Low 切換, 變成Hi,就會傳出Hi
        # '&': # Conjunction,全部都是Hi 時,會回傳Lo。其他回傳Hi
        if nowType=='&': conAll.add(now) # conAll 裡, 要記得誰是 '&'
# 全部記錄完後, 要將 con 的上游都記起來
conPrev = defaultdict(list)
for c in conAll: # 每次挑一個 con, 收集它的上游
    for opName in ops: # 對所有的 ops
        theNext = ops[opName]
        if c in theNext:
            conPrev[c].append(opName)
#print('broadcaster', broadcaster)
#print('ops', ops)
#print('conAll', conAll)
#print('conPrev', conPrev)
    
# 按下按鈕1000次數, 進行模擬。感覺和之前一題 有循環 的那題很像
# 資料會傳來傳去, 所以要丟到 queue 裡面處理
state = {op:False for op in ops} # False 表示 Low
send = {op:False for op in ops} # 都先送出 Low
#print(state)

def simulation():
    # 少算了 button -low broadcaster
    sendTime[False] += 1
    #print("====")
    queue = deque()
    for b in broadcaster:
        queue.append((b,False)) # 先由 broadcaster 送出 Flase/Low 出去
        #print('broadcast', '-low', b)
        sendTime[False]+=1
    while len(queue)>0:
        op, HiLo = queue.popleft()
        if ops[op][0]=='%': # Flipflop
            # '%': # Flipflop 收到Hi不做事。收到Lo 時 Hi, Low 切換, 變成Hi,就會傳出Hi
            if HiLo==False: # Lo 才做狀態改變
                state[op] = not state[op]
                send[op] = state[op] # 會送出的值
                for other in ops[op][1:]: # 把現在的狀態,傳給後面的人
                    if other in ops: # 解決 output 不做事的困境
                        queue.append((other,send[op]))
                    #print(op, '-low' if send[op]==False else '-high', other)
                    sendTime[send[op]]+=1
        if ops[op][0]=='&': # conjunction
            # '&': # Conjunction,全部都是Hi 時,會回傳Lo。其他回傳Hi
            # 先看上游是否都是 Hi
            bad = False
            for friend in conPrev[op]: # 逐一檢查上游的朋友
                if send[friend]==False: # 只要有一個不是Hi
                    bad = True # 就無法達成全Hi
            if bad: # 無法全Hi, 就會回傳 Hi
                state[op] = True
                send[op] = True
            else: # 全 Hi, 回傳 Low
                state[op] = False
                send[op] = False
            for other in ops[op][1:]: # 把現在的訊號,傳給後面的人
                if other in ops: # 解決 output 不做事的困境
                    queue.append((other, send[op]))
                #print(op, '-low' if send[op]==False else '-high', other)
                sendTime[send[op]]+=1


ans = 0
sendTime = {False:0, True:0}
for k in range(1000): # 要模擬4次
    simulation()
                
#print('sendHigh', sendTime[True])
#print('sendLow', sendTime[False])
ans = sendTime[False]*sendTime[True]
print(ans) # Part 1 我的 Puzzle Input 對應答案 808146535



