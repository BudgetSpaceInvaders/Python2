# Scrieți o funcție Python care primește ca argument un cuvânt și returnează numărul de litere unice din acel cuvânt.

unum = input("Please write your word: ")
unum = unum.lower()

list1 = set()


def Unique(unum, list1):
    for x in range(0, len(unum)):
        list1.add(unum[x])
    finumber = len(list1)
    return finumber


print(Unique(unum, list1))
