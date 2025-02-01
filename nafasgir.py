def nafasgir(lst1,lst2) :
    res = []
    for i in range(n):
        res.append(lst1[i]*lst2[i])
    return sum(res)
        
n = int(input())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
print(nafasgir(lst1, lst2))