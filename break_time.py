import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/home/aarti/Pictures")
    saved_path = os.getcwd()
    print("Current Working Directory is "+ saved_path)
    os.chdir(r"/home/aarti/Pictures")
    # (2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans(' ','_')))
    os.chdir(saved_path)

rename_files()

