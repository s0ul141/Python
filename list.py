'''Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output.'''

print ("a list of number separated by commas")
nums = input().split(',')
max_num = int(nums[0])
for i in nums:
    i = int(i)
    if i > max_num:
        max_num = i
        
print("the max number is",+max_num)
#sorting the list that is given by the user in reverse order / descending order 
print(sorted(nums, reverse=True))


