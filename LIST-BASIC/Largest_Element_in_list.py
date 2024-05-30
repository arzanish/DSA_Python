# find the largest element in list

def getMax(l):
  if not l:
    return None
  else:
    res=l[0]
    for i in range(1,len(l)):
      if res<l[i]:
        res=l[i]
    return res

l=[1000,6,5,3,9,8,10,2,65,22,324]
print(getMax(l))