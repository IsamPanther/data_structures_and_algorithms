#def that return the smallest integer from the list...
def get_smallest_integer(my_list):

#smallest count from index 0
  smallest_num = my_list[0]

#iterating index of each element in list
  for i in my_list:

    if i < smallest_num:

      smallest_num = i

#return value of def..
  return smallest_num 

#calling statement with an argument of [2,7,200,1,3]
if __name__=="__main__":
  print(get_smallest_integer([2,7,200,1,3]))
