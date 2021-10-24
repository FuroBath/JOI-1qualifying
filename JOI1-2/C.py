input()
S = list(input())
[print(S[i-1]) for i,n in enumerate(S) if n == 'J' and i > 0]
