# Find the maximum sum of K consecutive elements
# SLILDING WINDOW TECHNIQUE

def kMax(arr,k,n):
  sum_k=0
  for i in range(k):
    sum_k=sum_k+arr[i]
  maxSum=sum_k
  for i in range(k,n):
    sum_k=sum_k+arr[i]-arr[i-k]
    maxSum=max(maxSum,sum_k)
  return maxSum

# arr=[1,8,30,-5,20,7]
# k=3

arr=[5,-10,6,90,3]
k=2
print(kMax(arr,k,len(arr)))

