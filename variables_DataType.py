print("Hello, World!")

name = "humaira"
age = 20
print("My name is :", name)

print(type(name))
print(type(age))


# int, boolean, string, float and none = > none ->  mtlb hm is var mai kuch bhi val nahi dena chate hain empty rkho

a = 5
b = 6
sum = 0
sum = a+b
print("Sum of ", a ,"and", b , "is: ",sum)


#type conversion 
# float is superior then integer khudi horha implicitly

a = 2
b = 2.5
sum = a+b
print(sum) #ans = 4.5 q k int ko bhi float mai krdia python ne like = 2.0 + 2.5


#type casting
#float mai string nhi krskte  manually agr krna ho tu type cast

#js val k andr krna hai usy likha and then val pass krdi 

a = float("2")
b = 3
sum =a+b
print(sum)

#type cast only tb work krti jab dosre type k ander aisa koi data ho jo hmare new data k andr fit hoske like valid numbers hn 

a = 3.14
a = str(a)
print(type(a))


# name = input("Enter your name:")
# age = input("Enter your age: ")
# marks = input("Enter your marks: ")

# print("Welcome " ,name)
# print("Your age is : " , age)
# print("Your marks are : ", marks)


# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# sum = num1 + num2
# print("Sum of ", num1 ,"and", num2 ,"is : " , sum)


# side = int(input("Enter a side of square: "))
# area = side * side 
# print("Area of square is: ", area)

num1 =  float(input("Enter a number 1 :"))
num2 = float(input("Enter number 2 : "))
avrg = (num1+num2)/ 2
print("Avrg is : ", avrg)