# Stock buy and sell

def maxProfit(price):
  profit=0
  for i in range(1,len(price)):
    if price[i]>price[i-1]:
      profit=profit+ (price[i]-price[i-1])
  return profit

price=[1,5,3,8,12]

print(maxProfit(price))