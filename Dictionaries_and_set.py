# Dic -> key, values

# dict = {
#     "name" : "H.H",
#     "age" : 20,
#     "city" : "Karachi"
# }

# print(dict["name"])
# print(dict["age"])  
# print(dict["city"])


#we can also int, boolean, float, list, tuple, dict as value in dict

#mutable and 2 key same nhi ho skte nahi tu error aayega
# stud = {
#     "name" : "H.H",
#     "age" : 20,
#     "city" : "Karachi",
#     "Subjects" : ["Math", "Physics", "Chemistry"],
#     "Marks" : (85, 90, 95),
# }

# print(stud["Subjects"])
# print(stud["Marks"])
# stud["name"] =  "Bibi" #dict mutable hai isliye change kr skte tu error nhi ajaega
# print(stud["name"])

#purani values overrite kr dega tu new value print kr dega
# stud["Subjects"] = ["English", "Urdu"]  
# print(stud["Subjects"])

#empty dict bhi ho skati hai
#khali dic banai then us mai timely values add krte jayenge
null_dic = {}
null_dic ["name"] = "Humaira"
print(null_dic)

#nested Dictionary => dict ke andar dict
#ksi bhi key ki val ko dic bana do

student = {
    "name" : "H.H",
    "age" : 20,
    "city" : "Karachi",
    "Subjects" :{
    "physics" : 85,
    "chemistry" : 90,
    "math" : 95
    }
}

#student ki sbj wali dict mai phy ki val print krdo
# print(student["Subjects"] ["physics"]) #dict ke andar dict mai name key nhi hai tu error aayega

#Dict methods => srf dict pe implement hote hain ye

#sari keys ko print krne ke liye 
print(student.keys()) #dict ke sare keys ko print kr dega nested dict ka srf Subjects key print kr dega not inner dict ke keys

#hmare sare data ko list mai krdo convert
print(list(student.keys()))  #dict ke sare keys ko list mai convert kr dega nested dict ka srf Subjects key print kr dega not inner dict ke keys

print(list(student.values()))

#list k andr dic aur dic k andr list bhi store krwa skte hain

#.items => pairs banadega list of tuples
#dict ke sare key, value pairs ko print kr dega nested dict ka srf Subjects key, val print kr dega not inner dict ke keys, vals

pair = len(list(student.items()))
print(pair) #dict ke sare key, value pairs ko list of tuples mai convert kr dega nested dict ka srf Subjects key, val print kr dega not inner dict ke keys, vals

#.get key ki val return krta hai
# aik hota hai dic mai key se val lena aik hai dic se get krna key ko then val lena

# print(student["name2"]) #error de dega check krna k khn se arha h ye wala data

print(student.get("name2")) #error nhi dega, None return krega use for seeing exactly kahan pr val/ var name ghlt hai /konsi key kahan arhi hai

#agr number of lines mai koi error beech mai araha hai tu jahn error aya usse agy ka code bhi nahi chalega 

#update
#new ke, val pair se purane key and val ko update krna


student = {
    "name" : "H.H",
    "age" : 20,
    "city" : "Karachi",
    "Subjects" :{
    "physics" : 85,
    "chemistry" : 90,
    "math" : 95
    }
}


new_city = {"city" : "Lahore", "age"  : 21}
print(new_city)
print(student)


#SETS:
#unordered no index items and unique , immutable hn sare elements of set but set = mutable
# datatypes, list and dic ko store nhi krskte q k wo mutable hote hn only int, float,str,boolean,tuples

#4 unique element lega khali error nahi dega but not show o/p of similar values , no fixed order koi bhi in mai pehle askta hai

# set = {1,3,4, "Humaira", 4}
# print(set)

# print(len(set)) #4 unique element lega khali error nahi dega but not show o/p of similar values , no fixed order koi bhi in mai pehle askta hai

# collection = {} #dic 
# print(type(collection))

#So if we want to make empty set

# collection = set()
# print(type(collection))

#Methods in set:
#add method => set me element add krne ke liye pr is mai list , dic add nahi krskte only tuples

# collection = set()
# print(collection.add(1))
# print(collection.add(2))
# print(collection.add("Humaira Bibi"))
# print(collection)

#agr dic, list dale in set = unhashable type  , hash chng hua 
#remove => removing the val 
# print(collection.remove(2))
# print(collection)

#clear => pora set hi clear krdia no values => 0
# collection.clear()
# print(len(collection))

#pop => randomly agr koi val ksi set se le k show krni hai tu we use this

#order se nahi aega koi bhi random ajaega
collection = {"AI", "Python", "Humaira", "Hello", "World"}
print(collection.pop())

#union / intersection => like in maths =>combine both sets and return values

set1 = {1,2,3,4}
set2 = {1,2,3,45,6,10}
print(set1.union(set2))

#intersection => common values hi return krega 

print(set1.intersection(set2))

#PRACTICES:

wmean = {
  "word" : "meaning",
  "table" : {"a piece of furniture" , "a list of facts and figures"},
  "cat" : "a small animal" 
}
print(wmean["table"])

#set  dic ki trhn hi hain pr keys and val nahi bas is mai 
#unique classrooms chaye hain for std of these sbjs
subjects = { "Python", "Java" , "C" , "Python", "JS", "Java", "Python", "Java" , "C" , "C++" , "C", "JS" , "C++"
}
print(subjects)
print(len(subjects))

#dic mai 3 papers k marks enter krwane hain
#khali dic li hai 
marks= {}

sbj1 = int(input("Enter marks of chem:"))
#marks wali dic ko update func se () kra aur key {} aise di
marks.update({"chem" : sbj1})

sbj2 = int(input("Enter marks of phy: "))
marks.update({"phy" : sbj2 })

sbj3 = int(input("Enter marks of math: "))
marks.update({"math" : sbj3 })

print(marks)

#9 and 9.0 ko seperate values ki trhn se store krwana hai in set

val = {9,9.0}
print(val) # this will give 9 as a single val although there are 2 diff values

val = {9, "9.0"} #set ma 2 same nmbrs ko aik float aur aik int ka hai alg alg store krna hai 
print(val) # ab do alg val aengi q k hmne is mai "" laga dia and char val kuch aur hogi iski

# we can also do 1 set mai 2 tuples bana diye 

values = {

  ("float", 9.0),
  (int, 9)  
}

print(values)



