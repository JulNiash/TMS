from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        return "Bark"


class Cat(Animal):

    def speak(self):
        return "Meow"


class AnimalFactory:

    @staticmethod
    def create_animal(type):
        if type == "cat":
            return Cat()
        elif type == "dog":
            return Dog()


animal_type = input("Enter animal type (cat, dog): ")
animal = AnimalFactory.create_animal(animal_type)
print(animal.speak())