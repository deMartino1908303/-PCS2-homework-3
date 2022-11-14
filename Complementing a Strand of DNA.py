def nucl_swap(base) :
    if   base == "A" :
        return "T"
    elif base == "C" :
        return "G"
    elif base == "G" :
        return "C"
    elif base == "T" :
        return "A"
    return ""
    
    
DNA_file = open("rosalind_revc.txt",'r')

DNA_STR = DNA_file.read()

DNA_file.close()

reverse_dna = [nucl_swap(base) for base in DNA_STR]

reverse_dna.reverse()

print ("".join(reverse_dna))
