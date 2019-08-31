from sys import exit

def start():
    print("You are in a strange room with a lot of doors. All of them are closed")
    print("There is a table in the room with a key, that fits only to 15 inches door, a small bottle with unknown liquid and pie.")
    print("Which one will you take: bottle or pie?")

    choice = input("> ")

    if choice == "bottle":
        wonderland()
    elif choice == "pie"
        through_looking_glass()
    else:
        dead("You stumble around the room until you starve.")

start()
