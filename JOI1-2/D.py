import collections
input()
S = list(map(int,input().split()))
S.sort(reverse=True)
c = collections.Counter(S)
print(c.most_common()[-1][0])
