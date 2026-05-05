from aircraft import Aircraft

def main():
    model = input("Enter aircraft model: ")
    plane = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit): ")
        
        if command.upper() == "X":
            break
        
        parts = command.split()
        
        if len(parts) != 2:
            print("Invalid command format.")
            continue
        
        action, value = parts
        try:
            feet = int(value)
        except ValueError:
            print("Invalid number of feet.")
            continue
        
        if action.upper() == "A":
            plane.ascend(feet)
        elif action.upper() == "D":
            plane.descend(feet)
        else:
            print("Unknown command.")

    print(f"Final altitude: {plane.get_altitude()} feet")


if __name__ == "__main__":
    main()