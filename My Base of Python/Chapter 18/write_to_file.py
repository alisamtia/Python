# w: Override Every Thing or if file not exist its will create file and write tehre
# a: append mode
# r+: Start writing from 0 position and all the letters that will come at their place its will override them

with open('file2.txt','a') as f:
    f.write("\nmy name is ali")