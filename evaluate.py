from simulator import Simulator
import os
from utils import read_file
def evaluate(dir):
    score = 0
    for file in os.listdir(dir):
        f = open(os.path.join(dir,file))
        data = read_file(os.path.join("data/",file[:-4]))
        solution = dict()
        for line in f.readlines():
            line = list(map(int,line.split()))
            solution[line[0]]=line[1:]
        s = Simulator(solution,data)
        score+=s.start()
    return score


if __name__=="__main__":
    print(evaluate("./result_SA/result"))
