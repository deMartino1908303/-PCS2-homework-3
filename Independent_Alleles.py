from data_reader import read_data
from math import factorial

arr = read_data("rosalind_lia.txt").split()
gen = pow(2,int(arr[0]))
fig = int(arr[1])
res = 0
while fig <= gen:
    gen_fac = factorial(gen)
    fig_fac = factorial(fig)
    diff_fac = factorial(gen-fig)
    p = pow(0.25, fig)
    q = 0.75**(gen-fig)
    c = gen_fac/ (fig_fac*diff_fac)
    res += c*p*q
    fig += 1
print(round(res,3))
