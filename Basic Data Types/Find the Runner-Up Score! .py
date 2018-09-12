if __name__ == '__main__':
    n = int(input())
    arr = map (int,input().strip().split())
    print (sorted(list(set(arr)))[-2])
