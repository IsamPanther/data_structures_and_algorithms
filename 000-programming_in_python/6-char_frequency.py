#def that accept string into dictionary....
def character_frequency(string):

  dict={}

  for i in string:

    if i in dict:

      dict[i]+=1

    else:

      dict[i]=1

  return dict   

#user button that accept string entered by user
user=input("enter string:")  

#calling def with an argument from user button..
if __name__=="__main__":
  print(character_frequency(user))

