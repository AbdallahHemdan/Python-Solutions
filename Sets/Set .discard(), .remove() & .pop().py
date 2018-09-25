n = int(input())
st =set(map(int,input().split()))
for i in range(int(input())) : 
    t = input().split()
    if t[0]=="pop" : 
        st.pop()
    elif t[0]=="remove" : 
        st.remove(int(t[1]))
    elif t[0]=="discard" : 
        st.discard(int(t[1])) 
print(sum(st))
