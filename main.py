import file_helper

# ..................MAIN.......................
choice = int(input("Please choose 1 - 2 - 3: "))  # int()->because input() returns a string
print(f'You choose {choice} !')
# 1-> create file
if choice == 1:
    file_name = input("Please add file name: ")
    file_helper.create_file(file_name)
    template_name = input("Please add template name: ")
    file_helper.copy_info(file_name, template_name)
# 2-> modify file
elif choice == 2:
    file_name = input("Please add file name: ")
    template_name = input("Please add template name: ")
    file_helper.add_info(file_name, template_name)
# 3->delete file
elif choice == 3:
    file_name = input("Please add file name: ")
    file_helper.delete_file(file_name)
else:
    print("Not a valid value")
