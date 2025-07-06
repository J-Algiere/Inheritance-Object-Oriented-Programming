"""
Inheritance (Object-Oriented Programming) with a List of Pets
"""

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return "Some generic pet sound"

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return "Woof!"

class Cat(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return "Meow!"

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
    for pet in pets:
        print(f"{pet.name} ({type(pet).__name__}) - Age: {pet.age}")
        print(f"Breed: {pet.breed}")
        print(f"{pet.name} says: {pet.speak()}")
        print()

if __name__ == "__main__":
    main()