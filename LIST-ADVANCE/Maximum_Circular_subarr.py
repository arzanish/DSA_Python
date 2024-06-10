# Maximum Circular Subarray - Kadane's Algorithm
def maxSum(arr,n):
  res=arr[0]
  maximum=arr[0]
  for i in range(1,n):
    maximum=max(arr[i],arr[i]+maximum)
    res=max(maximum,res)
  return res

def maxCircularSum(arr,n):
  max_sum=maxSum(arr,n)
  sum=0
  for i in range(n):
    sum=sum+arr[i]
    arr[i]=-arr[i]
  inverted_maxSum=maxSum(arr,n)
  res=max(max_sum,sum+inverted_maxSum)
  return res
arr=[8,-4,3,-5,4]
# arr=[-5,1,-2,3,-1,2,-2]
print(maxCircularSum(arr,len(arr)))