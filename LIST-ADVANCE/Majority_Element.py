# Majority Element
# Moore's Voting Algorithm

# Idea: A MAJORITY element is an element that occurs more than n/2 times in an array , where n is the length of the array

def findMajority(arr,n):
  # This is the 1st half of the algorithm where we find a potential MAJORITY ELEMENT
  res=0 # this variable will contain the position of the potential MAJORITY element
  count=1 # We set count as 1
  for i in range(1,n):
    if arr[i]==arr[res]:
      count=count+1
    else:
      count=count-1
    if count==0:
      # Here if the count=0 we consider the current element as a potential MAJORITY and reset the count to 1 and start the next iteration
      res=i
      count=1

  # This is the other half of the element , where we confirm if the element we chose is an actual MAJORITY element or not.
  count=0
  for i in range(n):
    if arr[res]==arr[i]:
      count +=1
  if count <= n//2:
    res=-1
  return res

# arr=[8,3,4,8,8]
arr = [3,7,4,7,7,5]
print(findMajority(arr,len(arr)))
