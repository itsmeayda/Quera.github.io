def names(lst) :
   lens = []
   for i in lst :
       new_set = set(i)
       lens.append(len(new_set))
   print(max(lens))
       
   
lst = []
n = int(input())
for i in range(n) :
    name = input()
    lst.append(name)
#print(lst)
names(lst)