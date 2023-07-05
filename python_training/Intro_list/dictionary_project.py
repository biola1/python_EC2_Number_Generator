import os
cwd = os.getcwd()
file_list =[]
for file_name in os.listdir(cwd):
    file_path = os.path.join(cwd, file_name)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        
        file_info = {
            'name': file_name,
            'size': file_size
        }
        file_list.append(file_info)
for file_info in file_list:
    print(file_info)
