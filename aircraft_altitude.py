from aircraft import Aircraft

def main():
    model = input()  
    plane = Aircraft(model)

    while True:
        command = input()  
        
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