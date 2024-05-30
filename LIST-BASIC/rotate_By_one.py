# Rotate Array by one
def rotateByOne(ls):
  if len(ls)==1:
    return ls
  return ls[1:] + ls[0:1]

ls=[1,2,3,4]

print(rotateByOne(ls))