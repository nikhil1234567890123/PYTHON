# str1 ="this is string."
# str2 ='nikhil'
# str3 ="""this is string"""
'''str1 ="this is string.\nwe are creating it in python" #escape sequence character
print(str1)'''
#concatination ("hello"+ "world"-> "helloworld")
'''str1 = "nikhil"
str2 = "kaundal"
print(str1+str2)'''
#length of str
'''str1 = "nikhil"
len1 = len(str1)
print(len1)

str2 = "kaundal"
len2 = len(str2)
print(len2)

final_str = str1 +" "+ str2
print(final_str)
print(len(final_str))'''
#indexing
'''str1 = "nikhil kaundal"
ch = str1[0]
print(ch)'''
#slicing(Accessing parts of a string)
'''str1 ="nikhilkaundal"
ch = str1[6:len(str1)]
print(ch)'''
#negative index
'''str = "apple"
ch = str[-4:-1]
print(ch)'''
# string function
'''str = "i am studing fron UIET"
print(str.endswith("IET"))'''#TRUE (RETURN TRUE IF STRING ENDS WITH SUBSTR)
'''str = "i am studing from UIET"
print(str.capitalize())'''#ye first leter ko capital kr deta hai
'''str = "i am studing from UIET"
print(str.replace("UIET","apana collage"))'''#ye replace kr deta hai 
'''str = "i am from india"
print(str.find("o"))'''# find the index of character
'''str = "i am from india"
print(str.count("i"))'''# count the no. of chartacter 
#WAP to input user's first name & print its length 
'''a = input("Enter your name:")
print(a, "\nand the lenght of your name is:",len(a))'''
#WAP to find the occurrence of '$' in a string.
'''str = "hi, $i am the $ symbol $99.99"
print(str.count("$"))'''
#condition statement if-elif-else
'''light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")'''
'''num = 5
if(num>2):
    print("greater then 2")
elif(num>3):
    print("greater then 3") '''

'''light = "pink"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")'''

'''age = 14
if(age>=18):
    print ("can vote")
else:
     print("can't vote")'''
 
'''marks = int(input("Enter Marks:"))
if(marks>=90):
   grade = "A"
elif(marks>= 80 and marks < 90):
   grade="B"
elif(marks>=70 and marks < 80):
   grade="C"
else:
   grade="D"
print("grade of the student:",grade)'''
#nested 
'''age=90
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")'''

#WAP to check if a number entered by the user is odd or even 
'''num=int(input("Enter your number:"))
rem = num % 2
if(rem == 0):
    print(" number is even")
else:
    print("odd")'''
#WAP to find the greatest of 4 numbers entered by the user
'''a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number:"))
d = int(input("Enter your fourth number:"))

if(a>=b and a>=c and a>=d):
    print("first number is largest",a)
elif(b>=a and b>=c and b>=d):
    print("second number is largest",b)
elif(c>=a and c>=b and c>=d):
    print("fourth number is largest",c)
else:
    print("third number is the largest",d)'''

a = int(input("enter your number:"))

if (a%7 == 0):
    print(a, "is a multiple of 7")
else:
    print(a,"is not a multiple of 7")
