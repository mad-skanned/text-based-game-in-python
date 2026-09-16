rooms = {
    "hallway": {
        "description": "A dusty hallway. Exits lead north and south.",
        "exits": {"north": "kitchen", "south": "garden"},
    },
    "kitchen": {
        "description": "An old kitchen. An exit leads south.",
        "exits": {"south": "hallway"},
    },
    "garden": {
        "description": "A quiet garden. An exit leads north.",
        "exits": {"north": "hallway"},
    },
}

def main():
    current_room = "hallway"
    print("Welcome to the adventure.")

    while True:
        print(rooms[current_room]["description"])
        command = input("> ").strip().lower()

        if command == "quit":
            break
        elif command in rooms[current_room]["exits"]:
            current_room = rooms[current_room]["exits"][command]
        else:
            print("You can't go that way.")

if __name__ == "__main__":
    main()