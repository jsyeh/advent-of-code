import sys
lines = sys.stdin.readlines()
ans = 0
for line in lines:
	first, last = -1, -1
	for c in line:
		if c.isdigit():
			if first==-1: first = int(c)
			last = int(c)
	ans += first*10 + last
print(ans) # 54331
