#===========================================================================================
#1.string functions : upper,lower,capitalize,split,strip,count
#===========================================================================================

# 1. upper()
# a = "hello"
# print("Upper : ",a.upper())
# # 2. lower()
# b = "HELLO"
# print("lower : ",b.lower())
# # 3. capitalize()
# c = "hELLO WORLD"
# print("capital 1st letter : ",c.capitalize())
# # 4.split()
# d = "I love Python"
# print("split (remove spaces and convert list to substring) : ",d.split())
# # 5.strip()
# e = "  hello  "
# print("strip (remove left right whitespaces) : ",e.strip())
# # 6.count()
# f = "banana"
# print("count a :",f.count("a"))

#===========================================================================================
#2.# Write a code in which user enters
# 1) String eg : Laptop
# 2) character : p : 2, a: 1, t: 1, x : 0
# Code to write how many times the character is present in the string
# Constraint : You cannot use count functions.
# SECOND CONSTRAINT No use of length
#===========================================================================================

# name=input("enter a string : ")
# char=input("input char for count in string : ")
# l=0
# c=0
# for i in name:
#     l=l+1
# print("length of string : ",l)

# for j in range(0,l):
#     if name[j]==char:
#         c=c+1
# print("character ",char,"in string is : ",c)

#===========================================================================================
#3. while and for loop : # Find out the most frequent(max. occuring) in the strings.
#===========================================================================================
# while loop
# name=input("enter string : ")
# max=0
# emp_str=""
# i=0
# while i<len(name):
#     if name.count(name[i])>max:
#         emp_str=name[i]
#         max=name.count(name[i])
#     i=i+1
# print("most frequent element is : ",set(emp_str),"\nhaving count : ",max)

# # for loop
# name=input("enter string : ")
# max=0
# emp_str="" 
# for i in name:
#     if name.count(i) >max:
#         emp_str=i
#         max=name.count(i)
# print("max occurance elements are : ",set(emp_str),"\nhaving count : ",max)

#===========================================================================================
#4.while and for loop : # Find out the minimum occuring element in the string.
#===========================================================================================
#while loop
# name=input("enter string : ")
# min_count=len(name)+1
# emp_str=""
# i=0
# while i<len(name):
#     if name.count(name[i])<min_count:
#         emp_str=name[i]
#         min_count=name.count(name[i])
#     i=i+1
# print("least frequent element is : ",set(emp_str),"\nhaving count : ",min_count)

# # for loop
# name=input("enter string : ")
# min_count=len(name)+1
# emp_str="" 
# for i in name:
#     if name.count(i) <min_count:
#         emp_str=i
#         min_count=name.count(i)
# print("min occurance elements are : ",set(emp_str),"\nhaving count : ",min_count)