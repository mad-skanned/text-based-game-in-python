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

if __name__ == "__main__":
    main()