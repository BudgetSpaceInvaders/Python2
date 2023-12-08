import os

try:
    os.mkdir("tree")
    os.makedirs("tree/python/other_directories/c")
    os.makedirs("tree/c/other_directories/cpp")
    os.makedirs("tree/cpp/other_directories/c")
    os.makedirs("tree/python/other_directories/cpp")
    os.makedirs("tree/c/other_directories/python")
    os.makedirs("tree/cpp/other_directories/python")
except FileExistsError:
    print("File already exists!")


# def find(path, target_dir):
#     curwd = os.getcwd()
#
#     if os.path.exists(path):
#         print(True)
#     else:
#         print(False)
#
#
# find("/tree", "python")


def find(path, target_dir):
    for root, dirs, files in os.walk(path):
        if target_dir in dirs:
            target_path = os.path.join(root, target_dir)
            print(target_path)


# Example input
path = "./tree"
target_directory = "python"

# Call the find function
find(path, target_directory)
