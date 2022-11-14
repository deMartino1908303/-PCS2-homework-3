DNA_file = open("rosalind_gc.txt",'r')

DNA_str = DNA_file.read().replace("\n", "").split(">")
#the first 13 characters are roslaind_xxxx

DNA_file.close()
percent = 0
DNA_str.pop(0)
for counter in range(len(DNA_str)):
    G_num = DNA_str[counter][13:].count("G")
    C_num = DNA_str[counter][13:].count("C")
    total_len = len(DNA_str[counter][13:])
    tmp_percent = ((G_num+C_num)/total_len)*100
    if tmp_percent > percent:
        percent = tmp_percent
        sample = DNA_str[counter][0:13]
        
print (sample,f"%.6f"%percent,sep = "\n")
