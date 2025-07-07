"""
Inheritance (Object-Oriented Programming) with a List of Pets
"""
from abc import ABC, abstractmethod
import json

class Pet(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self) -> str:
        pass
    @abstractmethod
    def to_dict(self):
        pass

class Dog(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return "Woof!"

    def to_dict(self):
        return \
            {
                "petType": type(self).__name__,
                "name": self.name,
                "age": self.age,
                "breed": self.breed
            }

class Cat(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return "Meow!"

    def to_dict(self):
        return \
            {
                "petType": type(self).__name__,
                "name": self.name,
                "age": self.age,
                "breed": self.breed
            }

def main():
    # Create a list to hold all pets
    pets = []

    # Add some pets to the list
    pets.append(Dog("Raven", 2, "Pitbull"))
    pets.append(Cat("Olive", 1, "Tabby"))
    pets.append(Dog("Buddy", 4, "Labrador"))
    pets.append(Cat("Mittens", 3, "Siamese"))

    # Loop through the pets and print info
    print("---- Pet Roster ----")
    for pet in pets :
        print(f"{pet.name} ({type(pet).__name__}) - Age: {pet.age}")
        print(f"Breed: {pet.breed}")
        print(f"{pet.name} says: {pet.speak()}")
        print()

    # Create a list of Dictionaries for pets list
    pet_dict = [pet.to_dict()for pet in pets]


    with open("pets.json", "w") as json_file:
        json.dump(pet_dict, json_file, indent=4)
        print(json.dumps(pet_dict, indent=4))

if __name__ == "__main__":
    main()