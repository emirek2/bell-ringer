from dynamic_functions import check_3Digits, all_positives, sum_less, count_even




coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

#retrieve the names and price from the above tuple
for coffee, price in coffee_prices:
  print(f"The {coffee} costs ${price}")

#create a function for retriving the highest price coffe and its name
def most_expensive(coffee_prices):
  highest_prices=0
  my_most_expensive=''
  for coffe, price in coffee_prices:
    if price>highest_prices:
      highest_prices = price
      my_most_expensive = coffee
    else:
      pass
  return(my_most_expensive, highest_prices)
print(most_expensive(coffee_prices))

result=check_3Digits([55,99,600,780,48,120,65,666,37,17,975,17175145])
print(result)
end=all_positives([2,3,4,5,-1,5,57,-123])
print(end)
sum=sum_less([23,2,2,2,1,1,14,4,14,123,235])
print(sum)
counts=count_even([3,3,3,3,3,5,5,2,6,3,4,5,])
print(counts)
  
  




    
    # if p[1]>p[2] and p [3]:
    #   print(f'The {c[1]} is the highest price')
    # elif p[2]>p[3] and p [1]:
    #   print(f'The {c[2]} is the highest price')
    # elif p[3]>p[1] and p [2]:
    #   print(f'The {c[3]} is the highest price')