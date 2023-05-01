#def that search for the first occurrence of an integer...
def find_first_occurrence(my_list,num):

#loop for iterating elements in my_list
  for i in range (len(my_list)):

    if my_list[i] == num:

#Here return value for elements in my_list when iterating
      return i

#return statement if the elements in list is not exist....
  return -1   

#calling statement with an argument of [6,7,9,3,1] and the searching element is 9
if __name__=="__main__":
  print(find_first_occurrence([6,7,9,3,1],1))

