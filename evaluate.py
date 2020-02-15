from simulator import Simulator
import os
from utils import read_file


def evaluate(dir):
    score = 0

    for file in os.listdir(dir):
        v_id = 0
        print(file)
        f = open(os.path.join(dir,file))
        data = read_file(os.path.join("data/",file[:-4]+".in"))
        solution = dict()
        for line in f.readlines():

            line = list(map(int,line.split()))

            solution[v_id]=line[1:]
            v_id += 1
        s = Simulator(solution,data)
        score+=s.start()
    return score


if __name__=="__main__":
    print(evaluate("./output/"))
