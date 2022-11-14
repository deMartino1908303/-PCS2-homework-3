DNA_file = open("rosalind_dna.txt",'r')

DNA_str = DNA_file.read()

DNA_file.close()

a = DNA_str.count("A")
c = DNA_str.count("C")
g = DNA_str.count("G")
t = DNA_str.count("T")

print(a,c,g,t)
