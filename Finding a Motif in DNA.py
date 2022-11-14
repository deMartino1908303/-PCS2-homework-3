from data_reader import read_data

dna_str = read_data('rosalind_subs.txt').replace("\n", " ").split()
dna_code = dna_str[0]
segment_to_find = dna_str[1]
indexes = []
index_number = 1

while index_number < len(dna_code):
    tmp = dna_code.find(segment_to_find, index_number) +1
    if tmp == 0:
        break
    index_number = tmp
    print(index_number)
    indexes.append(str(tmp))
    
print(" ".join(indexes))
