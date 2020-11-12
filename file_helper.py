# .................IMPORTS....................
import os


# .................FUNCTIONS..................
def create_file(file_name_1):
    new_file = open(f"{file_name_1}.txt", "w+")  # w+->create if not exist, read & write
    new_file.close()


def copy_info(file_name_2, template):
    new_file = open(f"{file_name_2}.txt", "w+")
    with open(f"{template}.txt") as f:
        new_file.write(f.read())
    new_file.close()


def add_info(file_name_3, template_2):
    add_file = open(f"{file_name_3}.txt", "a")
    with open(f"{template_2}.txt") as f:
        add_file.write("\n")
        add_file.write(f.read())
        add_file.write("\n")
    add_file.close()


def delete_file(file_name_4):
    if os.path.exists(f"{file_name_4}.txt"):
        os.remove(f"{file_name_4}.txt")
    else:
        print("Sorry, the file does not exist")
