from data_reader import read_data

tmp_dna_list = read_data("rosalind_cons.txt").replace("\n", "").split(">")
tmp_dna_list.pop(0)

dna_strings = []
A_num = []
G_num = []
C_num = []
T_num = []

for mudblood_dna in tmp_dna_list : dna_strings.append(mudblood_dna[13:])

A_num = [0]*len(dna_strings[0])
C_num = [0]*len(dna_strings[0])
G_num = [0]*len(dna_strings[0])
T_num = [0]*len(dna_strings[0])

for dna_str in dna_strings :

    counter = 0
    
    for char in dna_str:
        if   char == "A" : A_num[counter] += 1
        elif char == "T" : T_num[counter] += 1
        elif char == "G" : G_num[counter] += 1
        elif char == "C" : C_num[counter] += 1
        counter += 1
        
 
counter = 0
common_ancestor = ''

while counter < len(A_num) :
    
    if A_num[counter] >= G_num[counter] and A_num[counter] >= C_num[counter] and A_num[counter] >= T_num[counter] :
        common_ancestor += "A"
        
    elif C_num[counter] >= G_num[counter] and C_num[counter] >= A_num[counter] and C_num[counter] >= T_num[counter] :
        common_ancestor += "C"
        
    elif G_num[counter] >= A_num[counter] and G_num[counter] >= C_num[counter] and G_num[counter] >= T_num[counter] :
        common_ancestor += "G"
        
    elif T_num[counter] >= G_num[counter] and T_num[counter] >= C_num[counter] and T_num[counter] >= A_num[counter] :
        common_ancestor += "T"
        
    counter += 1
    

A = list(map(str, A_num))
T = list(map(str, T_num))
G = list(map(str, G_num))
C = list(map(str, C_num))

with open ("result.txt", "w") as im_done:
    im_done.write(common_ancestor + "\n")
    im_done.write("A: " + " ".join(A) + "\n")
    im_done.write("C: " + " ".join(C) + "\n")
    im_done.write("G: " + " ".join(G) + "\n")
    im_done.write("T: " + " ".join(T))
