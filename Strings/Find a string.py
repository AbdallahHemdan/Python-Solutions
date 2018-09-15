def count_substring(s1, s2):
    c=0
    for i in range(len(s1)-len(s2)+1):
        if s1[i:i+len(s2)]==s2:
            c+=1
    return(c)         
