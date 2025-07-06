"""
Inheritance (Object-Oriented Programming)
"""
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return "Some generic pet sound"

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Inherit name and age
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
    dog = Dog("Raven", 2, "Pitbull")
    cat = Cat("Olive", 1, "Tabby")
    print(f"{dog.name} is a {dog.breed}, {dog.age} year(s) old.")
    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} is a {cat.breed}, {cat.age} year(s) old.")
    print(f'{cat.name} says: {cat.speak()}')

if __name__ == "__main__":
    main()