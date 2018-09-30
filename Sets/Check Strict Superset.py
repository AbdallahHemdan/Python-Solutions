s1 = set(map(int,input().split()))
t = int(input())
flag = True
for i in range(t) : 
    temp = set(map(int,input().split())) 
    if (not temp.issubset(s1)or len(temp)>=len(s1)):
        flag = False
        break
if flag : 
    print(True)
else :
    print(False)
    
        
