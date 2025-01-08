#dictionary in python(key:value)
'''info = {
    "key" : "value",
    "name" : "nikhil",
    "learning" : "coding",
    "age" : 20,
    "is_adult" : True,
    "marks" : 94.4,
    "subject" : ["python", "c", "java"]
}
null_dictionary = {}
info["learning"] ="pyhon" # update value
info["surname"] = "kaundal"# add new key : value
print(info)
print(null_dictionary)'''

#nested dictionary
'''student = {
    "name" : "nikhil",
    "class" : "cse",
    "score" : {
        "chem" : 98,
        "phy" : 99,   
        "math" : 98
    }
}
print(student["score"]["chem"])'''

#dictionary methods
'''student = {
    "name" : "nikhil",
    "class" : "cse",
    "score" : {
        "chem" : 98,
        "phy" : 99,
        "math" : 98
    }
}
print(list(student.keys())) # return all the keys
print(student.values())#retuern all the vlaues
print(student.items())#return all (key, val) pairs as tuple
print(student.get("name"))#return the key according to value
student.update({"city":"chandigarh", "age" : "21"})#insert the specific iten to the dictionarey
print(student)'''

#set in python: set is the collection of the unordered items. each elements in the set must be unique & immuatable.
'''collection = {1, 2, 2, 4, "hello", "world", "world"}
empty_set = set()#empty set

print(collection)
print(type(collection))
print(len(collection))
'''
#set method
'''collection = {1, 2, 2, 4, "hello", "world", "world"}
collection.add(5)#add an element
collection.remove(2)#remove the element
collection.clear()#empties the set
collection.pop()#remove a randome value
print(collection)'''
#UNION : combines both set value & return new
'''set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))'''
#INTERSECTION : combine common values & return new
'''set1 = {1, 2, 3, 4, 5}
set2 = {2, 8, 9, 4, 5}
print(set1.intersection(set2))'''

#store following word meaning in a python dictionary:
'''dictionary = {
    "table" : ["a pice of furniture", "list of facts & figures"], 
    "cat" : "a small animal"
}
print (dictionary)'''

#you are givena list of subjects for students. assume one classroom is required for 1 subject. how many classroom are needed by all the students.
'''subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print(len(subject))'''

#wap to enter marks of 3 students from the user and store them in a dictionary. start with an empty direction & add one by one. use subject name as key & marks as value.
'''score = {}
score["math"] = int(input("Enter your math Marks:"))
score["chem"] = int(input("Enter your chem Marks:"))
score["phy"] = int(input("Enter your phy Marks:"))
print(score)'''

'''marks = {}

x = int(input("enter phy:"))
marks.update({"phy" : x})

x = int(input("enter math:"))
marks.update({"math" : x})

x = int(input("enter chem:"))
marks.update({"chem" : x})

print(marks)'''

#figure out a way to store 9 & 9.0 as separate values in the set (you can take help of built-in data type)
'''value = {9, "9.0"}
print(value)'''

values = {

    ("float",9.0),
    ("int", 9)
}
print(values)