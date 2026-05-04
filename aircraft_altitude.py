from aircraft import Aircraft

def main():
    model = input("Enter aircraft model: ")
    my_aircraft = Aircraft(model)

    while True:
        user_input = input("Enter command (A for ascent, D for descent, X to exit): ")
        
        # .split() separa por espacios
        parts = user_input.split()
        
       
        if not parts:
            continue
            
        command = parts[0].upper()

        if command == "X":
            break
        
    
        elif (command == "A" or command == "D") and len(parts) > 1:
            try:
                feet = int(parts[1])
                if command == "A":
                    my_aircraft.ascend(feet)
                else:
                    my_aircraft.descend(feet)
            except ValueError:
                print("Invalid number of feet.")
        
        else:
            print("Invalid command or missing parameters.")

    
    print(f"Final altitude: {my_aircraft.altitude} feet")

if __name__ == "__main__":
    main()