from data_reader import read_data
from math import log10
var = read_data("zzztmp.txt").split()
print(var)
counter_at = 0
counter_cg = 0
for cha in var[0]:
    if cha == "A" or cha == "T":
        counter_at += 1
    else:
        counter_cg += 1

for chance in var[1:]:
    chance_ct = float(chance)/2
    chance_at = (1-float(chance))/2
    prob = log10(pow(chance_at, counter_at)) + log10(pow(chance_ct, counter_cg))
    print(round(prob,3), end = " ")
