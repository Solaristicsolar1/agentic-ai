class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_dog(self):
        print(f"my name is {self.name} and I'm {self.age}")

dog_1 = Dog("loner", 2)
dog_2 = Dog("Bingo", 3)
dog_1.about_dog()
dog_2.about_dog()