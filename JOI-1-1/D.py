input()
A = input().split()
B = input().split()

B = list(set(B))
C = [A.count(n) for n in B]
print(sum(C))
