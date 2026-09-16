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
        "description": "A quiet garden. An exit leads north.",
        "exits": {"north": "hallway"},
        "items": [],
    },
}

def main():
    current_room = "hallway"
    print("Welcome to the adventure.")
    print(rooms[current_room]["description"])

    while True:
        command = input("> ").strip().lower()

        if command == "quit":
            break
        elif command == "look":
            print(rooms[current_room]["description"])
        elif command in rooms[current_room]["exits"]:
            current_room = rooms[current_room]["exits"][command]
            print(rooms[current_room]["description"])
        else:
            print("You can't go that way.")

if __name__ == "__main__":
    main()