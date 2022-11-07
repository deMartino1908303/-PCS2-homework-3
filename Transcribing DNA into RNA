def T_swap(a) :
    if a == "T":
        return "U"
    return a
DNA_file = open("rosalind_rna.txt",'r')

DNA_str = DNA_file.read()

DNA_file.close()

RNA_str = [T_swap(x) for x in DNA_str ]
print ("".join(RNA_str))
