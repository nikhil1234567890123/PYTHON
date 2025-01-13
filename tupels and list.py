#list
'''marks1 = 94.4
marks2 = 83.5
marks3 = 90.6
marks4 = 57.3
marks5 = 45.5

marks = [94.4, 83.5, 90.6, 57.3, 45.5]
print(type(marks))
print(marks[0])
print(marks[4])'''

'''student = ["nikhil", 90.4, 20, "chandigarh" ]
print (student[0])
student[0]="hitesh"
print(student)'''#list are mutable it can change the values but we can not change in string

#list slicing(list_name[starting_idx : ending_idx])#ending index is not include
'''marks = [56, 58, 89, 52, 70]
print(marks[1:4])'''
#also include negative index
'''marks = [56, 58, 89, 52, 70]
print(marks[-3:-1])'''

#list methods
'''list = [2 ,1 ,3 ]
list.append(4)#adds one element at the end 
print(list)'''

'''[list = [2 ,4 ,3 ,1]
list.append(5)
list.sort()#sort in ascending order 
print(list)'''

'''list = [2, 4, 3, 1]
list.sort(reverse=True) #decending order
print(list)'''

'''list = [2, 4, 3, 1]
list.reverse()#for reverse the list
print(list)'''

'''list = [2, 4, 3, 1]
list.insert(2,5) #insert element at index
print(list)'''

'''list = [2 ,1 ,4 ,3 ,1 ]
list.remove(1)#remove first occurence of element
print(list)'''

'''list = [2 ,1 ,4 ,3 ,1 ]
list.pop(2)#remove element st idx
print(list)'''

#TUPLES IN PYTHON
#A built-in data type that lets us create immutable sequence of values

'''tuple = (2, 1, 5, 4)
print(tuple[0])
print(tuple[1])'''

#slicing in tuple
'''tup = (2 ,1 ,4 ,3 ,1 )
print(tup[1:4])'''

'''tup = (2 ,1 ,4 ,3 ,1 )
print(tup.index(4))#return index of first occurrence'''

'''tup = (2 ,1 ,4 ,3 ,1)
print(tup.count(3))#count total occurrence'''

#wap to ask the user to enter names of there 3 favorite movies & store them in a list
'''movies = []
a = input("Enter your first favorite movie:")
b = input("Enter your second favorite movie:")
c = input("Enter your third favorite movie:")

movies.append(a)
movies.append(b)
movies.append(c)
print(movies)'''

#wap to check if a list contains a palindroe(samne se or pecha se same) of elements.(hint:use copy() method)
#12321, 1,"abc", "abc",1]
'''list1 = [1, 2, 1]
list2 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list2 = list2.copy()
reverce_list1 = list1.reverse()
reverse_list2 = list2.reverse()

if(copy_list1 == list1):
    print("palandrome")
else:
    print("NOT palandrome")

if(copy_list2 == list2):
    print("palandrome")
else:
    print("NOT palandrome")'''

#wap to count the number of student with the "A"grade in the following tuple
'''tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))'''

#store the above values in a list & sort them form "A" to "D"
'''grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
'''
#store the ABOVE NUMBERS IN LIST & SORT THEM FROM 1 to 10 
numb= (1, 4, 5, 3, 6, 9, 8, 2)
numb.sort()
print(numb)