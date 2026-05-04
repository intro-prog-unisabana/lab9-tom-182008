import sys
from aircraft import Aircraft

def main():
    
    try:
        model = input("Enter aircraft model: ")
    except EOFError:
        return

    my_aircraft = Aircraft(model)

    while True:
        try:
            user_input = input("Enter command (A for ascent, D for descent, X to exit): ")
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
                    pass
        
        except EOFError:
            break

    print(f"Final altitude: {my_aircraft.altitude} feet")
    
    sys.exit(0)

if __name__ == "__main__":
    main()