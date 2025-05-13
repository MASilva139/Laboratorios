import numpy as np

class Distribution():
    def __init__(self, N:int=None):
        self._N = N

    def set(self, init_val:float=None, fin_val:float=None, distribution:str=""):
        try:
            if distribution=="normal":
                var = self._normal_distribution(init_val, fin_val)
            elif distribution=="uniform":
                var = self._uniform_distribution(init_val, fin_val)
            else:
                raise Exception("No hay distribucion")
            return var
        except Exception as e:
            print(f"Error: {e}")

    def _normal_distribution(self, i:float = 0.0, f:float = 0.0):
        var = np.random.normal(i, f, self._N) 
        return var 
    
    def _uniform_distribution(self, i:float = 0.0, f:float = 0.0):
        var = np.random.uniform(i, f, self._N)
        return var
    
    def _exponential_distribution(self, i:float = 0.0, f:float = 0.0):
        var = np.random.exponential(scale=i, size=self._N)
        return var
    