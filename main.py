import utils
from copy import deepcopy
from collections import defaultdict
from ride import Ride
from vehicle import Vehicle
from simulated_annealing import SimulatedAnnealing


def solver(inputs):
    rides_list = inputs['rides_list']
    rides_list = sorted([Ride(ride_info, i) for i, ride_info in enumerate(rides_list)])
    sol = defaultdict(list)
    vehicles = [Vehicle(i + 1, inputs['bonus']) for i in range(inputs['vehicles'])]
    for ride in rides_list:
        best, vehicle = None, None
        for v in vehicles:
            cur = v.score_if_assigned(ride)
            if (not vehicle) or (cur[0] > best[0] or cur[0] == best[0] and cur[1] < best[1]):
                best, vehicle = cur, v
        vehicle.assign(ride)
    sol = {v.id: v.get_idx() for v in vehicles}
    return sol


def simulatedAnnealingSolver(inputs, T=10, n_iter=10000, temp_update=.9):
    if inputs["rides"] < 100:
        temp_update = .9
    elif inputs["rides"] < 1000:
        n_iter = 1000
        temp_update = .95
    else:
        n_iter = 10000
        temp_update = .99
    model = SimulatedAnnealing(inputs, T=T, n_iter=n_iter, temp_update=temp_update)
    model.fit()
    print("score ", model.cur_score)
    return model.solution


if __name__ == "__main__":
    utils.solve_files('data', "result_SA", simulatedAnnealingSolver)
