def maxSumSubArray(ls):
  n=len(ls)
  res=ls[0]
  maxEnding=ls[0]
  for i in range(1,n):
    maxEnding=max(ls[i],maxEnding+ls[i])
    res=max(res,maxEnding)
  return res

ls=[-5,1,-2,3,-1,2,-2]
print(maxSumSubArray(ls))
