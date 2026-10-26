#===========================================================================================
#1. for and while loop: # Find out the maximum occuring element in the string.
# and also max occ more than 2 then also print all max occuring element
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
#     elif name.count(name[i])==max:
#             emp_str=emp_str+name[i]
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
#     elif name.count(i)==max:
#         emp_str=emp_str+i
# print("max occurance elements are : ",set(emp_str),"\nhaving count : ",max)
#===========================================================================================
#2.for and while loop: # Find out the minimum occuring element in the string.
 #and also min occ more than 2 then also print all min occuring element
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
#     elif name.count(name[i])==min_count:
#             emp_str=emp_str+name[i]
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
#     elif name.count(i)==min_count:
#         emp_str=emp_str+i
# print("min occurance elements are : ",set(emp_str),"\nhaving count : ",min_count)

#===========================================================================================
#3.# Find out the non-repeating element in the string
# Inputstring : "aavbbl"
# Output : vl
#===========================================================================================
# Inputstring = "aavbbl"
# emp_str=""
# for i in Inputstring:
#     if Inputstring.count(i)==1:
#         emp_str=emp_str+i
# print("Non repeating element in the string : ",emp_str)

#===========================================================================================
#4.# Find out the unique element in the string
# inputstr1 = "aavbbl"
# output : avbl
#===========================================================================================
# inputstr1 = "aavbbl"
# emp_str="" 
# for i in inputstr1:
#     if i not in emp_str:
#         emp_str=emp_str+i
# print("Unique element in the string : ",emp_str)
#===========================================================================================
#5. string functon index,find and boolean functions
#===========================================================================================
# s = "Hello World"
# print(s.index("W"))       # 6
# print(s.find("o"))        # 4
# print(s.isalpha())        # False
# print(s.isdigit())        # False
# print(s.isalnum())        # False
# print(s.islower())        # False
# print(s.isupper())        # False
# print(s.isspace())        # False

#===========================================================================================
#6.# Take a string from the user and a character also
# and print all the occurence/index.
# if not present print -1.

# M a h e s h
# 0 1 2 3 4 5
#===========================================================================================
#for loop
string=input("enter a string : ")
char=input("enter char to find : ")
emp_str=""
for i in range(len(string)):
    if string[i]==char:
        emp_str=emp_str+ str(i)+" "
if emp_str=="":
    print("-1 'char not present in string")
else :
    print("character index in string : ",emp_str)

#while loop
string=input("enter a string : ")
char=input("enter a character : ")
i=0
emp_str=""
while i<len(string):
    if string[i]==char:
        emp_str=emp_str+str[i]+" "
    i=i+1
if emp_str=="":
    print("-1 : character not present")
else :
    print("character indexes are ",emp_str)
