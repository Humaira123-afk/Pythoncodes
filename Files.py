#Files I/O => files ko input lia output lia usko update kra , read , write sab kra
# file handling => file ko handle krna , usko read krna , write krna , update krna , delete krna etc

#Ram => sara data hoa hai aur ye volatile hai refresh hojata hai 
#agr kuc permenantly rkhna hota tou we do put them in files

#2 types of files:
#these all files are bits = 0,1 mai hi data store hota in memo but we divide in two categories 

#Text files = txt, doc, dox, log
#binary files = char form k ilwa kisi form mai data videos, mp4, png , jpg


#if we do filing pehle hum usy open krein ge and then update, delt kuch bhi krskte
#2 cheezein pass hoti hai in f(file ka nam, = mode  mtlb read,mode kia krna ha) by default python think agr mode nahi hai set tu wo assume krta hai that we want to read file

#abhi demo wali file and this file dono aik hi folder mai hain tu we jst write file name else we've to give full path 
# C:\Users\H.H\OneDrive\Desktop\Pythoncodes\demo.txt

# f  = open("demo.txt", "r")
# data = f.read ()
# print(data) 
# w -> "write" , truncate -> "overwrite", a -> "append", b -> "binary file" , + -> "do operations sath karne hain", t -> "text" mai likhna hi but by default jab hm r krte hain wo t text ki form mai hi open hota hai

# f  = open("demo.txt", "r")
# data = f.read (8)  #is file se srf 8 words chaye hain
# print(data) 

# file =  open("demo.txt")
# print( file.readline())

# #print hone k baad 1 line ka gap q k \n hota by default 

# print(file.readline())


#Write in files:

# import abc


# file = open("demo.txt", "w")
# file.write("Learning JS!!") #sara purana data overwrite with this line
# file.close() #file ko close krna zroori hai wrna data save nahi hoga

# #append krna hai tu w use krte hain write krna hai tu w use krte hain aur agar dono krna hai tu w+ use krte hain
# file = open("demo.txt", "a")
# file.write("Hello World!!") #sara purana data overwrite with this line
# file.close()

# file = open("demo.txt", "r")
# print(file.read())

# #agr ksi nam se file hai hi nhi tou wo file create kr dega aur usme data write kr dega
# new_file = open("sample.txt", "w")
# print(new_file.write("Welcome to Python code learning"))
# new_file.close()

# reading = open("sample.txt", "r")
# print(reading.readline())
# reading.close()

# test =  open("test.txt", "w")
# test.write("Hello Guys !!")
# test.close()

# test = open("test.txt", "a")
# test.write("Do subscribe our channel")
# test.close()

# test = open("test.txt", "r")
# print(test.read())
# test.close()

#r+ => read and write dono krna hai tu r+ use krte hain no truncate hoga data ka matlab overwrite nahi hoga data ka tu r+ use krte hain
#w+ => write and read dono krna hai tu w+ use krte hain truncae hoga data ka matlab overwrite hoga data ka tu w+ use krte hain
#a+ => append and read dono krna hai tu a+ use krte hain no truncate hoga data ka matlab overwrite nahi hoga data ka tu a+ use krte hain

# file = open("demo.txt", "r+")
# print(file.write("abc")) 
# print (file.read()) #ye read nahi karega q k file pointer end mai hai tu read krne k liye hume file pointer ko start mai lana hoga
# file.close()

# #with in files

# with open("demo.txt", "r") as file: #with use krne se hume close krne ki zarurat nahi hai
#     data = file.read()
#     print(data)

# with open("demo.txt", "w" ) as file:
#   data =  file.write("new text again")
#   print(data) #yhn close nahi krte with khudi close krdeta hai

#deleting a file 
  #modules ksi aur ne built in library mai sare function rkhe hauy hain and we are using them:

# import os #deleting library install
# os.remove("test.txt") #remove file ka nam wo khudi dlet hojaegi

#PRACTICE:


# import os
# os.remove("practice.txt")
#new file create krna hai 
# from os import read


# with open("practice.txt", "w") as new_file:
#    new_file.write("Hi everyone \n We are learning File I/O \n")
#    new_file.write("using Java \n like programming in Java")

# #ab new file mai jahn jahn JAVA hai wahn python krdo replace krne k liye read and overwrite them

# # with open("practice.txt", "r") as f:
# #    data = f.read()
# # new_data = data.replace("Java", "Python")
# # print(new_data)


# #search k learning word hai us mai ya nahi

# # def word_search(word):
# #  with open("practice.txt", "r") as f:
# #    data = f.read()
# #    if(data.find(word) != -1):
# #       print("Found")
# #    else:
# #       print("not found")
# # word_search("notepads")


# with open("practice.txt", "r") as f:
#     data = f.read()
#     replaced =  data.replace("Java", "Python")
# print(replaced)


# #search a word in file and find the line number where it is found
# def search_word(word):
 
#    with open("practice.txt", "r") as f:
#       data =  f.read()
#       if(data.find(word) != -1):
#          print("Data found at index: ",data.find(word))
#       else :
#          print("Not Found")

# search_word("Hi")

# #line konsi hai word ki

# def check_line(word):
#     line_no = 1
#     found = False

#     with open("practice.txt", "r") as f:
#         for line in f:
#             if word in line:
#                 print("Data found at line:", line_no)
#                 found = True

#             line_no += 1

#     if not found:
#         print("Not found")

# check_line("nothing")

#file mai numbers dalo and check if even or odd and total count:

with open("practice.txt", "w") as f:
    data = f.write("1,2,3,4,56,78,90,100,13")

with open("practice.txt", "r") as f:
     data = f.read()
     print(data)

count = 0
numbers = data.split(",")
for i in numbers:
   nums = int(i)
   if (nums %2 ==0):
      print("Even: " , nums)
      count += 1
   else :
      print("odd: " , nums)
print("Total even numbers: ", count)


#practice of even odd

with open("practice.txt", "w") as f:
    data = f.write("1,2,3,4,56,78,90,100,13")
    f.close()

with open("practice.txt", "r") as f: 
     
     data = f.read()
     print(data)
    
     numbers = data.split(",")
     count = 0  
     for i in numbers:
         nums = int(i) 
         if(nums %2 ==0 ):
           print("Even: ", nums)
           count += 1
         else :
           print("Odd: ", nums)


with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

count_even = 0
count_odd = 0
nums = data.split(",")
 
for i in nums:
    if(int(i)%2==0):
        print("Even ", i)
        count_even+=1
    else:
        print("Odd", i)
        count_odd+=1
print ("Count of even :",count_even) 
print ("Count of odd :",count_odd) 


