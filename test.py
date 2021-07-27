#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

nums = [-1,2,1,-4]
sumList  = []
anchor1 = []
tempSum1 = 0
tempSum2 = 0
nums.sort()
target = 1
print(nums)
#itterate and store the value in another list
for i in range(1,len(nums)):
    anchor = nums[i-1]+nums[i]
    
    for j in range(i, len(nums)-1):
        print(j," ", nums[j], " ", anchor)
        tempSum1 = anchor + nums[j]
        sumList.append(tempSum1)
        
print(anchor1)
print(sumList)
        

#sorting the list


#compare the value 
for i in range (1,len(sumList)):
    tempVal = sumList[i-1]
    if (tempVal < sumList[i]):
        tempVal = sumList[i]
#return the number    
    else:
        print(tempVal)


