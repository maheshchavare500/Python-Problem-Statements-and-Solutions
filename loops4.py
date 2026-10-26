#===========================================================================================
#1.Find out the sum of all the prime nos from 1-100 using for loop.
#===========================================================================================
# sum=0
# for i in range(2,101):
#     flag=True
#     for j in range(2,i):
#         if i%j==0:
#             flag=False
#             break
#     if flag==True:
#         sum=sum+i
# print("sum of prime no from 1 to 100 : ",sum)

#===========================================================================================
#2.# Find out the sum of all the prime nos from 1-100 using while loop.
#===========================================================================================
# sum=0
# i=2
# while i<101:
#     flag=True
#     j=2
#     while j<i:
#       if i%j==0:
#         flag=False
#         break
#       j+=1
#     if flag==True:
#         sum=sum+i
#     i=i+1
# print(sum)

#===========================================================================================
# 3. Print nth fibonacci Number.
#===========================================================================================
# num=int(input("enter a nth no of fibonacci series : "))
# i=1
# num1=0
# num2=1
# while i<=num-2:
# 	temp=num1+num2
# 	num1=num2
# 	num2=temp
# 	i=i+1
# print("fibonacci no is : ",num2)

#===========================================================================================
#4.# Sum of fibonacci number from 1-N using while loop.
#===========================================================================================
num=int(input("enter a no till you want sum : "))
i=1
sum=0
num1=0
num2=1
while i<=num:
	sum=sum+num1
	temp=num1+num2
	num2=num1
	num1=temp
	i=i+1
print("fibonacci no is : ",num2)

