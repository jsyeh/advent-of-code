import sys
lines = sys.stdin.readlines()
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ans = 0
for line in lines:
	first, last = -1, -1
	pos1, pos2 = -1, -1
	for i,c in enumerate(line):
		if c.isdigit():
			if first==-1:
				first = int(c)
				pos1 = i
			last = int(c)
			pos2 = i
	# print(pos1, pos2)
	# print(first, last)
	for i,d in enumerate(digits):
		w1, w2 = line.find(d), line.rfind(d)
		if w1!=-1 and w1<pos1:
			pos1 = w1
			first = i+1
		if w2!=-1 and w2>pos2:
			pos2 = w2
			last = i+1
	# print(first, last)
	ans += first*10 + last
print(ans) # 54518
