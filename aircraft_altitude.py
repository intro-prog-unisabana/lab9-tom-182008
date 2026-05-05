from aircraft import Aircraft

def main():
    model = input("Enter aircraft model: ")
    plane = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit): ")
        
        if command == "X":
            break
        
        action, value = command.split()
        feet = int(value)

        if action == "A":
            plane.ascend(feet)
        elif action == "D":
            plane.descend(feet)

    print(f"Final altitude: {plane.get_altitude()} feet")


if __name__ == "__main__":
    main()