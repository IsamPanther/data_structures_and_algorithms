#def for printing right triangle..
def print_right_triangle(height):

  for i in range(height):

    for j in range(i+1):

      print("*",end=" ")

    print("\n")  

#user button for the height of right triangle..
user=int(input("enter height:"))

#calling of def with an argument from user button..
if __name__=="__main__":
  print(print_right_triangle(user))