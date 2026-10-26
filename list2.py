#===========================================================================================
# 01 Print the squares of all the numbers from 1-100.
# LIST COMPREHENSIONS.
# 1 2 3 4 5.... 100
#===========================================================================================
# square=[i*i for i in range (1,101)]
# print(square)

#===========================================================================================
#02 Print the cube of all the odd numbers from 25-250.
# LIST COMPREHENSION USE.
# 25 26..250
#===========================================================================================
# cube=[i*i*i for i in range(25,251,2)]
# print(cube)

#===========================================================================================
#3# employee salary list, I want to check number of employees having salary>20 LPA
# emplst = [19,20,21,22,25,28,29,5,8,9,11,29,30,8,5,11,15]
# # Using list comprehension
#===========================================================================================
# emp_sal=[i for i in emplst if i>20]
# print(emp_sal,"\ncount of having salary >20 : ",len(emp_sal))

#===========================================================================================
#4.explain sort(),count(),min(),max()
#===========================================================================================
#sort
# a = [40, 10, 30, 20, 50]
# a.sort()
# print(a)
# b = [40, 10, 30, 20, 50]
# b.sort(reverse=True)
# print(b)

#count
# a = [10, 20, 10, 30, 10, 40]
# print(a.count(10))

#min(),max()
# a = [40, 10, 30, 20, 50]
# print(min(a))
# print(max(a))

#===========================================================================================
#5.# Find out the maximum  element in the list.
#In 3 ways
#===========================================================================================
#1st way max function
# lst = [5,4,3,10,8]
# print("maximum ",max(lst))
# print("minimum ",min(lst))
#2 2nd way sorting
# lst = [5,4,3,10,8]
# lst.sort(reverse=True)
# print("maximum :",lst[0])
# print("minimum :",lst[-1])
#3rd way by making 1st as large
# lst = [5,4,3,10,8]
# max=lst[0]
# min=lst[0]
# for i in lst:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
# print("maximun element is : ",max,"/nminimum element is : ",min)

#===========================================================================================
#6..# PRINT THE SECOND LARGEST ELEMENT IN THE LIST
#2 ways first. sort and slicing function   second : NUMBER LINE APPROACH
#===========================================================================================
#1st way   sort and slicing function 
# lst = [5,4,3,10,8]
# lst.sort()
# print(lst[-2])
# second way : number line approach
# lst = [5,4,3,10,8]
# fir_lar=lst[0]
# sec_lar=lst[0]
# for i in lst:
#     if i>fir_lar:
#         sec_lar=fir_lar
#         fir_lar=i    
#     elif i<fir_lar and i>sec_lar:
#         sec_lar=i
# print("second largest element in the list : ",sec_lar)


#===========================================================================================
#7. Find out the most frequency element in the list.
#===========================================================================================
#for loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# max_count=0
# emp_str=""
# for i in lst:
#     if lst.count(i)>max_count:
#         max_count=lst.count(i)
#         emp_str=i
#     elif max_count==lst.count(i) and i!=emp_str:
#         emp_str=emp_str+" "+i
# print("maximum count element in list is :",emp_str,"\n having count :",max_count)
#while loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# max_count=0
# emp_str=""
# i=0
# while i<len(lst):
#     if lst.count(lst[i])>max_count:
#         max_count=lst.count(lst[i])
#         emp_str=lst[i]
#     elif max_count==lst.count(lst[i]) and lst[i]!=emp_str:
#         emp_str=emp_str+" "+lst[i]
#     i=i+1
# print("maximum count element in list is :",emp_str,"\n having count :",max_count)

#===========================================================================================
#8. Find out the least frequency element in the list.
#for loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# min_count=len(lst)+1
# emp_str=""
# for i in lst:
#     if lst.count(i)<min_count:
#         min_count=lst.count(i)
#         emp_str=i
#     elif min_count==lst.count(i) and i!=emp_str:
#         emp_str=emp_str+" "+i
# print("minimum count element in list is :",emp_str,"\n having count :",min_count)
#while loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# min_count=len(lst)+1
# emp_str=""
# i=0
# while i<len(lst):
#     if lst.count(lst[i])<min_count:
#         min_count=lst.count(lst[i])
#         emp_str=lst[i]
#     elif min_count==lst.count(lst[i]) and lst[i]!=emp_str:
#         emp_str=emp_str+" "+lst[i]
#     i=i+1
# print("minimum count element in list is :",emp_str,"\n having count :",min_count)

#===========================================================================================
#9. Find out the unique element in the list.
#for loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# emp_str=""
# for i in lst:
#     if i not in emp_str:
#         emp_str=emp_str+" "+i
# print("unique element in strings are : ",emp_str)
#while loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# emp_str=""
# i=0
# while i<len(lst):
#     if lst[i] not in emp_str:
#         emp_str=emp_str+" "+lst[i]
#     i=i+1
# print("unique element in strings are : ",emp_str)

#===========================================================================================
#10. Find out the non-repeating element in the list.
#===========================================================================================
#for loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# for i in lst:
#     if lst.count(i)==1:
#         print(i," ")
#while loop
# lst = ["Raunak","Ravi","Shushant","Yash","Yash"]
# i=0
# while i<len(lst):
#     if lst.count(lst[i])==1:
#         print(lst[i]," ")
#     i=i+1