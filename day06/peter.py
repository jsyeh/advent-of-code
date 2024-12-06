lines=[]

while True:
    try: lines.append(input())
    except: break
M,N=len(lines),len(lines[0])
for i in range(M):
    for j in range(N):
        if lines[i][j]=='^':
            startI,startJ=i,j
            guardI,guardJ=i,j

dI=[0,1,0,-1]
dJ=[1,0,-1,0]
d=3
grid=[[0]*N for i in range(M)]
grid[guardI][guardJ]=1

while True:
    ii,jj=guardI+dI[d],guardJ+dJ[d]
    if ii<0 or jj<0 or ii>=M or jj>=N:
        break
    if lines[ii][jj]=='#':
        d=(d+1)%4
        continue
    guardI,guardJ=ii,jj
    grid[ii][jj]=1
ans=0
for i in range(M):
    for j in range(N):
        if grid[i][j]==1: ans+=1
print(ans)

print("====part 2====")

def helper():
    grid=[[[] for j in range(N)] for i in range(M) ]
    d=3
    guardI,guardJ=startI,startJ
    while True:
        ii,jj=guardI+dI[d],guardJ+dJ[d]
        if ii<0 or jj<0 or ii>=M or jj>=N: return 0
        if lines[ii][jj]=='#':
            d=(d+1)%4
            continue
        if d in grid[ii][jj]: return 1
        grid[ii][jj].append(d)
        guardI,guardJ=ii,jj
lines=[[lines[i][j] for j in range(N)] for i in range(M)]
ans=0
for i in range(M):
    for j in range(N):
        if lines[i][j]!='.': continue
        lines[i][j]='#'
        ans+=helper()
        lines[i][j]='.'
print(ans)


