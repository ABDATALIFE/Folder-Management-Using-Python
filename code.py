#%%
## Importing Libraries
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
#%%


## Get the current directory of the File 
current_directory = os.getcwd()




#%%




list_sub_directories = os.listdir(current_directory)

#%%
sub_folders = []
for x in list_sub_directories:
    if os.path.isdir(x):
        sub_folders.append(os.getcwd()+x)
        




#%%

new_list_sub_directories=list([y[0] for y in os.walk(current_directory)])



#%%

file_size = []
size = {}

total_size = 0

#%%
def get_dir_size(start_path = '.'):
    total_size = 0
    if 'scandir' in dir(os):
        # using fast 'os.scandir' method (new in version 3.5)
        for entry in os.scandir(start_path):
            if entry.is_dir(follow_symlinks = False):
                total_size += get_dir_size(entry.path)
            elif entry.is_file(follow_symlinks = False):
                total_size += entry.stat().st_size
    else:
        # using slow, but compatible 'os.listdir' method
        for entry in os.listdir(start_path):
            full_path = os.path.abspath(os.path.join(start_path, entry))
            if os.path.isdir(full_path):
                total_size += get_dir_size(full_path)
            elif os.path.isfile(full_path):
                total_size += os.path.getsize(full_path)
    return total_size

def get_dir_size_walk(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

#%%
get_size = get_dir_size

dir_tree = {}


#%%
for root, dirs, files in os.walk(os.getcwd()):
    for d in dirs:
        dir_path = os.path.join(root, d)
        if os.path.isdir(dir_path):
            dir_tree[(dir_path.replace(current_directory,"")).lstrip("\\")] = get_size(dir_path)
            




#%%

for z in list_sub_directories:
    
    if os.path.isdir(z):
        
        
        size[z[-9:]] =0
        for path,dirs,files in os.walk(z):
            for f in files:
                fp = os.path.join(path,f)
                size[z[-9:]] = size[z[-9:]]+os.path.getsize(fp)
                print(f)
        
    

    
    

#%% Plotting FolderDistribution at Level 1 


values = list(size.values())
folders = list(size.keys())



#%%
for i in range(len(folders)):
    del dir_tree[folders[i]]

#%%
big_values = list(dir_tree.values())
big_folders = list(dir_tree.keys())

#%%
fig,ax = plt.subplots()
x = ["File Distribution"]




for i in range(len(size)):
     ax.bar(x,list(size.values())[i],bottom=sum(values[:i]),alpha = 0.5,edgecolor="b",linewidth=3)
ax.legend(folders,loc=1)
for i in range(len(dir_tree)):
     ax.bar(x,big_values[i],bottom=sum(big_values[:i]),alpha=0.7)
ax.legend(big_folders,loc='lower right')
#first_legend = ax.legend(handles=[folders], loc='upper right')
plt.show()
         
            
            
        

    
            

            


