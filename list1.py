#===========================================================================================
#1.Explain 2 ways to create a list a)crated by [] b)typecasting
#===========================================================================================
#1st way (by square bracket)
# a = [10, 20, 30, 40, 50]
# print(a)
# print(type(a))
#2nd way
# a = (10, 20, 30, 40)
# b = list(a)
# print(b)
# print(type(b))

#===========================================================================================
#2.fnamelst = ["Kulbuhshan","Shushant","Amol","Sumedh"]
#lnamelst = ["Patil","Salunke","Salunke","Kamble"]
# Amazon mail id create
# kulbushan.patil.amazon@gmail.com
# sushant.salunke.amazon@gmail.com
# amol.salunke.amazon@gmail.com
# sumedh.kamble.amazon@gmail.com
#===========================================================================================
# fnamelst = ["Kulbuhshan","Shushant","Amol","Sumedh"]
# lnamelst = ["Patil","Salunke","Salunke","Kamble"]
# full_name_lst=[i.lower()+"."+j.lower()+".amazon@gmail.com" for i,j in zip(fnamelst,lnamelst)]
# print(full_name_lst)

#===========================================================================================
# 3.fnamelst = ["Raunak","Ishi"]
# lnamelst = ["Jha","Patil"]
# deplst = ["Datascience","DevOps"]
# mail id list : 
# FORMAT - 01 - raunak.jha.datascience@gmail.com 
# FORMAT - 02 - rjha.datascience@gmail.com
# LIST COMPREHENSION : [<LOGIC> <LOOPING> <CONDITIONALSTATEMENTS>]
#===========================================================================================

#formal 01
# fnamelst = ["Raunak","Ishi"]
# lnamelst = ["Jha","Patil"]
# deplst = ["Datascience","DevOps"]
# final_lst=[i.lower()+"."+j.lower()+"."+k.lower()+"@gmail.com" 
#            for i,j,k in zip(fnamelst,lnamelst,deplst)]
# print(final_lst)

#format02
fnamelst = ["Raunak","Ishi"]
lnamelst = ["Jha","Patil"]
deplst = ["Datascience","DevOps"]
final_lst=[i[0].lower()+j.lower()+"."+k.lower()+"@gmail.com" 
           for i,j,k in zip(fnamelst,lnamelst,deplst)]
print(final_lst)

