#def that accept list of an integer  and integer target,returns indices of two numbers...
def two_indices(nums,target):

#check that the list is not empty..  
  if not nums:

    return None

  else:  

    for i in range (len(nums)):

      for j in range (i+1,len(nums)):

        if nums[i] + nums[j] == target:

          
          return i,j

#calling of def with an argument of list of [1,3,8,10,2] and target number of 11
if __name__=="__main__":
  print(two_indices([1,3,8,10,2],11))        