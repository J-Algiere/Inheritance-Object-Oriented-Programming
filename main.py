from abc import ABC, abstractmethod
import json

# Parent Class
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

# Child Class
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

# Child Class
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

def load_pets_from_file(filename):
    with open(filename, "r") as json_file:
        pet_data_list = json.load(json_file)

    pets = []

    for pet_data in pet_data_list:
        if pet_data['petType'] == "Dog":
            pets.append(Dog(pet_data['name'], pet_data['age'], pet_data['breed']))
        elif pet_data['petType'] == "Cat":
            pets.append(Cat(pet_data['name'], pet_data['age'], pet_data['breed']))
    return pets

def main():
    # Create a list to hold all pets
    orginal_pets = []

    # Add some pets to the list
    orginal_pets.append(Dog("Raven", 2, "Pitbull"))
    orginal_pets.append(Cat("Olive", 1, "Tabby"))
    orginal_pets.append(Dog("Buddy", 4, "Labrador"))
    orginal_pets.append(Cat("Mittens", 3, "Siamese"))

    # Create a list of Dictionaries for pets list
    pet_dict = [pet.to_dict()for pet in orginal_pets]


    with open("pets.json", "w") as json_file:
        json.dump(pet_dict, json_file, indent=4)


    all_loaded_pets = load_pets_from_file("pets.json")

    loaded_dogs = [pet for pet in all_loaded_pets if isinstance(pet, Dog)]
    loaded_cats = [pet for pet in all_loaded_pets if isinstance(pet, Cat)]

    print("--------Loaded dogs--------")
    for dog in loaded_dogs:
        print(f'{dog.name}\nAge: {dog.age}\nBreed: {dog.breed}\n{dog.name} says {dog.speak()}', end="\n\n")


    print("--------Loaded cats--------")
    for cat in loaded_cats:
        print(f'{cat.name}\nAge: {cat.age}\nBreed: {cat.breed}\n{cat.name} says {cat.speak()}', end="\n\n")


if __name__ == "__main__":
    main()
