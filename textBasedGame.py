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
        "items": [],
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
    print("Welcome to the adventure.")
    print(rooms[current_room]["description"])

    while True:
        command = input("> ").strip().lower()

        if command == "quit":
            break
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
        else:
            print("You can't go that way.")

if __name__ == "__main__":
    main()