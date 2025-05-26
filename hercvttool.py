import xmi
import os

print("You can use this tool on AWS and HET virtual tapes")
print(" ")
print(" ")

tape_path = "File_does_not_exist"

while not os.path.exists(tape_path):
    if tape_path == "File_does_not_exist":
        pass
    else:
        print("The tape file does not exist, try again")
    tape_path = input("Enter the full path to the tape: ")

tape_obj = xmi.open_file(tape_path)

op = "Initial value"

print("Menu")
print(" ")
print("1: List all datasets and dataset members")
print("2: Print detailed file information")
print("3: Print JSON metadata")
print("4: Extract all files/folders on the tape to a destination folder")
print("5: Exit")

while op not in ["1", "2", "3", "4", "5"]:
    if op == "Initial value":
        pass
    else:
        print("Invalid selection, try again")
    op = input("Type the number of the desired operation: ")

if op == "1":
# To list all datasets and dataset members
    for f in tape_obj.get_files():
        if tape_obj.is_pds(f):
            for m in tape_obj.get_members(f):
                print("{}({})".format(f, m))
        else:
            print(f)

if op == "2":
    # Print detailed file information
    tape_obj.print_tape(human=True)  # Converts size to human readable

if op == "3":
    # Print JSON metatdata        
    print(tape_obj.get_json())

if op == "4":
    # Silently extract all files/folders to a destination folder of your choice
    print(" ")

    path = "Path_does_not_exist"

    while not os.path.exists(path):
        if path == "Path_does_not_exist":
            pass
        else:
            print("The path does not exist, try again")
        path = input("Enter destination folder path: ")

    tape_obj.set_output_folder(path)
    tape_obj.set_quiet(True)
    tape_obj.extract_all()
