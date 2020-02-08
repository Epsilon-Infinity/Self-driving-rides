def distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]+p2[1])

class Vehicle():

    def __init__(self, T):

        self.rides = []
        self.loc = (0, 0)
        self.t = 0
        self.T = T

    def __str__(self):
        return str(([r.__str__() for r in self.rides], self.loc, self.t))

    def score(self, ride):
        # find distance begin self.loc end ride.begin
        points = 0
        d = distance(self.loc, ride.begin)

        # determine if ride will start on time
        bonus = False
        if self.t + d < ride.tstart:
            # ride will start on time
            bonus = True
            points += ride.bonus

        # determine if ride will end in time
        ride_points = distance(ride.begin, ride.end)
        if bonus:
            points += ride_points
        elif self.t + d + ride_points < ride.tfinish:
            points += ride_points

        return points
    
    def add_ride(self, ride):
        
        self.rides.append(ride)

        # update time used
        d = distance(self.loc, ride.begin)
        ride_points = distance(ride.begin, ride.end)
        self.t += d + ride_points
        # update loc
        self.loc = ride.end


if __name__ == '__main__':
    from rides import Ride

    ride1 = Ride((2,0), (2,2), 0, 9, 2, 3)
    ride2 = Ride((1,2), (1,0), 0, 9, 2, 2)
    ride3 = Ride((0,0), (1,3), 2, 9, 2, 1)

    vehicle = Vehicle(10)

    vehicle.add_ride(ride2)

    print(vehicle)

    vehicle.add_ride(ride2)

    print(vehicle)

    vehicle.add_ride(ride3)

    print(vehicle)