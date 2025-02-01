def prime(a):
    lst = []
    if a == 1 :
        print(f'{a+1}')
    for i in range(2,a*a) :
        if i > 2 and i %2 == 0 :
            continue
        c = 0 
        for j in range(1, i+1):
            if i % j == 0 :
                c +=1
        if c == 2 :
                lst.append(i)
    #print(lst)
    x = 0
    for i in lst :
         x +=1 
         if x == a :
             print(i)      
a = int(input('enter the number :'))
prime(a)
