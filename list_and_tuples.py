#arrays => tuples and list
#tuples are immutable (unchangeable)
#list are mutable (changeable)
#tuples are faster than list


from shutil import copy


import copy


marks = [56,25,10, 90]
print(marks)
print(len(marks))

#different data types aik sth aik hi list mai store kr skte hain

str = "hello"
print(str[0])
# str[0] ="H" #string immutable hai isliye change nhi kr skte tu error ajaega

student = ["Humaira", 20, 90, "Karachi"]
print(student[0])
student[0] = "Huma" #list mutable hai isliye change kr skte tu error nhi ajaega
print(student)

#sublist => slicing of list

marks = [85,95, 89, 100]
print(marks[:3]) #0 se 2 tk print kr dega 3 tk nhi kyu k 3rd index tk print krna hai tu 2 tk print kr dega
print(marks[1:3]) #1 se 2 tk print kr dega
print(marks[-3:-1]) #last se 3rd se last tk print kr dega

#list methods: srf list pe implement hote hain ye

list = [50,100,10,90,5]
#append => list ke end mai element add krta hai
list.append(75)
print(list)


#sorting -> desc/ asc 

print(list.sort()) #ascending order  => returns None kyu kyu k list ko change krta hai tu None return krta hai. Original list ko change krta hai tu None return krta hai
print(list)
print(list.append(80))
print(list)


#desc mai krne k liye hm sort krne k baad reverse kr skte hain
print(list.sort(reverse= True))
print(list)

#srf numbers pe nahi strings pe bhi kr skte hain sort acc to alphabetical order

list = ["banana", "apple", "grapes", "orange"]
print(list.sort())
print(list)

# print(list.reverse())
# print(list)

#reverse => list ko reverse order mai krta hai
print(list.reverse())
print(list)

#insert => kisi specific index pr element add krta hai
list.insert(1, "mango") #index 1 pr mango add kr dega
print(list)

#remove => specific element ko remove krta hai
list.remove("grapes")
print(list)

list.pop() #last element ko remove krta hai
print(list)



#tuples => immutable (unchangeable) string bhi immutable hai tuples bhi immutable hain tu change nhi kr skte tu error ajaega

#tuples are faster than list

# tuples = (56,25,"Humaira", 90)
# print(tuples)
# print(type(tuples[0]))
# print(type(tuples[2]))
# tuples [2] = "Bibi" #error dega q k is mai change nhi kr skte tu error ajaega

# tup = ()
# print(tup)
# print(type(tup))

# tup = (1, 2, 3, 4, 5)
# print(tup)
# print(type(tup)) #tuple aayega kyu kyu k ek element wala tuple bna hai tu python usko tuple samjhta hai

# tup = (1, 2, 3, 4, 5)
# print(tup[1:3]) #1 se 2 tk print kr dega 3 tk nhi kyu k 3rd index tk print krna hai tu 2 tk print kr dega

# #Tuple Methods:

# tup = (2,1,3,1)
# print(tup.count(1)) #1 kitni baar aya hai uska count deta hai
# print(tup.index(3)) #3 ka index deta hai

# #Practice Questions:


# lists = []
# listing1 = input("Enter your 1st favorite movies:")
# lists.append(listing1)

# listing2 = input("Enter your 2nd favorite movies:")
# lists.append(listing2)

# listing3 = input("Enter your 3rd favorite movies:")
# lists.append(listing3)

# print(lists)

#Palindrom in lists  => start and end jahn se bhi prhein word same like racecar , madam, level, rotor, kayak, reviver, madam, refer, deed, noon

list1 = [1,2,1]
list2 = [1,2,3]

# copy.list1 = list1.copy() #list1 ko copy krke copy.list1 mai store kr dega
# copy.list1.reverse() #copy.list1 ko reverse kr dega
# if(list1 ==copy.list1):
#     print("Palindrome 1")
# else:    print("Not Palindrome")


#input val pe palindrome check krna hai

# inpt = input("Enter a word:")
# copy.inpt = inpt[::-1] #input ko reverse krke copy.inpt mai store kr dega
# if(inpt ==copy.inpt):
#     print("Palindrome")
# else:    print("Not Palindrome")


#std js ka grade A hai

grade = ("C-", "A"  ,"B", "A+", "C-", "A" , "A")
print("Grade A occurs",grade.count("A"),"times")    #A kitni baar aya hai uska count deta hai

#from A -> D
# grade_lis = ["C-", "A"  ,"B", "A+", "C-", "A" , "A" , "B-", "D"]
# print(grade_lis.sort())
# print(grade_lis)


# From D -> A
grade_lis = ["C-", "A"  ,"B", "A+", "C-", "A" , "A" , "B-", "D"]
print(grade_lis.sort(reverse= True))
print(grade_lis)
