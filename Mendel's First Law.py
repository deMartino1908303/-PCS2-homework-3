from data_reader import read_data

population = list(map(int,read_data('rosalind_iprb.txt').split()))

total_pop = 0 

for x in population : total_pop += x

probAA = 1 * (population[0]/total_pop)

probAa = ((1 * (population[0] / (total_pop-1))) + (0.75 * ((population[1]-1) / (total_pop-1))) + (0.5 * (population[2] / (total_pop-1)))) * (population[1]/total_pop)

probaa = ((1 * (population[0] / (total_pop-1))) + (0.50 * (population[1]/(total_pop-1)))) * (population[2]/total_pop)

print( probAA + probAa + probaa)



___________________
data redar is a function i created to read input from a file more easly
