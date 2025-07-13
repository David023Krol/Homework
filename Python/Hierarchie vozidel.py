from abc import ABC, abstractmethod

# Abstraktní třída Vozidlo
class Vozidlo(ABC):
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    @abstractmethod
    def start(self):
        """Abstraktní metoda pro startování vozidla."""
        pass

# Třída Auto, dědí z Vozidlo
class Auto(Vozidlo):
    def __init__(self, znacka, model, pocet_dveri):
        super().__init__(znacka, model)
        self.pocet_dveri = pocet_dveri

    def start(self):
        return "Auto " + self.znacka + " " + self.model + " startuje se " + str(self.pocet_dveri) + " dveřmi."

# Třída Motorka, dědí z Vozidlo
class Motorka(Vozidlo):
    def __init__(self, znacka, model, typ_motorky):
        super().__init__(znacka, model)
        self.typ_motorky = typ_motorky

    def start(self):
        return "Motorka " + self.znacka + " " + self.model + " typu " + self.typ_motorky + " startuje."

vozidla = [
    Auto("Škoda", "Octavia", 4),
    Auto("Ferrari", "458", 2),
    Motorka("Yamaha", "YZF-R1", "sportovní"),
    Motorka("Harley-Davidson", "Iron 883", "chopper")
]

for vozidlo in vozidla:
    print(vozidlo.start())
