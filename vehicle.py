
class Vehicle:
    def __init__(self, id ,timer, bonus=0):
        self.id = id
        self.loc = (0 ,0)
        self.step = 0
        self.rides = []
        self.bonus = bonus
        self.timer = timer

    def score_if_assigned(self, ride):
        time_to_arrive = self.timer.get_time( ) +self.distance(self.loc, ride.ride_from)

        score = self.bonus if time_to_arrive <= ride.earlist_start else 0
        finish_step = self.get_finish_step(ride)
        score += ride.distance if finish_step <= ride.latest_finish else 0
        return score, finish_step

    def assign(self, ride):

        self.timer.step(max(ride.earlist_start-self.timer.get_time() ,self.distance(self.loc ,ride.ride_from ) )+ ride.distance)
        self.step = self.get_finish_step(ride)
        self.rides.append(ride)
        self.loc = ride.to

    def distance(self, loc1, loc2):
        return abs(loc1[0 ] -loc2[0] ) +abs(loc1[1 ] -loc2[1])

    def get_finish_step(self, ride):
        return self.step + self.distance(self.loc, ride.ride_from) + ride.distance + ride.earlist_start

    def get_idx(self):
        return [ ride.idx for ride in self.rides]



