import os
import re

"""
f = open("nou.txt", "a")
f.write("Hello, world!\n")
f.close()
f = open("nou.txt", "r")
#print(f.read())
f.close()"""

fil = open("example.txt", "a")
fil.write("Hello, world!\n")
fil.close()
fil = open("example.txt", "r")
print(fil.read())
fil.close()
"""
files1 = open("fisier1.txt", "a")
files1.write("Hello, world!\n")
files1.close()
files1 = open("fisier1.txt", "r")
files2 = open("fisier2.txt", "a")
files2.write("Hello, world!\n")
files2.close()
files2 = open("fisier2.txt", "r")
files3 = open("fisierconcatenat.txt", "a")
files3.close()
# files3 = files1 + files2

filenames = ['fisier1.txt', 'fisier2.txt']
with open('fisierconcatenat.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
files3 = open("fisierconcatenat.txt", "r")
print(files3.read())
files3.close()"""

with open("example.txt", "r+") as fil:
    continut_fisier1 = fil.read()
    continut_fisier1 = continut_fisier1.replace("world", "mankind")
    print(continut_fisier1)

    fil.seek(0)

    fil.truncate()
    fil.write(continut_fisier1)

lentxt = len(continut_fisier1)
print(lentxt)

# with open("example.txt", "r+") as fil:


# with open("example.txt", "r+") as fil:
#     continut_fisier3 = fil.read()
#     continut_fisier3 = example.txt += continut_fisier2

print(os.listdir())

with open("sortare.txt", "r+") as fisier:
    continut_fisier2 = fisier.readlines()

import os
import re

nume_fisier = "sortare.txt"

if os.path.exists(nume_fisier):
    with open(nume_fisier) as f:
        content = f.readlines()
    linii_sortate = sorted(content)
    linii_sortate = re.sub(r'[^\w\s]', '', str(linii_sortate))
    numar_cuvinte = len(linii_sortate.split())
    print(numar_cuvinte)
    content = f.readlines()
linii_sortate = sorted(content)
linii_sortate = re.sub(r'[^\w\s]', '', str(linii_sortate))
numar_cuvinte = len(linii_sortate.split())
print(numar_cuvinte)
