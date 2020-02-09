from vehicles import Vehicle


def best_vehicle(rides, F, T):
    
    vehicles = []
    for ride in rides:

        # create new vehicle
        if F > 0:
            vehicles.append(Vehicle(T))
            F -= 1
        
        # find best_vehicle
        best_vehicle = vehicles[0]
        for vehicle in vehicles:
            if best_vehicle.score(ride) < vehicle.score(ride):
                best_vehicle = vehicle
        best_vehicle.add_ride(ride)
    
    return vehicles

def output_solution(vehicles, file):
    fh = open(file, 'w')

    for vh in vehicles:
        fh.write(f"{len(vh.rides)} {' '.join([str(r.rid) for r in vh.rides])}\n")


if __name__ == '__main__':
    from rides import Ride

    ride1 = Ride((2,0), (2,2), 0, 9, 2, 2)
    ride2 = Ride((1,2), (1,0), 0, 9, 2, 1)
    ride3 = Ride((0,0), (1,3), 2, 9, 2, 0)

    rides = [ride1, ride2, ride3]

    vehicles = best_vehicle(rides, 2, 10)

    file = 'solution.out'
    output_solution(vehicles, file)