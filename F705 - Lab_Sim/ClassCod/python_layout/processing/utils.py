import random
import numpy as np

#def normal_generator(n: int, mu: float=0, sigma: float=1) -> list[float]:
#    list = [random.gauss(mu=mu, sigma=sigma) for _ in range(n)]
#    return list

def normal_generator(n: int, mu: float = 0, sigma: float = 1) -> list[float]:
    #return np.random.normal(loc=mu, scale=sigma, size=n).tolist()
    return np.random.uniform(low=mu, high=sigma, size=n).tolist()
