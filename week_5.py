# Polymorphism showing different animals with the same method "move"

class Dog:
    def move(self):
        print("Running 🐕")

class Bird:
    def move(self):
        print("Flying 🐦")

class Fish:
    def move(self):
        print("Swimming 🐟")

class Snake:
    def move(self):
        print("Slithering 🐍")

# Create objects
dog = Dog()
bird = Bird()
fish = Fish()
snake = Snake()

# Store them in a list and call move() on each
animals = [dog, bird, fish, snake]

for a in animals:
    a.move()
