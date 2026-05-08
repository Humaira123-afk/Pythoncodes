# pehle hmne procedural programing seekhi then functional programming then object oriented programming
# oop me hmne class and object seekha , encapsulation , inheritance , polymorphism and

# object can be anything in our surrounding like a pen , a chair , a table , a car etc
# class => blueprint of object , template of object , design of object, jo info hemin store krwani hoti hai ksi cheez ki 

# aik class bana k then us mai jab tk obj nahi banaye it's wasted 

# class Student:
#     name = "Humaira" #similar features kia kia hnge us class k objects mai

# s1 = Student() #hmne bataya k s1 ka jo obj hai wo is class mai se aya hai 
# print(s1.name) #jitne bhi bar obj banaye ge and called with name sab mai "Humaira" hi ja rha hai

# class Cars:
#     name = "Audi"
#     brand = "Toyota"

# c1 = Cars() #ye () use for calling constructor func
# print(c1.name) 
# print(c1.brand) 
   
# Constructors => hmare pas use hote in class in __init__ function obj creation k time ye invoke hota hai, jb koi new obj banti hai tu ye func invoke hojata hai , when hm class mai obj bnate hain khudi constructor invoke hojata ha hmne jese opr wale obj mai nahi bnaya constructor pr automatically ye ban rha hoga and run bhi horha hoga

# initialization of this function ye func class k andr likhen ge
# const khud ba khud aik parameter leta hai hamesha that is self 1st para hamesha self hoga

# class Cars:
#     name = "Audi"
#     brand = "Toyota"

#     def __init__(self): #1 para self zroor leta hai constructor that is self 
#     #self => jo new obj create hua wahi hai ye refrence and point to it self = s1 ya jo bhi new ayaa hai
#        print(self)
#        print("Hello! adding new obj/std in DB")

# #ab jese hi hum is obj ko create and call krein ge init khudi run hoga

# c1 = Cars()
# print(c1)


# 2 types of attributes:
# jo chezzein common hoti hain wo class attribute mai ati hain aik class k andr hi var define krdia 
# jo cheezein diff hoti hai wo alg alg self.attribute kr k ata hai 

# class Std:
#     college_name = "XYZ college "
#     def __init__ (self, fullname , age):                   
#          #ye do para's mai dun gi in hr obj k func mai 
#         self.name = fullname   # jo bhi new val aegi fullname ki wo ajaegi yhn ,,,,self => obj aur name attribute hai ye attribute chng hoskte hain isliye self.name waghra
#         self.age = age         #new val of age for all objs
#         print("Adding new val")    #obj attribute > class obj
    
# s1 = Std ("Humaira", 20)
# print("name: ", s1.name, ":",  "Age: ",  s1.age)
# print(s1.college_name)

# s2 = Std ("Bushra", 18)
# print("name: ", s2.name,  ":", "Age: ",  s2.age )
# print(s2.college_name)

# agr aik class mai multiple init hn tou js k para match hnge wahi run hoga 
# def __init__(self): #ye default hai ye hamesha hi run hoga 
# //working
# name, age sab attributes hain mtlb var = attributes

# METHODS:
# class k andr jo functions likhte hain that are called methods

# class Std:
#     college_name = "XYZ college "
#     def __init__ (self, fullname, age):                   
        
#         self.name = fullname 
#         self.age = age
    
#     def Welcome (self):
#         print("Welcome",self.name)

#     def ages(self):
#         return self.age 

# s1 = Std ("Humaira", 18)
# s1.Welcome()
# print("Your age is: ",s1.ages())

# static methods => ye methods aise hote hain jo class k sath directly call hote hain bina kisi obj ke , ye methods self parameter nahi lete hain , ye class k sath directly call hote hain

# jese hello world print krna hai tu uske liye bhi hm static method bana k call kr kr rhe thy hala k koi sense hi nahi bnta whn need hi nahi hai iski but in these cases we can use static method 
# class level k method hote hain not of obj level. Obj level methods mai hum use krte hain self

# class Student:
  
#  @staticmethod #decorater yehn hm ye likh k agy hum use krskte hain class k andr define ye para bhi leta hai aur o/p bhi deta hai 

#  def hello():
#     print ("Hello world")
 
#  def __init__(self, name, marks):
#       self.name =  name
#       self.marks = marks

#  def avrg (self):
#       sum = 0
#       for i in self.marks:
#           sum += i
#       print("Hi!",self.name , "Your avrg score is: " , sum/3)

# s1 = Student ("Humaira", [99,90,98])
# s1.hello()
# s1.avrg()
# s1.name = "Bushra"
# s1.avrg()
# s1.name = "Rakhi"
# s1.avrg()

# 4 pillars of OOP 
# abstractions  => hiding the details of class that are unnecassary and srf imp cheezein hi dikhaen ge

# Encapsulation => data and related function ka capsule(object hai) bana dete hain ->class mai methods bhi hain aur relative data bhi haain , attribute bhi hain sab hai

# class Car :
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start (self):
#         self.acc =True  #ye sare steps class k andr hain and unnecassary hain jo hidden hain
#         self.clutch = True 
#     print("Car is starting....")

# c1 = Car()
# c1.start()

# class  Account :
#     def __init__(self, balance, account_no):
#         self.balance = balance
#         self.account_no = account_no
#         print("Bank is processing your request...")
     
#     def debit(self, amount ):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("Total balance is: ", self.get_balance())

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"was credited")
#         print("Total balance is: ", self.get_balance())

#     def get_balance(self):
#         return self.balance


# cus1 = Account (10000, 1234)
# cus1.debit(1000)
# cus1.credit(500)
# cus1.credit(4000)


# aggr obj ko ya uske attribute ko dlt krna ho tou use del func

# class info:
#     def __init__(self, name):
#      self.name = name 
 
# n1 = info("Humaira")
# print(n1.name)

# n2 = info("Bushra")
# print(n2.name)
# #ye agr delt krna ho tu we use del and is trhn se hmne n2 ko dlt krdia hai
# del n2.name
# print(n2.name)

# public / private methods and attributes
# public class k bahar bhi access krna
# private class k bahr nahi access krskte for making private use  __ in variable

# class bank:
#    def __init__(self, acc_no, acc_pass):
#       self.acc_no = acc_no
#       self.__acc_pass = acc_pass   #ab self.__ k baad aise krne se wo private hogya hai 
   
#    def reset_pass (self):
#       return self.__acc_pass
   
# acc1 =  bank("123", "abc123") 
# # print(acc1.acc_no, acc1.__acc_pass) # ye print ki statement class k bahar hai not in class k kisi func mai included tou we have to make the pass private or else anybody can access it //security => RIP
# print(acc1.acc_no)
# print(acc1.reset_pass()) #yhn ye run krjaega q k ye class k andr k func ko kr rha hai call not outside class access

# inheritance => 1 class derives the properties and methods of another class we have to use (parent class)

# 3 types of inheritance :
# single inheritance => 1 class ki properties ko srf 1 class mai hi implement krskee hain
# multi-level => 2 class 1st class ki prop use krske aur 3 wali 1,2 dono ki hi use krskti hai
# multiple inheritance => 1 class ki properties multiple classes use krskte hain

# polymorphism => 

# we are inheriting properties from Car to Toyota wali cars only
# class Car:
#    color =  "Black"
#    @staticmethod 
#    def start():
#       print("Car started...")
   
#    @staticmethod 
#    def stop():
#       print("Car stopped...")

# #ab aik actual class banani ha that is Toyota Car wali cars k liye srf
# class Toyota(Car): #inherit properties of Car

#    def __init__(self,name):
#        self.name  = name

# c1 = Toyota("Fortuner") 
# c2 = Toyota("Corolla") 

# c1.start()
# print("Car name: ",c1.name)
# print(c2.color)

# print("Car name: ",c2.name)
# print(c2.color)

# c1.stop()

# multi level inheritance =>
#  1 cheez hai Car aur car k andr Toyota ko humne rkha uske andr bhi types hain fortuner and all ab un alg alg jo cars hain unko use kr rhe hain hum for making class aur us mai ab hm inherit krein ge cars ki props
# class Car:

#    color =  "Black"
#    @staticmethod 
#    def start():
#      print("Car started...")
   
#    @staticmethod 
#    def stop():
#      print("Car stopped...")

# #ab aik actual class banani ha that is Toyota Car wali cars k liye srf
# class Toyota(Car): #inherit properties of Car

#    def __init__(self,brand):
#      self.brand = brand

# class Fortuner(Toyota):

#    def __init__ (self,type):
#      self.type = type

# c1 = Fortuner("diesel")
# c1.start()
# print(c1.type)
# c1.color = "orange"
# print(c1.color)

# c2 = Fortuner ("electric")
# print(c2.type)
# c2.color = "black"
# print(c2.color)  


# multi inheritance =>

# class A:
#    varA = "Class A"

# class B:
#   varB = "Class B"
   
# class C(A,B):
#     varC = "Class C"

# c1 = C()
# print (c1.varA)
# print(c1.varC)
# print(c1.varB)
   
# Super Method : we are talking about constructor of parent ki class 

# class methods:

# class Person:
#    name = "Anonymous" #is name ko obj k method se change krne ki try ki 

# #yhn pr hum ne isy chng krne ki koshish kri tu self , obj 2 trhn se name agyae hmare pas but we want to only change the previous one so ab hum isy directly access krne k liye ise self.name k bajaye

#    def change_name(self, name):
#       Person.name = name #we do this k class jo hai Person ki us mai hum ab jo bhi val dein name ki jaga wo pori class ka nam cheng krde
#       #another way of accessing obj of other class is: self.__class__.name = "Humaira" i trhn se obj ko access kia class k and all

# p1 = Person()
# p1.change_name("Humaira")
# print(p1.name)
# print(Person.name) #yhn jb humne class name k through check kia k asl mai PErson wali class  mai value pri kia hai tu whn hmein pta chala k whn hai #Anonymus hi mtlb abhi tk val chng nahi hui hai name ki ab hmein is class k name ko chng krna hai tu we can do k self.name ki jaga Person(class).name krein tak us class ki name val chng hojae 

# The best practice to do this all is using class methods:
# directly ksi attribute waghra ko chng krna ho tu hum aise krte k @classmethod banaeye aur humne slef k bajaye class ko ab paass krenge as an explicit argument

# class Person:
#    name = "anonymous"
#    @classmethod
#    def chng_name (cls,name):
#       cls.name = name  #ab jo bhi name chng kra wo directly class mai hoga not any obj

# p1 = Person ()
# p1.chng_name("Humaira") #yhn name chng kia tou directly name chng hogaya tha
# print(Person.name)

# static method  => jo instance / class dono mai se ksi k bhi instance/ attributes ko access nahi krte 
# class method => cls as a first para ati hai
# instance methods => self as a first para jata hai

# @property => decorater  jb hum ksi attribute ko fix val nahi deskte aur uski val ksi dosre parameter ya caluclation p depend kr rha hota hai tou we use it

# function ki property ko attributes mai cvrt kr rahe hain
# class Std :
#    def __init__(self,phy, chem, maths):
#       self.phy = phy
#       self.chem = chem 
#       self.maths = maths

#    @property #getter and setter bhi hain decorator 
#    def percentage (self):
#       return str((self.phy + self.chem + self.maths) /3) +"%"
   
# p1 = Std(99,98,97)
# print(p1.percentage)

# #ab agr marks change krne hon tu marks chng huay
# p1.phy = 87
# p1.chem = 100
# print(p1.percentage) # ab marks chng huay hain tu percentage bhi khudi update hogayi hai else agr hum @property nahi krte use tu hmein bar bar manually krna prta chng isliye humne aise kra chng 

# polymorphism => 1 hi cheez ki multiple forms hain : 
# type of poly => operator overloading

# implicit overloading

# print(1+2) #3 #hr word, hr cheez aik obj hai jo already define hai class mai 
# print("Humaira" + "Bibi") #Humaira Bibi
# print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6]

# complex numbers => 1i (real + imaginary)
# normal numbers => real no -> 1,2,3,-4,0
# jb 2 complex numbers ko + krte hain tu hum imaginary ko dono k alg aur real walun ko alg add krte hain

# -- (dunder numbers)

# class Complex():
   
#    def __init__(self, real, imaginary):
#       self.real = real
#       self.imaginary = imaginary

#    def showNumbers(self):
#       print(self.real,"i +",self.imaginary,"j")
 
#    def __add__(self, n2): #real self mai, imaginary n2
#       newReal = self.real + n2.real
#       newImg = self.imaginary +n2.imaginary
#       return Complex(newReal, newImg)
   
#    def __sub__(self, n2): #real self mai, imaginary n2
#       newReal = self.real - n2.real
#       newImg = self.imaginary - n2.imaginary
#       return Complex(newReal, newImg)
   

# n1 = Complex(9,9)
# n1.showNumbers()

# n2 = Complex(5,6)
# n2.showNumbers()
# print ("-----------")

# n3 = n1 + n2 
# n3.showNumbers()

# print("\n")
# n1.showNumbers()
# n2.showNumbers()
# print("----------")

# n4 = n1 - n2 
# n4.showNumbers()
# ab agr hmein chaye hai k ye aise hr bar krne se bajaye hmare pas hm direct no1 and no2 de dein aur wo calculation khudi hojae jese + and other hote hain in str, int, float waghra mai 
# n3 =  n1.add(n2) #aise bar bar call nahi krna pre
# n3.showNumbers()

# we have to use dunder func now agr aise krna hai tu :simply add ka jo func logic banae thi us mai __add__ krdein ge

# practice Question: 
# circle ka area , parameter calculate

# class circle :
#    def __init__(self,radius):
#       self.radius = radius

#    def Area (self):
#       return 3.14 * self.radius ** 2
   
#    def Peremeter(self):
#       return 2 * 3.14 * self.radius
   
# c1 = circle(7)
# print("Area: ", c1.Area())
# print("Paremeter ", c1.Peremeter())


# Employee class aur method hai show all things 

# class Employee:
   
#    def __init__(self,role,dept,salaray):
#       self.role = role
#       self.dept = dept
#       self.salary = salaray
   
#    def showDetails (self):
#       print("Role: ",self.role)
#       print("Department: ", self.dept)
#       print("Salary:", self.salary)



# e1 = Employee ("Inter","Finance Dept", "20,000")
# e1.showDetails()

# e2 = Employee ("Job", "DataAnalyst", "40,000")
# e2.showDetails()

# class Engineer (Employee):

#     def __init__(self,name, age): 
#        self.name = name 
#        self.age = age
#        super().__init__("Fianance", "Intern", "40,000")

#     def detail(self):
#        print("Name :" , self.name)
#        print("Age :" , self.age)


# e1 = Engineer("Humaira",20)
# e1.showDetails()
# e1.detail()


# order stores items and price use __gt__ ord1 > ord 2 if price ord1 > price ord2 

# class Order:
#    def __init__(self, items, price):
#       self.price = price
#       self.items = items
     
#    def __gt__(self, ord2):
#       return self.price > ord2.price
#    print ("->Order1 is greater than Order2 ?")

# o1 = Order ("Chips", 50)
# o2 = Order("Tea", 20)
# print(o1 > o2)



       