bday = input("Please write your birthday date(in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY): ")
lsbday = []
for x in bday:
    if x.isdigit():
        lsbday.append(int(x))

answ = sum(lsbday)
