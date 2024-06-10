# Maximum appearing element in ranges

def maxAppearingElem(left,right):
  freq=[0]*101
  for i in range(len(left)):
    freq[left[i]] +=1
    freq[right[i]+1] -=1
  maxElem=-123
  for i in range(1,100):
    freq[i] +=freq[i-1]
  return freq.index(max(freq))

left=[1,2,4]
right=[4,5,7]
print(maxAppearingElem(left,right))