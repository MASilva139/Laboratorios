
#Herencia Simple
class Particula:
    def __init__(self, masa):
        self.masa = masa

    def energia_cinetica(self, velocidad):
        return 0.5 * self.masa * velocidad**2


class Electron(Particula):
    def __init__(self, masa, carga):
        super().__init__(masa)
        self.carga = carga

electron = Electron(9.11e-31, -1.6e-19)
print(f"Energía cinética del electrón: {electron.energia_cinetica(1e6)} J")


#Herencia Simple y absbtraccion
from abc import ABC, abstractmethod

class ParticulaAbstracta(ABC):
    def __init__(self, masa):
        self.masa = masa

    @abstractmethod
    def energia_cinetica(self, velocidad):
        pass


class Electron(ParticulaAbstracta):
    def __init__(self, masa, carga):
        super().__init__(masa)
        self.carga = carga

    def energia_cinetica(self, velocidad):
        return 0.5 * self.masa * velocidad**2


electron = Electron(9.11e-31, -1.6e-19)
print(f"Energía cinética del electrón: {electron.energia_cinetica(1e6)} J")


#Herencia, abbsbtraccion y polimorfismo
from abc import ABC, abstractmethod

class ParticulaAbstracta(ABC):
    def __init__(self, masa):
        self.masa = masa

    @abstractmethod
    def energia_cinetica(self, velocidad):
        pass


class Electron(ParticulaAbstracta):
    def __init__(self, masa, carga):
        super().__init__(masa)
        self.carga = carga

    def energia_cinetica(self, velocidad):
        return 0.5 * self.masa * velocidad**2


class Proton(ParticulaAbstracta):
    def __init__(self, masa, carga):
        super().__init__(masa)
        self.carga = carga

    def energia_cinetica(self, velocidad):
        return 0.5 * self.masa * velocidad**2

particulas = [
    Electron(9.11e-31, -1.6e-19),
    Proton(1.67e-27, 1.6e-19)
]

for particula in particulas:
    print(f"Energía cinética: {particula.energia_cinetica(1e6)} J")
    
    
# Herencia, abstraccion, polimorfismo y encapsulamiento
from abc import ABC, abstractmethod

class ParticulaAbstracta(ABC):
    def __init__(self, masa):
        self.__masa = masa

    @abstractmethod
    def energia_cinetica(self, velocidad):
        pass

    def get_masa(self):
        return self.__masa


class Electron(ParticulaAbstracta):
    def __init__(self, masa, carga):
        super().__init__(masa)
        self.carga = carga

    def energia_cinetica(self, velocidad):
        return 0.5 * self.get_masa() * velocidad**2


class Proton(ParticulaAbstracta):
    def __init__(self, masa, carga):
        super().__init__(masa)
        self.carga = carga

    def energia_cinetica(self, velocidad):
        return 0.5 * self.get_masa() * velocidad**2

electron = Electron(9.11e-31, -1.6e-19)
proton = Proton(1.67e-27, 1.6e-19)

print(f"Energía cinética del electrón: {electron.energia_cinetica(1e6)} J")
print(f"Energía cinética del protón: {proton.energia_cinetica(1e6)} J")


# Herencia, abstraccion, polimorfismo, encapsulamiento y sobrecarga
from abc import ABC, abstractmethod

class ParticulaAbstracta(ABC):
    def __init__(self, masa):
        self.__masa = masa

    @abstractmethod
    def energia_cinetica(self, velocidad):
        pass

    def get_masa(self):
        return self.__masa


class Electron(ParticulaAbstracta):
    def __init__(self, masa, carga):
        super().__init__(masa)
        self.carga = carga

    def energia_cinetica(self, velocidad):
        return 0.5 * self.get_masa() * velocidad**2

    def energia_cinetica(self, velocidad, tipo="clásico"):
        if tipo == "relativista":
            # Calcular el factor de Lorentz gamma
            gamma = 1 / (1 - (velocidad**2 / c**2))**0.5
            # Energía total relativista
            energia_total = gamma * self.get_masa() * c**2
            # Energía cinética relativista
            energia_cinetica = energia_total - self.get_masa() * c**2
            return energia_cinetica
        else:
            return 0.5 * self.get_masa() * velocidad**2


electron = Electron(9.11e-31, -1.6e-19)

print(f"Energía cinética clásica del electrón: {electron.energia_cinetica(1e6)} J")
print(f"Energía cinética relativista del electrón: {electron.energia_cinetica(1e6, tipo='relativista')} J")
