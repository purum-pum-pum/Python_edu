class House():
    """Документация класса через три кавычки"""

    def __init__(self, street, number):
        """Документация функции в трех кавычках"""
        self.street = street
        self.number = number
        self.age = 2

    def build (self):
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен")

    def age_of_house(self, year):
        self.age += year


House1 = House("Московская", 20)
House2 = House("Московская", 21)

print("Номер дома House2 " + str(House2.number))

House1.build()

House1.age_of_house(3)
print("Возраст дома " + str(House1.age))


class ProspectHouse(House):

    def __init__ (self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = ProspectHouse("Ленина", House1.number)

print("Дом расположен на проспекте " + PrHouse.prospect + " " + str(PrHouse.number))
