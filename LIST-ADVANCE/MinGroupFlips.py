# Minimum Group flips to make the array same

def minFlips(arr,n):
  for i in range(1,n):
    if arr[i]!=arr[i-1]:
      if arr[i]!=arr[0]:
        print(f"From {i} to ")
      else:
        print(i-1)
  if arr[n-1]!=arr[0]:
    print(n-1)

arr=[0,0,1,1,0,0,1,1,0,1]
minFlips(arr,len(arr))


