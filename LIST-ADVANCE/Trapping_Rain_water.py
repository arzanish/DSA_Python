# Trapping Rain Water
def trapRainWater(ls,n):
  res=0
  lmax=[0]*n
  rmax=[0]*n

  lmax[0]=ls[0]
  rmax[n-1]=ls[n-1]

  for i in range(1,n):
    lmax[i]=max(ls[i],lmax[i-1])
  for i in range(n-2,-1,-1):
    rmax[i]=max(ls[i],rmax[i+1])

  for i in range(1,n-1):
    res=res+(min(lmax[i],rmax[i])-ls[i])

  return res


ls=[5,0,6,2,3]
print(trapRainWater(ls,len(ls)))
# lm=[5,5,6,6,6]
# rm=[6,6,6,3,3]
