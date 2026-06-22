import random as r
def geradezahlen(bis):
    menge = []
    i = 0
    while i < bis:
        menge.append(round(i+(i*r.random()/bis)))
        i = i + 2
    return menge

