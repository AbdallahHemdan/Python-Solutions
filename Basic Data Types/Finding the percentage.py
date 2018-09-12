if __name__ == '__main__':
    n = int(input())
    l= {}
    for i in range(n) : 
        t = input().split()
        l[(t[0])]= (float(t[1])+float(t[2])+float(t[3]))/3 
        
        
    name = input()
    print("%.2f" % round(l[name],2))
