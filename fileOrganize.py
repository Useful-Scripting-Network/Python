import os  # Using system functions 
import shutil # Moving file to different folders. 
  

# Changing the folder location. 
os.chdir(os.getcwd()) 
cwd = os.getcwd() 

# For listing files from the folder. 

l = [f for f in os.listdir(cwd) if os.path.isfile(f)]  
# remove current file from list 
l.remove(os.path.basename(__file__))
l2 = [] 

# Get the extension of file from list l. 

for  value in l: 
    filename, file_extention = os.path.splitext(value)
    l2.append(file_extention)
    #s = value.split('.')[1]  
    #l2.append(s) 
#print(l, l2) 

# We remove duplicate values from  
# list l2 and checks if directory  
# exists otherwise we create new one 

for extension in set(l2): 
    dirname = extension  
    if os.path.exists(f'{cwd}\{extension}'): 
        pass
    else: 
        os.makedirs(dirname) 

# We use zip function and list l and 
# l2 passed as arguments. 
# If extension in file is same and 
# file not exists then we move the file. 

for files, extension in zip(l, l2): 
    if extension in files: 
        if os.path.exists(os.path.join(cwd, extension, files)): 
            # skip if file already exists in folder 
            pass
        else:
            # Move files to the extention folder
            print(f'{files} moved to {extension}')
            shutil.move(os.path.join(cwd, files), os.path.join(cwd, extension)) 
        #print(extension, files)
    else : 
        print('error') 


def CountFrequency(my_list): 
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1

    for key, value in freq.items(): 
        print(f"{value} files were moved to {key}")

print()
print('---'*20)
print('Summary')
CountFrequency(l2)
