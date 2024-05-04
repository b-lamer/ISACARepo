class menu:
    def __init__(self, food):
        self.food = food

chicalf = menu("1. Chicken Alfredo")
spagmeat = menu("2. Spaghetti with Meatballs")
bakzit = menu("3. Baked Ziti")
chiccar = menu("4. Chicken Carbonara")

print("Here's ur menu")
print(chicalf.food)
print(spagmeat.food)
print(bakzit.food)
print(chiccar.food)