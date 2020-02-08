from rides import Ride

def read_input(file):

    fh = open(file)

    list_of_rides = []

    R, C, F, N, B, T = list(map(int, fh.readline().strip().split()))

    # append first ride
    a, b, x, y, s, f = list(map(int, fh.readline().strip().split()))
    list_of_rides.append(Ride([a,b], [x,y], s, f, B))

    for ride in range(N-1):
        a, b, x, y, s, f = list(map(int, fh.readline().strip().split()))
        
        ride = Ride([a,b], [x,y], s, f, B)

        # Insert Ride into sorted position
        inserted = False
        for i,r in enumerate(list_of_rides):

            if ride.tstart < r.tstart:
                list_of_rides.insert(i, ride)
                inserted = True
                break
            elif ride.tstart == r.tstart:
                if ride.tfinish <= r.tfinish:
                    list_of_rides.insert(i, ride)
                    inserted = True
                    break
        
        if not inserted:
            list_of_rides.append(ride)
    return list_of_rides, T


if __name__ == '__main__':
    file = 'data/e_high_bonus.in'
    inp = read_input(file)
    print(len(inp[0]))
    # print([r.__str__() for r in list_of_rides])
    


