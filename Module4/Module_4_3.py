class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to (self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
            else:
                print('Такого этажа не существует')
    def __len__(self):
        return (self.number_of_floors)
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House("Жк Эльбрус", 10)
h4 = House("ЖК Акация", 20)

h1.go_to(5)

print(h3)
print(h4)

print(len(h3))
print(len(h4))