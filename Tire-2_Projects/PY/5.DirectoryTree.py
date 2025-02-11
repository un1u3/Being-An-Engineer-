import os 

def validate_path(path):
    if not os.path.exists(path):
        print(f'Error:Tha path {path}does not exists')
        return False
    if not os.path.isdir(path):
         print(f'Error:Tha path {path} is not a dir')
         return False
    return True



def traversal(path,indent = ''):
    try:
        items = os.listdir(path)
        items.sort()
        
        for i, items in enumerate(items):
            item_path = os.path.join(path,item)
            
            is_last = (i== len(items)-1)
            pref

def main():
    path = input("Enter the directory").strip()
    
    if validate_path(path):
        print(f"Sucess {path} is valid")
    else:
        print("Please Provide a valid pat")
        
    
         
         

        