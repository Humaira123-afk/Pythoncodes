#while jb tk ye true horha tb tk print krta rahega

#1 to 5 
i = 1
while i <= 5 :
    print("Your value is : ", i) 
    i+=1

#reverse 10 to 1
i = 10
while i>= 1:
    print("Reverse: ", i)
    i-=1

i = 1
while i <= 100:
    print(i)
    i+=1 

i = 100
while i >= 1:
    print(i)
    i-=1

# i +=1 ta k ye agy tk chalta jae agr -=1 kra tu wo negative mai deta jaega val 

n = int(input("Enter a number: "))
i = 1
while i<= 10:
    print( n ," x ", i ,"=",n * i) 
    i+=1

# print elements of the list using loop

lis = [1,4,9,16,25,36,49,64,81,100]
# manually her bar indexes pe ja ja k krwane se acha we use 
print( lis[0])
print( lis[1])
 
i = 0
while i < (len(lis)):
    print(lis[i])
    i+=1

#in a tuple earch for x using loop:
tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number: "))
i=0
found = False 
while i < len((tup)): 
    if(tup[i]==x):
      print("Found at index: ",i) 
      found = True
    i+=1

if found is False :
   print("Not found")


# break and continue:

i = 1
while i <= 10:
   if (i == 3 ): #srf kuch iterations hui then break 3 print hi nahi hosaka
      break
   print(i)
   i+=1


i = 1
while i<= 10:
    if (i%2 == 0):
         i+=1
         continue # jab i == 3 hojae tu skip krdo and agy dekhlo continue next
    print(i)
    i += 1


# For loops: sequential traversal
# for el, val, item kuch bhi likhe skte 

# num k andr lis ki sari values jati ja rhi hain

lis = [1,2,3,4,5]
for num in lis :
     print(num)

vaggies = ["Brinjal", "carrot", "peas", "cucumber"]
for vagg in vaggies :
     print(vagg)

  
tup = (1,2,3,4,5)
for tupl in tup:
    print(tupl)

# update, sopping condi => while
# traversing => for loop

name = "Humaira"
for nm in name :
    print(nm)
else : 
    print("End")

# i se tracking indexes and finding char 'o'
name = "PythonProgramming"
i = 0
for char in name:
    if(char == 'o'):
      print("o found at index ",i)
      break
    print(char)
    i+=1 #agr i ko +1 nahi kra tu wo hamesha 0 per hi rahega 

# list ko print krwana hai
lis = [1,4,9,16,25,36,49,64,81,100]

for el in lis :
   print(el)

tp = (1,4,9,16,25,36,49,64,81,100)

# number x ko dekhna hai k wo tuple mai hai ya nahi

# linear search
i = 0
x = int(input("Enter a number to find: "))
for tupl in tp :
   if(tupl == x):
      print("Value found at:", i)
      break
   i+=1
   
# range:
# by default 0 se Start 
# stepsize = kitne ka increment chaye 1
# range k andr (start, stop, step size) htota stop compulsory but start and step size not compulsory 

# even no's from 2 to 100
for i in range (2, 102, 2):
   print(i)

# 1 se 100 tk sare nmbrs print
for i in range(1, 101):
   print(i)

for i in range (100,0, -1): #start, stop, step size -1 k acc ulta chalao
    print(i)

n = int(input("Enter a number: "))
for i in range(1, 11) :
    print (n, "x", i , "=" , n * i)


# pass statement: abhi k liye koi loop ya kuch bana dia aur future mai hmein  us mai koi kam krna hai it's a placeholder for future code

# sum krwana 

n = int(input("Enter a number:"))
sum = 0
for i in range(1, n+1):
    sum += i
print ("Sum is : ",sum)


n = int(input("Enter a number:"))
sum  = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print("Sum is: ",sum)


#factorial 1***...n
n = int(input("Enter a number:"))
fact =  1
i = 1

while i<= n:
    fact *= i
    i+=1
print("Factorial is: ", fact)

n = int(input("Enter a number:"))
fact = 1
for i in range (1, n+1):
    fact *= i
print(fact)

