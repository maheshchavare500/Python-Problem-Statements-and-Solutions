#===========================================================================================
#1.difference bwn diff types of string ' '," ",''' '''
#===========================================================================================

# ''," "--->word string
# ''' ''',"""" """  ---> multiline string 
# whithout varibale multiline string behaves like multiline comment

#===========================================================================================
#2. CHECK STRING IS MUTABLE OR NOT
#===========================================================================================

# name="mahesh"
# name[0]='s'
# print(name)
# name[0] = 's' → Tries to replace the first character m with s.
# Python raises a TypeError because strings are immutable.

#===========================================================================================
#3.string slicing : techName = "Data Science Domain"
# P.S
# Science out of techname
#===========================================================================================
# techName = "Data Science Domain"
# print(techName[5:12])
# print(techName[-14:-7])

#===========================================================================================
#4.string slicing : name = "rau kumar Jha"
# P.S
# Kumar retrive out of name
#===========================================================================================

# name = "rau kumar Jha"
# print(name[4:9])
# print(name[-9:-4])

#===========================================================================================
#5.string slicing:  ooden Gl
# every 2nd element : Alternative element
# odnG
#===========================================================================================
# name="ooden Gl"
# print(name[::2])

#===========================================================================================
#6. string slicing : 
#techname2 = "Big Data Engineering"
# Data Eng
# third element
# Dan : Output
#===========================================================================================

techname2 = "Big Data Engineering"
print(techname2[4:13])
print(techname2[-17:-8])

print(techname2[::3])