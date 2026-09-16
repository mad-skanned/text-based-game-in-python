rooms = {
    "hallway": {
        "description": "A dusty hallway. Exits lead north and south.",
        "exits": {"north": "kitchen", "south": "garden"},
        "items": [],
    },
    "kitchen": {
        "description": "An old kitchen. An exit leads south.",
        "exits": {"south": "hallway"},
        "items": ["key"],
    },
    "garden": {
        "description": "A quiet garden. An exit leads north. There is a locked shed to the east.",
        "exits": {"north": "hallway", "east": "shed"},
        "items": ["flower"],
    },
    "shed": {
        "description": "Inside the shed, sunlight streaks through the cracks. You made it.",
        "exits": {"west": "garden"},
        "items": [],
    },
}

def main():
    current_room = "hallway"
    inventory = []
    moves = 0
    print("Welcome to the adventure.")
    print(rooms[current_room]["description"])

    while True:
        command = input("> ").strip().lower()

        if command == "":
            continue
        moves += 1

        if command == "quit":
            break
        elif command == "help":
            print("Commands: look, take <item>, drop <item>, examine <item>, inventory, help, quit, or a direction (north/south/east/west)")
        elif command == "look":
            print(rooms[current_room]["description"])
            if rooms[current_room]["items"]:
                print("You see:", ", ".join(rooms[current_room]["items"]))
        elif command.startswith("take "):
            item = command[5:]
            if item in rooms[current_room]["items"]:
                rooms[current_room]["items"].remove(item)
                inventory.append(item)
                print(f"You take the {item}.")
            else:
                print("There's nothing like that here.")
        elif command.startswith("drop "):
            item = command[5:]
            if item in inventory:
                inventory.remove(item)
                rooms[current_room]["items"].append(item)
                print(f"You drop the {item}.")
            else:
                print("You aren't carrying that.")
        elif command.startswith("examine "):
            item = command[8:]
            if item in inventory or item in rooms[current_room]["items"]:
                print(f"It's a {item}. Nothing special stands out.")
            else:
                print("You don't see that here.")
        elif command == "inventory":
            if inventory:
                print("You are carrying:", ", ".join(inventory))
            else:
                print("You aren't carrying anything.")
        elif command in rooms[current_room]["exits"]:
            destination = rooms[current_room]["exits"][command]
            if destination == "shed" and "key" not in inventory:
                print("The shed is locked. You need a key.")
            else:
                current_room = destination
                print(rooms[current_room]["description"])
                if current_room == "shed":
                    print("You win!")
                    break
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()