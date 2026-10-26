#===========================================================================================
#1.# Print the alternate element of the string
#===========================================================================================
# name="mahesh"
# print(name[::2])

#===========================================================================================
#2.# Print the reversal of the string
#===========================================================================================
# name="mahesh"
# print(name[::-1])

#===========================================================================================
#3. PRINT THE ALTERNATE ELEMENTS IN THE REVERSAL OF THE STRING
#===========================================================================================


# name="mahesh"
# print(name[::-2])

#===========================================================================================
#4.two approaches and while and for loop alsoCheck if the string is palindrome or not
#  1.slicing 2.floor divison half string
#===========================================================================================

#1.slicing
# name="naman"
# if(name==name[::-1]):
#     print("palindrome")
# else :
#     print("non palindrome")

#2.floor divison
#for
# name=input("enter string to check palindrome : ")
# l=len(name)
# flag=True
# for i  in range(0,l):
#     if name[i]!=name[l-i-1]:
#         flag=False
#         break
# if flag==True:
#     print("palindrome")
# else :
#     print("not a palindrome")

#while loop
name=input("enter a string to check palindrome : ")
l=len(name)
flag=True
i=0
while i<l:
    if name[i] !=name[l-1-i]:
        flag=False
        break
if flag==True:
    print("palindrome")
else:
    print("not a palindrome")