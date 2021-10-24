import sys
a,b,c = map(int,map(str.rstrip, sys.stdin))
print(1) if a+b <= c else print(0)
