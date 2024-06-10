# Find the Equilibrium Point in array
# TIME COMPLEXITY O(n)
# SPACE COMPLEXITY O(1)

# def equilibrium(arr,n):
#   preSum=[None]*n
#   preSum[0]=arr[0]
#   postSum=[None]*n
#   postSum[n-1]=arr[n-1]
#   for i in range(1,n):
#     preSum[i]=arr[i]+preSum[i-1]
#   for i in range(n-2,-1,-1):
#     postSum[i]=arr[i]+postSum[i+1]
#   for i in range(n):
#     if preSum[i]==postSum[i]:
#       print(f"Equilibrium point at index : {i} with value : {arr[i]}")
#       return 0
#   print("No equilibrium")

def equilibrium(arr,n):
  preSum=0
  postSum=0
  for i in range(n):
    postSum+=arr[i]
  for i in range(n):
    postSum -=arr[i]
    if preSum==postSum:
      print(f"Equilibrium point at index : {i} with value : {arr[i]}")
      return True
    preSum +=arr[i]
  print("No equilibrium")
  return False




arr=[3,4,8,-9,20,6]
# arr=[4,2,-2]
equilibrium(arr,len(arr))