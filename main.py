import pickle
import os

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("не имплементирован")

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чирикает!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} хрюкает!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит!")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.role = "работник"

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.role = "Ветеринар"

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, {animal.age} лет")

    def show_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, {staff.role}")

    def save_zoo(self, filename):
        with open(filename, "wb") as file:
            pickle.dump((self.animals, self.staff), file)
            print("Зоопарк сохранен.")

    def load_zoo(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'rb') as file:
                    self.animals, self.staff = pickle.load(file)
                    print("Зоопарк загружен.")
            except Exception as e:
                print("Произошла ошибка при чтении файла:", e)
        else:
            print("Зоопарк создается первый раз.")


zoo = Zoo()
zoo.load_zoo("zoo_data.pkl")

staff_k1 = ZooKeeper("Иван")
staff_v1 = Veterinarian("Коля")

zoo.add_staff(staff_k1)
zoo.add_staff(staff_v1)

boar = Mammal("хряк", 5)
sparrow = Bird("воробей", 7)
varan = Reptile("варан", 8)

zoo.add_animal(sparrow)
zoo.add_animal(boar)
zoo.add_animal(varan)

zoo.save_zoo("zoo_data.pkl")

zoo.show_animals()
zoo.show_staff()

animal_sound(zoo.animals)

staff_k1.feed_animal(boar)
staff_v1.heal_animal(sparrow)
