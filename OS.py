import os

# Task 1.1
list1 = []
filelist = os.listdir()
if len(filelist) == 0:
    print("There was nothing to be sorted!")
else:
    for x in filelist:
        if x.endswith(".txt"):
            list1.append(x)
print(list1)


# Task 1.2
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


# Testează funcția cu extensia ".txt"
list_files_with_extension(".txt")
