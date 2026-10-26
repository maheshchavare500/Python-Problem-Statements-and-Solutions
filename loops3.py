#===========================================================================================
#1. for and while loop : # Print all the nos from 1-10
#===========================================================================================
# for loop
for i in range(1,11):
    print(i)
#while loop
i=1
while i<=10:
    print(i)
    i=i+1

#===========================================================================================
# 2. difference between for and while loop
#===========================================================================================
# for loop	                                               while loop
# 1. Used to iterate over a sequence or range.	           1. Used to execute code while a condition is True.
# 2. Generally used when the number of iterations is known.	2. Generally used when the number of iterations is unknown.
# 3. Automatically moves to the next item.	                3. Requires manual updates when using a counter.
# 4. Less likely to cause an infinite loop.                  	4. Can cause an infinite loop if the condition never becomes False.
# 5. Example: for i in range(1, 6):	                        5. Example: while i <= 5: