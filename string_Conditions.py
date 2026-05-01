str1 ="Humaira"
str2 = 'Humaira'
str3 = """Humaira"""
#\n for next line in strin 
#\t tab ka space b/w two words

# 1 => 'This is Humaira's new code' # is  invalid because the it will confuse interpreter k ye third ' khn se arha h
#"perfect"

#concatination: add to strings

first = "Humaira"
last = "Bibi"
full_name = first + " " + last
print(full_name)  # name concatinate
print(len(full_name)) #length mai tabs, spaces bhi count 

#indexing =>srf access krskte not manipulate ya chnge

str = "Humaira"
print(str[1])   #index 2

#slicing => accessing parts in strings
#starting and ending index pass kia aur beech ka pora part ajaega access ho kr

str1 = "Humaira Bibi"
print(str1[1:4]) # uma ajaega 1st index se le k 3rd index tk ajae sab

print(str1[0:7]) #pora word ajae
print(str1[7:len(str1)])  #last word ajae pora tu uske liye last index

print(str1[7:])  # last index tk hi jana hai from 7 to last index

#negative slicing -> reverse / backward counting
print(str1[-9:-5])  # -5 se -9 tk jao in reverse

#functions
 #substrings leta hai aur Boolean return true/false k us pr end horha hai ya nahi
print(str1.endswith("bi"))
print(str1.endswith("ra"))

#capital krega new string ko original mai chngs nhi krega new jo string bnega usi mai phla word capital
st = "i am learning Python from APNA COLLEGE . I am 20 years old"
#print(st.capitalize()) #func hai ye 

#agr hm apni new val of str ko purani val se replace krwana chate tu pehle usy var mai Store
# st = st.capitalize()
# print(st)

#old , new val do and replace krlo
print(st.replace("APNA COLLEGE", "YouTube"))

#exist krta hai ya nahi agr kr rha exist tu jahn bhi 1st time exit kra wahn ka index 
print(st.find("P"))

#count => konsa word kitni bar exist kr rha hai 
print(st.count("am"))


#PRACTICE:

# name =(input("Enter your first name:"))
# print(len(name))

# str = "Sea Side School"
# print(str.count("S"))


#find index find krta hai k kahan occur kr rha hai word / letter and count = kitni bar krha hai

#if k andrd elif multiple if under if 
# elif => frst state true nahi tu dosri ko check krlo

# check = int(input("Enter the number: "))

# if check %2 == 0:
#     print("Even")
# else :
#     print("Odd")


# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3: "))

# if(num1 >= num2 and num1 >= num3 ):
#     print(num1,"is greater then : ", num2, num3)
# elif (num2>=num1 and num2 >= num3):
#     print(num2,"is greater then : ", num1, num3)
# else : 
#     print(num3,"is greater then : ", num1, num2)


multiple = int(input("Enter a number: "))
if multiple % 7 == 0:
    print("Number is multiple of 7")
else : print("Number is not a multiple of 7")