class Pet:
    def __init__(self, name, amount=15000):
        self.name = name
        self.amount = amount

    def check_amount(self):
        return f"Your pet amount is ${self.amount:.2f}"

    def breed(self, caste='coolie'):
        if caste == self.name:
            self.caste=True
            return "Good"
        else:
            self.caste=False
            return "Bad"

    def behave(self, sound):
        self.sound = sound
        return f"Your pet behaves like {self.sound}"

    def walking(self, color):
        self.color = color
        return f"The pet color is {self.color}"


# Create a pet object
pet = Pet("dog")

while True:
    print("\n=== PET ===")
    print("1. Check Amount")
    print("2. Breed")
    print("3. Behave")
    print("4. Walking Style")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(pet.check_amount())

    elif choice == "2":
        caste = input("Enter pet breed name: ")
        print(pet.breed(caste))

    elif choice == "3":
        sound = input("Enter sound of pet: ")
        print(pet.behave(sound))

    elif choice == "4":
        color = input("Enter pet color: ")
        print(pet.walking(color))

    elif choice == "5":
        print("Thank you for choosing pet. Goodbye!")
        break   # ← NOW this is inside the while loop

    else:
        print("Invalid option.")
