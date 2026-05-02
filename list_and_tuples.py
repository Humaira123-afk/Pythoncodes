#arrays => tuples and list
#tuples are immutable (unchangeable)
#list are mutable (changeable)
#tuples are faster than list


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

tuples = (56,25,"Humaira", 90)
print(tuples)
print(type(tuples[0]))
print(type(tuples[2]))