#loops in python : loops are use to repeate instruction 
#WHILE loops
'''count = 1 # iterator
while count<=5 :
    print("hello")
    count = count + 1 #count+=1
print(count)'''

'''i = 1
while i <= 10000:
    print("nikhil", i)
    i+=1'''
    
#print numbers form 1 to 5 
'''i = 5
while i>=6:
    print(i)
    i-=1'''

#print numbers form 1 to 100.
'''i = 1
while i<=100:
    print(i)
    i+=1'''

#print numbers form 100 to 1 
'''i = 100
while i>=1:
    print(i)
    i-=1'''

#print the multiplication table of a number n 
'''n = int(input("enter your number : "))
i = 1
while i<=10:
    print(n*i)
    i+=1'''

#print the elements of the following list using a loop:
'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#traverse
idx = 0
while idx< len(nums):
    print(nums[idx])
    idx+=1'''

#search for a number x in this tuple using loop:
'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36
i=0
while i<len(nums):
    if(nums[i] == x):
        print("found at idx", i)
    i+=1'''

#break : used to terminate the loop when encountered
'''i = 1
while i <= 5:
    print(i)
    if(i==3):
        break#stop
    i+=1

print("end of loop")
'''
#continue: terminated execution in the current interation & continues execution of the loop with the next iteration
'''i = 0
while i<=10:
    if(i%2!=0):
        i += 1
        continue#skip
    print(i)
    i+=1'''

#FOR LOOP: it is use for sequential travesal. for traversing list, string, tuples etc.
"""list = [1, 2, 3]
for el in list:
    print(el)"""

#nums = [1, 2, 3, 4, 5]
'''nums = ["nikhil", "hitesh", "shreya", "harshit"]
for val in nums:
    print(val)'''

'''tup = (1, 2, 3, 4, 4, 5, 6)
for num in tup:
    print(num)'''

'''str = "NIKHIL"
for name in str:
    print(name)
else:#else ki hume vahan jarurt padti hai jahan hum break ka use krte han 
    print("END")'''

'''str = "NIKHIL"
for name in str:
    if (name == "H"):
        print("H Found")
        break
    print(name)
else:
    print("END")'''

#print the elements of the following list using a loop:
'''list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for numb in list:
    print(numb)'''

#search for a number X in this tuple using loop:

'''tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = int(input("ENTER THE VALUE OF X : "))
idx = 0
for num in tup:
    if (num == x):
        #print(x, "is found")
        print("number found at idx", idx)
    idx +=1
        #break
    #print(num)
else:
   print("VALUE OF X IS NOT FOUND")'''

#RANGE : range function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before specified number.
'''eq =  range(11)
for i in seq:
    print(i)'''
'''for i in range(10): range(stop) | mostly we use this 
    print(i)'''
#range(start?, stop, step?)
'''for i in range(2,10): #range(start, stop)
    print(i)'''

#range(start, stop, step)
'''for i in range(2, 10, 3):
    print(i)'''
for i in range(2, 100, 2):
    print(i)
