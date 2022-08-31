def addingSum(n):
#Initializing sum with 0
sum = 0

#Loop to calculate up to n and add
for row in range(n):
    sum = sum + (1 << row)

return sum    

n = 8
print("Sum of all elements:", addingSum(n))