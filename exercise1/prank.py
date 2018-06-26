import os
from string import digits
list_files=os.listdir("C:\\Users\\lab7-12\\Downloads\\prank")
print(list_files)
os.chdir("C:\\Users\\lab7-12\\Downloads\\prank")
for file in list_files:
    old_name = file
    print (old_name)
    new_name=old_name.lstrip(digits)
    print (new_name)
    os.rename(old_name,new_name)




