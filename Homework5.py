# Homework 5
import os
import shutil


def dir_largest(direct):
    try:
        if os.path.exists(direct):
            dr_list = os.listdir(direct)
            larg = ""
            len_larg = len(larg)
            for x in dr_list:
                if len_larg < os.path.getsize(x):
                    larg = x
            else:
                print(larg)

        else:
            raise FileNotFoundError
    except Exception as e:
        print(f"An unexpected error {e} has occurred!")


dir_largest("/Users/catalin/PycharmProjects/Python2")
