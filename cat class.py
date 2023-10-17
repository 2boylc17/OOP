class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, amount):
        self.weight += amount

    def walk(self, amount):
        if self.weight <= 1:
            print("Can't walk anymore")
            return
        self.weight -= amount


cat1 = Cat("Flathead", 3, 4)
cat2 = Cat("Cupra", 2, 3)
cat3 = Cat("Old Tom", 10, 6)
cat4 = Cat("Scrat", 1, 1)

cat3.eat(1)
cat1.walk(1)
cat2.walk(1)
cat3.walk(1)
cat4.walk(1)
print(f" Cat 1 {cat1.weight}")
print(f" Cat 2 {cat2.weight}")
print(f" Cat 3 {cat3.weight}")
print(f" Cat 4 {cat4.weight}")