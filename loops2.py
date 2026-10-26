#===========================================================================================
#1.for and while loop : # Find out the sum of all the even Nos from 1-100.
#===========================================================================================
#for loop
# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum=sum+i
# print("for loop : sum of even from 1-100 : ",sum)
# #while loop
# s=0
# j=1
# while j<101:
#     if j%2==0:
#         s=s+j
#     j=j+1
# print("while loop:sum of even from 1-100 : ",s)

#===========================================================================================
#2.for and while loop : # Find out the sum of all the odd nos from 50-250.
#===========================================================================================
#for loop
sum=0
for i in range(50,251):
    if i%2!=0:
        sum=sum+i
print("for loop : sum of odd from 50-250 : ",sum)
# #while loop
s=0
j=50
while j<251:
    if j%2!=0:
        s=s+j
    j=j+1
print("while loop:sum of odd from 50-250 : ",s)

#===========================================================================================
#3.for and while loop :Find out the product and sum of all even nos and all odd nos from 1-100
#===========================================================================================
#for loop
# s_even=0
# s_odd=0
# p_even=1
# p_odd=1
# for i in range(1,101):
#     if i%2==0:
#         s_even=s_even+i
#         p_even=p_even*i
#     else:
#         s_odd=s_odd+i
#         p_odd=p_odd*i
# print("even sum : ",s_even)
# print("odd sum : ",s_odd)
# print("even product : ",p_even)
# print("odd product : ",p_odd)

#while loop
# s_even=0
# s_odd=0
# p_even=1
# p_odd=1
# i=1
# while i<=100:
#     if i%2==0:
#             s_even=s_even+i
#             p_even=p_even*i
#     else:
#             s_odd=s_odd+i
#             p_odd=p_odd*i
#     i=i+1
# print("even sum : ",s_even)
# print("odd sum : ",s_odd)
# print("even product : ",p_even)
# print("odd product : ",p_odd)

#===========================================================================================
#4.for and while loop# Check whether a number is prime or not.
#===========================================================================================
#for loop(with flag)
# num=7
# flag=True
# for i in range(2,num):
#        if num%i==0:
#               flag=False
#               break
# if flag==True:
#        print("prime")
# else:
#        print("not prime")

#while loop(with flag)
# flag=True
# num=37
# i=2
# while i<num:
#     if num%i==0:
#         flag=False
#         break
#     i=i+1
# if flag==True:
#     print("prime")
# else:
#     print("not prime")

#===========================================================================================
#5. for and while  without flag :  Check whether a number is prime or not
#===========================================================================================
#for loop
# num=int(input("enter a no : "))
# for i in range(2,num):
#     if num%i==0:
#         print("Non-prime")
#         break
# else:
#     print("prime")
#while loop(without flag)
# num=int(input("enter a no to check prime :"))
# i=2
# while i<num:
#     if num%i==0:
#         print("non_prime")
#         break
#     i=i+1
# else:
#     print("prime")