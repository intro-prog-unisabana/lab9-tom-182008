# TODO: Import modules
from car import Car
import car_utils

def main():
    cars = {}  # Dictionary to store cars with car_id as key and car objects as values

    while True:
        print("\nMenu:")
        print("1. Add a new car")
        print("2. View all cars")
        print("3. Drive a car")
        print("4. Paint a car")
        print("5. Exit")

        choice = input("Choose an option:\n")

        if choice == '1':
            # Call the appropriate function from utils.py to create the car
            new_car = car_utils.create_car_from_input()
            # Add it to the dictionary
            cars[new_car.car_id] = new_car
            # Print the car
            print(new_car)
            print("Car added.")

        elif choice == '2':
            # Call the appropriate function from utils.py to display all the cars
            car_utils.display_cars(cars)

        elif choice == '3':
            car_id = input("Enter the car ID to drive:\n")
            miles = float(input("How many miles to drive?\n"))
            # Look up the car in the dictionary
            if car_id in cars:
                # Call the appropriate class method to increase the mileage
                cars[car_id].drive(miles)
                print("Mileage updated.")
                # Print the car
                print(cars[car_id])
            else:
                print("Car not found.")
          
        elif choice == '4':
            car_id = input("Enter the car ID to paint:\n")
            new_color = input("Enter the new color:\n")
            # Look up the car in the dictionary
            if car_id in cars:
                # Call the appropriate class method to change the color
                cars[car_id].change_color(new_color)
                print("Color updated.")
                # Print the car
                print(cars[car_id])
            else:
                print("Car not found.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
