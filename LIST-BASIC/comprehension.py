# Comprehension in python
even=[x for x in range(11) if x%2==0]
print(even)

odd=[x for x in range(11) if x%2!=0]
print(odd)

#function
def getSmaller(ls,x):
  return [e for e in ls if e<x]
ls=[9,15,12,3,7,11]
x=10

print(getSmaller(ls,x))

#SET Comprehension
ls=[10,20,35,6,33,42,56,656,99]
s1={x for x in ls if x%2==0}
print(s1)

#DICTIONARY Comprehension
ls=[1,3,4,2,5]
d1={x:x**3 for x in ls}
d2={x:f"ID{x}" for x in range(4)}
print(d1)
print(d2)
