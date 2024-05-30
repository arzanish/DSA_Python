# Reverse a List
def reverseList(ls):
  return ls[::-1]

def reverseList_ownMethod(ls):
  s=0
  e=len(ls)-1
  while s<e:
    ls[s],ls[e]=ls[e],ls[s]
    s=s+1
    e=e-1
  return ls

ls=[1,2,3,4,5]

print("3 ",reverseList(ls))
print("4 ",reverseList_ownMethod(ls))