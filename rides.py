class Ride():

    def __init__(self, begin, end, tstart, tfinish, bonus ):
        self.begin = begin
        self.end = end
        self.tstart = tstart
        self.tfinish = tfinish
        self.bonus = bonus
    
    def __str__(self):
        return str((self.begin, self.end, self.tstart, self.tfinish, self.bonus))