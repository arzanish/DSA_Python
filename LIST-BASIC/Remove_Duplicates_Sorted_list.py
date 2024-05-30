# Remove duplicates in a sorted list
def removeDuplicates(ls):
  res=1
  for i in range(1,len(ls)):
    if (ls[res-1]!=ls[i]):
      ls[res]=ls[i]
      res=res+1
ls=[10,20,20,30,40,40,50]
removeDuplicates(ls)
print(ls)
