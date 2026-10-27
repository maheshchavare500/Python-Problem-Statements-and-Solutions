
#1.Expllain reverse and index function in list
#reversse
# lst = ["Raunak","Yash","Shushant"]
# print("Before ",lst)
# lst.reverse()
# print("After ",lst)
# #index
# productlst = ["T-Shirt","Jeans","Shorts","Shirt","Shirt","Jeans"]
# print(productlst.index("Shorts"))
# print(productlst.index("Shirt"))


#2.# P.S
# List input
# Element input
# if present : each occurence
# if not present : -1
# return
# lst=input("entere  a list : ").split()
# ele=input("enter element : ")
# emp_lst=[]
# for i in range(len(lst)):
#     if lst[i]==ele:
#         emp_lst.append(i)
# if emp_lst==[]:
#     print("-1 element not present")
# else :
#     print("element found at index : ",emp_lst)


#3.P.S explain insert, append,extend
#emplst = ["Kulbushan","Sumedh","Amol","Prachi","Sushant"]
#insert  insert element at specific position
# emplst = ["Kulbushan","Sumedh","Amol","Prachi","Sushant"]
# emplst.insert(2,"mahesh")
# print(emplst)
# #append append only one element at the end of list
# emplst = ["Kulbushan","Sumedh","Amol","Prachi","Sushant"]
# emplst.append("mahesh")
# print(emplst)
# #extend It adds all elements of the second list to the original first list.
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)  
# print(b)  

#4.# DIFFERENCE OBSERVE LIST CONCATENATION VS EXTEND??
# a = [1, 2]
# b = [3, 4]
# print(a + b)  # [1, 2, 3, 4]  concat
# print(a.extend(b))  # None   just called
# print(a)  # [1, 2, 3, 4]     printed

#5.explain 2 d list  
empdata =     [[1,2,3],
              ["Yash","Shushant","Ravi"],
              ["Raj","Salunke", "Kamble"],
              ["Pune","Mumbai","Delhi"],
              ["Sales","DevOps","Data"]]
# Shushant retrive
print(empdata[1][1])
#delhi retrive
print(empdata[3][2])