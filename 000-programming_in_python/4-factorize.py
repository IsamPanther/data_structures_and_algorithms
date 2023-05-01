#def that factorize input number into its prime factor
def factorize(number):

  for i in range (1,number+1):

    if(number%i==0):

      count=0

      for j in range (1,i+1):

        if (i%j==0):

          count=count+1

      if(count==2):

        print(i,end=" ")    

  
#user button that allow user to input number for factorization in program
user=int(input("enter number:"))

#calling statement of def that accept an argument from user button for factorization..
if __name__=="__main__":
    print(factorize(user))

