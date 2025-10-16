class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display(self):
        print (f"The name of my pet is {self.name}, it is a/an {self.species} and it is {self.age}years old now. ")

    def celebrate(self):
        print (f'Happy birthday day {self.name}, cheers to your {self.age}rd year😘')

dog = Pet("Bruno", "Eskimo", 3)
dog.display()
dog.celebrate()

def show_first_five():
    print("\nThe first 5 multiples of 3 are: 3, 6, 9, 12, 15")

def table_of(number: int):
    """This function prints the multiplication of any number that is passed into the function from the 1 to 12"""

    print(f"\n=== Multiplication table of {number} ===")
    for n in range(1, 13):
        multiplication = number * n
        print(f"{number} x {n} = {multiplication}")


table_of(15)
show_first_five()