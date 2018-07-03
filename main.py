
import csv
from collections import defaultdict


def diff_zahl(a: int, b: int):
    a_l = [int(i) for i in str(abs(a))]
    b_l = [int(i) for i in str(abs(b))]
    result = 0
    if a_l.__len__() != b_l.__len__():
        return -1
    else:
        for ziffer_a, ziffer_b in zip(a_l, b_l):
            result += ziffer_a != ziffer_b
    return result


def read():
    meldungen = dict()
    with open("Meldungen.csv", "r", encoding="utf-8") as csvsource:
        reader = csv.DictReader(csvsource)
        for row in reader:
            try:
                meldungen[row["Nummer"]]["Meldungen"] += 1
            except KeyError:
                meldungen[row["Nummer"]] = {"Meldungen": 1}
    return meldungen


def tmp(meldungen: dict):
    result = defaultdict(list)
    for nummer, dict_ in meldungen.items():
        result[dict_["Meldungen"]].append(nummer)
    return result


for i, j in sorted(tmp(read()).items(), key=lambda x:x):
    print("%d %d" % (i, j.__len__()))
