

class Vehicle:
    def __init__(self, id, bonus=0):
        self.id = id
        self.loc = (0,0)
        self.step = 0
        self.rides = []
        self.bonus = bonus

    def score_if_assigned(self, ride):
        score = self.bonus if ride.ride_from == self.loc else 0
        finish_step = self.get_finish_step(ride)
        score += ride.distance if finish_step <= ride.latest_finish else 0
        return score, finish_step

    def assign(self, ride):
        self.step = self.get_finish_step(ride)
        self.rides.append(ride)
        self.loc = ride.to

    def distance(self, loc1, loc2):
        return abs(sum(loc1) - sum(loc2))

    def get_finish_step(self, ride):
        return self.step + self.distance(self.loc, ride.ride_from) + ride.distance + ride.earlist_start

    def get_idx(self):
        return [ ride.idx for ride in self.rides]



