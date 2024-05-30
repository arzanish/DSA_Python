# Second Largest element in list

def secondLargest(ls):
  if not ls:
    return None
  else:
    lg=ls[0]
    slg=-1111111
    for i in range(1,len(ls)):
      if lg<ls[i]:
        slg=ls
        lg=ls[i]
      elif lg>ls[i]:
        if ls[i]>slg or slg is None:
          slg=ls[i]
    return slg
# l=[1000,6,5,3,9,8,10,2,65,22,324]
l=[2,2,2,2,3]
print(secondLargest(l))
