class Timer:
    def __init__(self):
        self.cur_step = 0

    def get_time(self):
        return self.cur_step

    def step(self, steps=1):
        self.cur_step += steps
        return self.cur_step

    def __str__(self):
        return str(self.cur_step)

    def __repr__(self):
        return "Current time step :" + str(self.cur_step)
