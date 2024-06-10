# Prefix Sum
arr=      [2,8,3,9,6,5,4]
          [2,10.13,32,38,43,47]
i*arr[i]  [2,20,39,128,190,329]
n=len(arr)
preSum=n*[None]
preSum[0]=arr[0]
for i in range(1,n):
  preSum[i]=preSum[i-1]+arr[i]
def getSum(l,r):
  if l==0:
    return preSum[r]
  else:
    return preSum[r]-preSum[l-1]

print(getSum(0,2))
print(getSum(1,3))
print(getSum(2,6))