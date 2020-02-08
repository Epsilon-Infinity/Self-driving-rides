from get_input import read_input
from best_vehicle import best_vehicle, output_solution

data = '../data/'
output = '../output/'
files = ['a_example.in','b_should_be_easy.in','c_no_hurry.in','d_metropolis.in','e_high_bonus.in']

for file in files:
    list_of_rides, F, T = read_input(data+file)
    vehicles = best_vehicle(list_of_rides, F, T)
    output_solution(vehicles, output+file.strip('.in')+'.out')

