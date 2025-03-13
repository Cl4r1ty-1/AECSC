class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound."
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof"
    
    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species}"
        
animal1 = Animal("Generic Animal", "Unknown")
dog1 = Dog("Buddy", "Golden Retriever")

print(animal1)
print(dog1)

print(animal1.make_sound())
print(dog1.make_sound())
print(dog1.sleep())