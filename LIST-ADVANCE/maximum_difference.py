# Maximum difference
# find the maximum of arr[j]-arr[i] , where j>i

def maxdiff(arr,n):
  res=arr[1]-arr[0]
  minval=arr[0]
  for j in range(1,n):
    res=max(res,arr[j]-minval)
    minval=min(minval,arr[j])
  return res
arr=[2,3,10,6,4,8,1]
print(maxdiff(arr,len(arr)))