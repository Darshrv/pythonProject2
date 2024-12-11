import os
try:
    full_path=os.getcwd()
    print(full_path)
    full_path_file=full_path+"/example.txt"
    print(full_path_file)

    file=open(full_path_file)
except Exception as fnfe:
    print("File not found,Fix the path or create file")
finally:
    print("This code will executed anyhow")