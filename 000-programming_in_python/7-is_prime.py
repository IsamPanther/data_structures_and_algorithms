 #def that check whether an integer is  prime or not....
def is_prime(number):

  if number==0 and number==1:

    return 
    
  elif number>1:

    for i in range(2,number):

      if (number%i==0):

        return False

    else:
      
      return True

  else:

    return False      

#user button
user=int(input("enter number:"))

#calling of def wit an argument
if __name__=="__main__":
  print(is_prime(user))