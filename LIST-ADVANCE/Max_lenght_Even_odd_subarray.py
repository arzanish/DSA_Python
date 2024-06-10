# Maximum length of EVEN ODD subarray

def maxEvenOdd(ls,n):
  curr=1
  res=1
  for i in range(1,n):
    if(ls[i]%2==0 and ls[i-1]%2!=0) or (ls[i]%2!=0 and ls[i-1]%2==0):
      curr=curr+1
      res=max(res,curr)
    else:
      curr=1
  return res

# ls=[10,12,14,7,8]
ls=[7,4,5,6]
print(maxEvenOdd(ls,len(ls)))