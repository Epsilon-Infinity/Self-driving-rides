from timer import Timer
from ride import Ride
from vehicle import Vehicle

class Simulator():
    def __init__(self, solution: dict, data):
        self.solution = solution

        self.data = data
        self.rides = dict()
        self.vehicles = dict()
        timers = [Timer() for t in range(data["vehicles"])]

        for ride in range(data["rides"]):
            self.rides[ride] = Ride(data["rides_list"][ride], ride)
        for vehicle in range(data["vehicles"]):
            self.vehicles[vehicle] = Vehicle(vehicle, timers[vehicle], data["bonus"])

    def start(self):
        score = 0
        for v_id in self.solution.keys():
            vehicle = self.vehicles[v_id]
            rides_list = self.solution[v_id]
            for ride_id in rides_list:
                ride = self.rides[ride_id]
                score += vehicle.score_if_assigned(ride)[0]
                vehicle.assign(ride)
        return score

    def validate(self):
        all_rides = [set(r) for v, r in self.solution.items()]
        for i in range(len(all_rides)):
            for j in range(i + 1, len(all_rides)):
                if len(all_rides[i].intersection(all_rides[j])) != 0:
                    return False
        return True

