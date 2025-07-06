"""
Inheritance (Object-Oriented Programming)
"""
def main():
    dog = Dog("Raven", "Pitbull", "1")
    print(f'{dog.name} is a {dog.breed} and is {dog.age} year(s) old.')
    print(dog.speak())

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return "Some genric pet sound"

class Dog(Pet):
    def __init__(self,name, breed, age):
        super().__init__(name, age) # call the pets __init__
        self.breed = breed

    def speak(self) -> str:
        return "Woof!"


if __name__ == "__main__":
    main()