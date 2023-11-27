import os
import shutil #Delete, copy, move
# os.chdir(r'')
# print(os.listdir())

# file_iter=os.walk(r'D:\Backup\Python\Python Projects\Chapter 20')
# for currect_path,folder_names,file_names in file_iter:
#     print(f'Currect Path: {currect_path}')
#     print(f'Folder Path: {folder_names}')
#     print(f'File Names: {file_names}')

# Delete only those folders/files that 
# os.rmdir('new')

# Make 2 new folders folder inner folder
# os.makedirs('songs\Hindi Songs')

# Delete a folder with its inner files or folders:
# shutil.rmtree('songs')

# copy a full folder/file
# shutil.copytree('songs','Ali/songs')

# copy file
# shutil.copy('file.txt','Ali\file.txt')

# move a file
shutil.move('file.txt',r'Ali\file.txt')