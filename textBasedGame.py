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
    print(rooms[current_room]["description"])

if __name__ == "__main__":
    main()