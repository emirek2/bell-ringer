def check_3Digits(list1):
  # return number in range(100, 1000)
  three_digit_list=[]
  for i in list1:
    if i in range(100,1000):
      three_digit_list.append(i)
      # return True
    else:
      pass
  return three_digit_list



  # pass
  
########################################################################################################################
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.
def all_positives(list2):
  
  for i in list2:
    if i <=0:
      return False
    else:
      pass
  return True
# Don't call the function, you just need to define it.


########################################################################################################################
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list (stored in the variable numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.
def sum_less(list3):
  total=0
  for i in list3:
    total+=i

  return total


########################################################################################################################
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_even(list4):
  count=0
  for i in list4:
    if i % 2==0:
      count+=1
    else:
      pass
  return count