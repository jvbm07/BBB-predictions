import pandas as pd

def criaTabelaParedoes(path):
    ###
    return


prefix = "../../data/external/paredoes/paredoes20"
for i in range(1,22):
    if i < 10:
        suffix = "0" + i + ".csv"
    else:
        suffix = i + ".csv"
    path = prefix + suffix
    criaTabelaParedoes(path)