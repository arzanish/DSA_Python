# Rotate array by d places
def reverse(ls,a,b):
  s=a
  e=b
  while s<e:
    ls[s],ls[e]=ls[e],ls[s]
    s=s+1
    e=e-1
def rotateByD(ls,d):
  reverse(ls,0,d-1)
  reverse(ls,d,len(ls)-1)
  reverse(ls,0,len(ls)-1)

ls=[1,2,3,4,5]
rotateByD(ls,2)
print(ls)
