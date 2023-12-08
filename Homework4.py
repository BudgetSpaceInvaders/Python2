import os
import shutil


# Problem 4

def dir_remover(direct):
    try:
        if os.path.exists(direct):
            shutil.rmtree(direct)
            print(f'The directory: {direct} was deleted successfully')
        else:
            raise FileNotFoundError
    except Exception as e:
        print(f"An unexpected error{e} has occurred!")


dir_remover("nope")
