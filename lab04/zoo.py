# DEFINING HELP
def show_help():
    print("Type 'help' to see this list again")
    print("Type 'see' to see all the animals")
    print("Type 'pet' followed by the animal's name to pet that animal")
    print("Type 'feed' followed by the animal's name to feed that animal")
    print("Type 'bye' to leave the zoo and exit the program")

# SHOW ANIMALS
def show_all_animals():
    print("The animals in the zoo are:")
    print("* Clover the Bunny 🐇")
    print("* Coco the Baby Goat 🐐")
    print("* Arno the Alligator 🐊")
    print("* Tina the Turtle 🐢")

# PET ANIMAL
def pet_animal(animal): 
    if animal== "clover":
        print("Clover is so happy! ❤️")
    elif animal == "coco":
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == "arno":
        print("Actually, we cannot allow you to pet Arno. ⛔️ ")
    elif animal == "tina":
        print("Tina loves pets! 🐢")
    else:
        print("Sorry, I don't know that animal")

# FEED ANIMAL
def feed_animal(animal):
    if animal == "clover":
        print("Clover loves her carrots! 🥕")
    elif animal == "coco":
        print("Coco loves her hay! 🌾")
    elif animal == "arno":
        print("Arno loves his fish! 🐟")
    elif animal == "tina":
        print("Tina loves her lettuce! 🥬")
    else:
        print("Sorry, I don't know that animal")

# WELCOME MESSAGE
print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()
while True:
    response = input("What would you like to do? ").strip().lower()
    if response == "help":
        show_help()
    elif response == "see":
        show_all_animals()
    elif response.startswith("pet"):
        animal = response[4:]
        pet_animal(animal)
    elif response.startswith("feed "):
        animal = response[5:]
        feed_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        break
    else:
        print("Sorry, I don't understand that command") 