from random import randint
import random
import math
from copy import deepcopy
from ride import Ride
from simulator import Simulator


class SimulatedAnnealing:
    def __init__(self, data, T=100, n_iter=1000, temp_update=.9):
        self.data = data
        self.rides = dict()
        self.T = T
        self.n_iter = n_iter
        self.cur_score = 0
        self.temp_update = temp_update

        for ride in range(data["rides"]):
            self.rides[ride] = Ride(data["rides_list"][ride], ride)

        self.solution = self.get_random_solution()

        simulator = Simulator(self.solution, self.data)
        if not simulator.validate():
            print("Something is wrong with solution")
        self.cur_score = simulator.start()

    def fit(self):
        for iteration in range(self.n_iter):
            candidate_solution = self.get_random_solution(self.solution)
            simulator = Simulator(candidate_solution, self.data)
            if not simulator.validate():
                print("Something is wrong with candidate solution")
            score = simulator.start()
            if score >= self.cur_score:
                self.solution = candidate_solution
                self.cur_score = score
                print("update score :", score)
            else:
                prop_acceptance = math.exp(-(self.cur_score - score) / self.T)
                #print("Acceptance probability ", prop_acceptance)
                accept = random.choices([True, False], [prop_acceptance, 1 - prop_acceptance])[0]
                if accept:
                    self.solution = candidate_solution
                    self.cur_score = score
                    print("accept score :", score)
                    self.T = self.temp_update * self.T

        return self.solution

    def get_random_solution(self, cur_solution=None):
        if cur_solution == None:
            solution = dict()
            rides = self.rides.keys()
            for vehicle in range(self.data["vehicles"]):
                solution[vehicle] = []
                count = len(rides) // self.data["vehicles"]
                for ride in rides:
                    solution[vehicle].append(ride)
                    count -= 1
                    if count == 0:
                        rides = rides.__sub__(set(solution[vehicle]))
                        break
            return solution
        else:
            cur_solution = deepcopy(cur_solution)
            actions = ["delete", "swap", "add"]
            count_selected = sum([len(rides) for v, rides in cur_solution.items()])
            p_delete = 0.2 * (count_selected - 1) / len(self.rides)
            p_add = 0.2 * (1 - (count_selected) / len(self.rides))
            probs = [p_delete, 1 - p_delete - p_add, p_add]

            action = random.choices(actions, probs)[0]
            if action == "delete":
                # To-Do make it as a weigted choice
                v = random.randint(0, self.data["vehicles"] - 1)
                while len(cur_solution[v]) == 0:
                    v = random.randint(0, self.data["vehicles"] - 1)
                to_remove = random.choices(cur_solution[v])[0]
                cur_solution[v].remove(to_remove)
                return cur_solution

            elif action == "add":
                rides = self.rides.keys()
                selected_rides = set()
                for v, r in cur_solution.items():
                    selected_rides.update(set(r))

                remaining = list(rides.__sub__(selected_rides))
                to_add = random.choices(remaining)[0]
                vehicle = random.randint(0, self.data["vehicles"] - 1)
                if len(cur_solution[vehicle]) >= 1:
                    index = random.randint(0, len(cur_solution[vehicle]) - 1)
                else:
                    index = 0
                cur_solution[vehicle].insert(index, to_add)
                return cur_solution

            else:  ## action is swap
                from_v = random.randint(0, self.data["vehicles"] - 1)
                while len(cur_solution[from_v]) == 0:
                    from_v = random.randint(0, self.data["vehicles"] - 1)
                to_v = random.randint(0, self.data["vehicles"] - 1)
                while len(cur_solution[to_v]) == 0:
                    to_v = random.randint(0, self.data["vehicles"] - 1)

                from_index = random.randint(0, len(cur_solution[from_v]) - 1)
                to_index = random.randint(0, len(cur_solution[to_v]) - 1)

                cur_solution[from_v][from_index], cur_solution[to_v][to_index] = cur_solution[to_v][to_index], \
                                                                                 cur_solution[from_v][from_index]
                return cur_solution

    def write(self, output_file="solution.out"):
        f = open(output_file)
        for v, r in self.solution.items():
            f.write(str(v+1)+" ")
            f.write(" ".join([str(ride) for ride in r])+"\n")



