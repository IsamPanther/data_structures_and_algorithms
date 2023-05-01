#def for converting integer to roman numerals...
def int_to_roman(n):

#this list of integer 
  numbers=[1,4,5,9,10,40,50,90,100,400,500,900,1000]

#this is list of roman symbol in reference from the list of integer
  roman=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]

#Here i=12 means the total count of element per each list in index count...
  i=12

  roman_numerals=" "


#This is loop that check if entered argument is satisfied in iteration or not..
  while n!=0:

    if numbers[i]<=n:

      roman_numerals+=roman[i]

      n=n-numbers[i]

    else:

      i=i-1
#here is the return point for execution of function if all condition in a loop satisfied
  return roman_numerals

#user button...
user=int(input("enter number:"))

#calling statement of def with an argument from user
if __name__=="__main__":
  print(int_to_roman(user))

      
   










        
