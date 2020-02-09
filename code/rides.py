class Ride():

    def __init__(self, begin, end, tstart, tfinish, bonus, rid ):
        self.begin = begin
        self.end = end
        self.tstart = tstart
        self.tfinish = tfinish
        self.bonus = bonus
        self.rid = rid
    
    def __str__(self):
        return str((self.begin, self.end, self.tstart, self.tfinish, self.bonus))