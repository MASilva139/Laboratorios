import numpy as np
from simulation import simulation
from utils import data_generator, graphics

def main():
    parameters, distributions = data_generator()
    ranges, valid_angles, h_max = simulation(parameters, distributions)
    graphics(ranges, valid_angles, h_max, parameters, distributions)

if __name__ == "__main__":
    main()
