#===========================================================================================
#1.conditional statement : if the discount is more than 20%, buy the shirt.
#===========================================================================================

# T_shirt_price=100
# discount_perc=25
# if discount_perc>20:
#     print("Buy Tshirt")

#===========================================================================================
#2.write a conditional statement for this condition:                                        
        # stock price > 1000                Sell the stock        
        # stock price <= 1000             Hold the stock.  
#===========================================================================================
   
# stock_price=1450
# if stock_price>1000:
#     print("sell the stock")
# else:
#     print("Hold stock")   


#===========================================================================================
#3.# if shirtprice <=2000 :- Buy the shirt
# if shirtprice >2000 :- Add to my wishlist.
#===========================================================================================

# shirtprice=1500
# if shirtprice>2000:
#     print("Add to my wishlist")
# else:
#     print("buy shirt")


#===========================================================================================
#4.Write the conditional statement to handle this condition.                                                
# Product-price segementation                                        
                # >=20000        Costly product                                
                # 10000-20000                Upper middle cost product                        
                # 5000 - 10000                Lower middle cost product                        
                # <5000                Cheap product            
#===========================================================================================
#             
pro_price=5750
if pro_price<5000:
    print("cheap product")
elif pro_price >=5000 and pro_price<10000:
    print("lower middle class price")
elif pro_price >=10000 and pro_price<=20000:
    print("upper middle class price")
else:
    print("costly product")