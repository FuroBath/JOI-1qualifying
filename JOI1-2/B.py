import sys
A,B = map(int,map(str.rstrip, sys.stdin))
print(12) if (X:=((A+B)%12)) == 0 else print(X)
