# Return a boolean value if you found a subarray with the given sum
def isSubSum(arr,sum,n):
  curr=0
  s=0
  for e in range(n):
    curr=curr+arr[e]
    while curr>sum:
      curr -=arr[s]
      s=s+1
    if curr==sum:
      return True
  return False
arr=[1,4,20,3,10,5]
sum=33
print(isSubSum(arr,sum,len(arr)))