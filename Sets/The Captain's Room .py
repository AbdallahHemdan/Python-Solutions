k = int(input())
s1 = list(map(int,input().split()))
s2 = set(s1)
print(int((sum(s2)*k-sum(s1))/(k-1)))
