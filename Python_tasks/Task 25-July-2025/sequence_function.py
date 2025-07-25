# filter
marks = [70,89,79,98,56,86,89]
passed = list(filter(lambda x: x>85,marks))
print(passed)


#map
price_usd = [10,20,30]
price_inr = list(map(lambda x:x*85.5,price_usd))
print(price_inr)

#reduce
from functools import reduce
cart_item = [100,200,300,600]
total = reduce(lambda x,y: x+y, cart_item)
print(total)

#zip
a = ["apple","banana","carrot"]
b = [1,2,3]
zipped_c = list(zip(a,b))
print(zipped_c)

#enumerate
questions = ["who r u","whats ur name"]
for i,q in enumerate(questions,start = 1):
  print(f"{i}:{q}")


#sorted
student = [("alice",90),("ben",70),("charlie",80)]
sort_stu = sorted(student,key= lambda x:x[0],reverse = True)
print(sort_stu)


#any
#all
access_right = [True,False,True]
print(any(access_right))# true
print(all(access_right))# false



#reversed
names = ["Alan","Baggey","Chara"]
print(list(reversed(names)))
