import re

PATH = r"C:\Users\User\Desktop\python cyber\message.txt"


def remove_duplicates(lst):
    rng1 = [y for y in range(len(lst))]
    for i in rng1:
        rng2 = [x for x in range(i,len(lst))]
        for j in rng2:
            if lst[i] == lst[j]:
                lst.pop(j)
                rng1.pop(len(rng1) - 1)
                rng2.pop(len(rng2) - 1)
    return lst

def extract():
    s = open(PATH, "r")
    text = s.read()
    PROGRAMS = re.compile("\s").split(text)

    PROGRAMS = [i[:-4] for i in PROGRAMS if i[-3:] == "exe"]
    PROGRAMS = [PROGRAMS[i] for i in range(0, len(PROGRAMS) - 1) if PROGRAMS[i] != PROGRAMS[i + 1]]
    PROGRAMS = remove_duplicates(PROGRAMS)
    for i in PROGRAMS:
        print(i)


extract()