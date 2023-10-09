import os
import shutil

"""
choice1 = input("Please write the extension of the wanted file: ")
list1 = []
filelist = os.listdir()
if len(filelist) == 0:
    print("There was nothing to be copied!")
else:
    for x in filelist:
        if x.endswith(choice1):
            with open("United.txt", "r+") as list1:
                
print(list1)

global filtered_files
filtered_files = []

def list_files_with_extension(extension):
    try:
        # Obține lista de fișiere și directoare din directorul curent
        files_and_directories = os.listdir()

        # Filtrare pentru a obține doar fișierele cu extensia specificată

        filtered_files = [file for file in files_and_directories if file.endswith(extension)]


        # Afișează fișierele găsite
        if filtered_files:
            print(f"Fișierele cu extensia '{extension}' din directorul curent sunt:")
            for file in filtered_files:
                print(f"- {file}")
        else:
            print(f"Nu există fișiere cu extensia '{extension}' în directorul curent.")

    except FileNotFoundError:
        print(f"Eroare: Directorul curent nu există.")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")


def copying(path, fis):
    os.makedirs(path)
    shutil.copy(fis, path)

try:
    for x in filtered_files:
        copying("/Users/catalin/Downloads/PycharmProjects/venv/bin/python", x)
except SyntaxError:
    print("Something was written wrong, please check again or re-write the program!")


# Testează funcția cu extensia ".txt"
list_files_with_extension(".txt")"""


def copy_with_ext(source, dest, ext):
    try:
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source path {source} does not exist")
        if not os.path.exists(dest):
            os.makedirs(dest)

        for file in os.listdir(source):
            if file.endswith(ext):
                shutil.copy(os.path.join(source, file), dest)
    except Exception as e:
        print(e)


copy_with_ext("D:\\ansamble_methods\\ansamble", "D:\\ansamble_methods\\copy_d", ".png")
