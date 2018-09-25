n1 = int(input())
s1 = set(map(int,input().split()))
n2 = int(input())
s2 = set(map(int,input().split()))
lis = list(s1.symmetric_difference(s2))
lis.sort()
for i in lis : 
    print(i)
