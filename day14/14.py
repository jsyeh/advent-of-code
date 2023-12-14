# AdventOfCode2023_Day14
# Day 14: Parabolic Reflector Dish
# https://adventofcode.com/2023/day/14

# 題目看起來好像 2048 4096 這類的遊戲, 可以把石頭 推向某一側
# 題目 Part 1 只往上方推, 每個圓石重量是「岩石到平台南邊緣的行數，包括岩石所在行」
# 「總荷載是所有圓形岩石產生的荷載總和」

#""" # 下面是簡單的 Sample Input 測資，在 Part 1 會輸出 136，在 Part 2 會輸出 64
lines = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''.splitlines()
#""" # 上面是 Sample Input

# 下面是從 stdin 讀入 我的 Puzzle Input
import sys
lines = sys.stdin.read().splitlines()

M, N = len(lines), len(lines[0])

def showTable():
    for i in range(M):
        print(''.join(table[i]))
    print()

def part1(table):
    colLoad = [M]*N # 每個 col 目前將放的石頭的重量
    ans = 0
    for i in range(M):
        for j in range(N):
            if table[i][j] == 'O': # 要把石頭放在 colLoad[j] 的位置
                ans += colLoad[j]
                colLoad[j] -= 1 # 用掉一格,下一格的重量少1
            if table[i][j] == '#': # 要更新 colLoad[j]
                colLoad[j] = M-i-1 # 格子的再下一格可以放
    return ans

# 先把 str 變成 list，方便移動石頭時，可改變內容
table = [[lines[i][j] for j in range(N)] for i in range(M)]
ans = part1(table)
print(ans) # Part 1 我的 Puzzle Input 對應答案 112048


print('====Part 2====')
# 向北滾動，然後向西，然後向南，然後向東滾動
# 經過1000000000循環後, 北支撐樑上的總荷載為64
# 總共有 1,000,000 個格子, 其中2031個圓石
# 我猜做幾次之後, 就會穩定了, 不需要真的跑那麼多次的循還

# 先把 str 變成 list，方便移動石頭時，可改變內容
table = [[lines[i][j] for j in range(N)] for i in range(M)]

# 利用 table 做出 hashtable。
history = {} # key 是地圖盤面字串，value 是 (step k 及「石頭總重」)

def part2(table):
    #colLoad = [M]*N # 每個 col 目前將放的石頭的重量
    ans = 0
    for i in range(M):
        for j in range(N):
            if table[i][j] == 'O': # 要把石頭放在 colLoad[j] 的位置
                ans += M-i
    return ans

for k in range(1,1000001): # 不會真的做那麼多次啦，發現 k..prev 循環 會break
    colPos = [0]*N # 下次堆石頭的位置 
    for i in range(M): # 往北的一輪, 所以 i 從小到大
        for j in range(N):
            if table[i][j] == 'O':
                table[i][j] = '.' # 舊位置變空
                table[colPos[j]][j] = 'O' # 新位置放圓石
                colPos[j] += 1
            if table[i][j] == '#':
                colPos[j] = i+1 # 下次會放的格子位置
    # showTable()

    rowPos = [0]*M # 下次堆石頭的位置 
    for j in range(N): # 往西的一輪, 所以 j 從小到大
        for i in range(M):
            if table[i][j] == 'O':
                table[i][j] = '.'
                table[i][rowPos[i]] = 'O' # 新位置放圓石
                rowPos[i] += 1
            if table[i][j] == '#':
                rowPos[i] = j+1 # 下次會放的格子位置
    # showTable()

    colPos = [M-1]*N # 下次堆石頭的位置 
    for i in range(M-1,-1,-1): # 往南的一輪, 所以 i 從大到小
        for j in range(N):
            if table[i][j] == 'O':
                table[i][j] = '.'
                table[colPos[j]][j] = 'O' # 新位置放圓石
                colPos[j] -= 1
            if table[i][j] == '#':
                colPos[j] = i-1 # 下次會放的格子位置
    # showTable()

    rowPos = [N-1]*M # 下次堆石頭的位置 
    for j in range(N-1,-1,-1): # 往東的一輪, 所以 j 從大到小
        for i in range(M):
            if table[i][j] == 'O':
                table[i][j] = '.'
                table[i][rowPos[i]] = 'O' # 新位置放圓石
                rowPos[i] -= 1
            if table[i][j] == '#':
                rowPos[i] = j-1 # 下次會放的格子位置
    # showTable()
    # print(k, part2(table))
    # showTable()

    tableStr = ''.join( [''.join(table[i]) for i in range(M)] )
    if tableStr in history: # key 是地圖盤面字串 tableStr
        prev = history[tableStr][0] # value是 (step k 及「石頭總重」)
        #print(k, '-', prev)
        # k vs. prev 前一次重覆
        # 所以 (k-prev) 便是循環的長度, 再取餘數 就是答案
        MOD = k - prev
        ansK = 1000000000 % MOD
        while ansK<prev: # 若 ansK 還沒進入 prev 後的循環
            # print('ansK', ansK)
            ansK += MOD # 就讓 ansK 照著 MOD 值，持續長大
        break
    history[tableStr] = (k, part2(table))
    # key是地圖盤面字串，value是 (step k 及「石頭總重」)
    
# print('ansK', ansK)
for (key, ans) in history.values(): # value 是 (step k 及「石頭總重」)
    #print(key, ans)
    if key==ansK: # 若找到對應的 key 值 step k，就回傳當初一起送出的 「石頭總重」
        print(ans) # Part 2 我的 Puzzle Input 對應答案 105606

# 我把 1000,000,000 看成了 1000,000 所以這題一直答錯
# cooldown 時間就從 1min, 3min, 5min 10min 一直增加
# 前幾次答錯會提示 too low 或 too high，但後來就不提示，以免有人猜答案


