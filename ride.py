
class Ride:
    def __init__(self, ride_info, idx):
        self.ride_from = ride_info[:2]
        self.to = ride_info[2:4]
        self.earlist_start = ride_info[4]
        self.latest_finish = ride_info[5]
        self.distance = self.compute_dist(self.ride_from, self.to)
        self.idx = idx

    def compute_dist(self, loc1, loc2):
        return abs(loc1[0]-loc2[0])+abs(loc1[1]-loc2[1])

    def __eq__(self, other):
        return self.compute_dist(self.ride_from, other.ride_from) == 0 and \
            self.compute_dist(self.to, other.to) == 0

    def __lt__(self, other):
        this, o = sum(self.ride_from), sum(other.ride_from)
        return this < o or (this == o and sum(self.to) < sum(other.to))

    def __gt__(self, other):
        this, o = sum(self.ride_from), sum(other.ride_from)
        return this > o or (this == o and sum(self.to) > sum(other.to))

    def __str__(self):
        info = self.ride_from + self.to
        return ' '.join([str(i) for i in info])
