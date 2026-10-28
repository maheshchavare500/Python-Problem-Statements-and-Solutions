#===========================================================================================
#1.difference between shallow and deep copy list
#ex.studentdata = [[1, 2, 3], ["Albert", "Bob", "Charlie"], ["Pune", "Delhi", "Nanded"]]
#===========================================================================================

#1. Shallow Copy: Copies only the outer list; nested lists are shared with the original list.
  #. Deep Copy: Copies the outer list and nested lists independently.
#2. Shallow Copy: Changes to nested lists affect both the original and copied lists.
   #. Deep Copy: Changes to nested lists affect only the modified list.

#shallow copy
import copy
studentdata = [[1, 2, 3], ["Albert", "Bob", "Charlie"], ["Pune", "Delhi", "Nanded"]]
newdata = copy.copy(studentdata)
newdata[1][0] = "Mahesh"
print(studentdata)
print(newdata)

#deep copy
from copy import deepcopy
studentdata = [[1, 2, 3], ["Albert", "Bob", "Charlie"], ["Pune", "Delhi", "Nanded"]]
newdata = copy.deepcopy(studentdata)
newdata[1][0] = "Mahesh"
print(studentdata)
print(newdata)

