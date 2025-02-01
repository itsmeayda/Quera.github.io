def henduneKharboze(lst) :
    h1 = lst[0] * 2
    k1 = lst[1] * 1
    total = h1 + k1
    if lst[0] % 2 == 0 and lst[1] % 2 == 0 :
        if total % 2 == 0 :
            print("YES")
        else :
            print("NO")
        

lst = []
h = int(input())
k = int(input())
lst.append(h)
lst.append(k)
henduneKharboze(lst)