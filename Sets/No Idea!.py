t = list(map(int,input().split()))
n = t[0]
m = t[1]
Happy = 0 
lis = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
for i in lis : 
    if i in A : 
        Happy+=1 
    elif i in B : 
        Happy-=1 
print(Happy)
