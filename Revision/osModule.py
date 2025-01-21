import os 


# print(dir(os))

# TO get current working directory 

print(os.getcwd())

# To change directory 
# os.chdir('/home/un1u3/Desktop/')
print(os.getcwd())

# TO make a directory 

# os.makedirs("NOt")

# To delete the folder 

# os.rmdir("NOt")


# to rename 
# os.rename("hello.txt","demo.txt")




from datetime import datetime

os.chdir('/home/un1u3/Desktop/Being-An-Engineer-')

for dirpath, dirnames, filenames in os.walk('/home/un1u3/Desktop/Being-An-Engineer-'):
    print('Current Path',dirpath)
    print('Directories',dirnames)
    print('Files',filenames)



# Checking The connection   