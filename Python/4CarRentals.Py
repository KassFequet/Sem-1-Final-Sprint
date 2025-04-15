# Description: Track Car Rentals
# Author: Kass Fequet
# Date(s): April 14/24

# Define required libraries.
import datetime as DT
import FormatValues as FV
import os
from datetime import datetime, timedelta

# Define program constants.

#Define program functions.

# Function to check if a car is occupied
def is_car_occupied(car_num):
    car_file = f"Car{car_num}.dat"
    if os.path.exists(car_file):
        with open(car_file, "r") as file:
            for line in file:
                # Check if the car has an active rental
                return True  # Assume occupied if there's any data
    return False

# Function to check if a car is occupied for the given rental period
def is_car_occupied(car_num, start_date, num_days):
    car_file = f"Car{car_num}.dat"
    if not os.path.exists(car_file):
        return False  # If the file doesn't exist, the car is not occupied

    # Calculate the rental period
    rental_dates = set(
        (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range(num_days)
    )

    # Check for conflicts in the car's file
    with open(car_file, "r") as file:
        for line in file:
            # Assume the file format is: RentalID, StartDate, RentalDur, NumDays, RentCost, HSTRate, Total
            _, existing_start_date, _, existing_num_days, *_ = line.strip().split(", ")
            existing_start_date = datetime.strptime(existing_start_date, "%Y-%m-%d").date()
            existing_num_days = int(existing_num_days)

            # Calculate the existing rental period
            existing_rental_dates = set(
                (existing_start_date + timedelta(days=i)).strftime("%Y-%m-%d")
                for i in range(existing_num_days)
            )

            # Check for overlap
            if rental_dates & existing_rental_dates:
                return True  # Conflict found

    return False  # No conflict

# Open the data file.
f = open("Defaults.dat", "r")

# Initialize variables to store default values
NextTransNum = 0
TransID = 0
EmpNum = 0
HST = 0.0


# Define data storage lists.


# Open the data file.
f = open("Defaults.dat", "r")

# Process each line (record) in the file in a loop.
for XRecord in f:

    # The following line reads the first record in the file and creates a list.
    XLst = XRecord.split(",")

    # Now grab the values from the list and assign to variables.
    # You may not need all the fields.
    TransNum = int(XLst[0].strip())
    EmpNum = int(XLst[1].strip())
    MonthStandFee = float(XLst[2].strip())
    DayRentFee = float(XLst[3].strip())
    WeekRentFee = float(XLst[4].strip())
    HST = float(XLst[5].strip())
    
    



# Open the Rentals.dat file in append mode to save rental information
rentals_file = open("Rentals.dat", "a")

# Main program starts here.
while True:
    # Gather user inputs for employee details and report dates.

    while True:
        RentalID = input("Enter the rental ID: ")
        if RentalID == "":
            print()
            print("   Data Entry Error - Rental ID cannot be blank.")
            print()
        else:
            break

    while True:
        StartDate = input("Enter the start date of the rental (YYYY-MM-DD): ")
        if StartDate == "":
            print()
            print("   Data Entry Error - Start date cannot be blank.")
            print()
        else:
            try:
                StartDate = DT.datetime.strptime(StartDate, "%Y-%m-%d").date()
                if StartDate > DT.date.today():
                    print()
                    print("   Data Entry Error - Start date cannot be in the future.")
                    print()
                else:
                    break
            except ValueError:
                print()
                print("   Data Entry Error - Start date must be in YYYY-MM-DD format.")
                print()

    while True:
        CarNum = input("Enter the car number (1, 2, 3, or 4): ")
        if CarNum == "":
            print()
            print("   Data Entry Error - Car number cannot be blank.")
            print()
        elif CarNum not in ["1", "2", "3", "4"]:
            print()
            print("   Data Entry Error - Car number must be 1, 2, 3, or 4.")
            print()
        elif is_car_occupied(CarNum, StartDate, NumDays):
            print()
            print(f"   Car {CarNum} is currently occupied. Please choose another car.")
            print()
        else:
            break

    while True:
        RentalDur = input("Enter if the rental is for a day or a week (D/W): ").upper()
        if RentalDur == "":
            print()
            print("   Data Entry Error - Rental duration cannot be blank.")
            print()
        elif RentalDur not in ["D", "W"]:
            print()
            print("   Data Entry Error - Rental duration must be D or W.")
            print()
        elif RentalDur == "W":
            RentalDur = "Week"
            NumDays = 7
            break
        elif RentalDur == "D":
            RentalDur = "Day"
            while True:
                NumDays = input("Enter the number of days the car is rented for: ")
                if NumDays == "":
                    print()
                    print("   Data Entry Error - Number of days cannot be blank.")
                    print()
                elif not NumDays.isdigit():
                    print()
                    print("   Data Entry Error - Number of days must be a number.")
                    print()
                else:
                    NumDays = int(NumDays)
                    break
            break

    while True:
        RentCost = input("Enter the rental cost: ")
        if RentCost == "":
            print()
            print("   Data Entry Error - Rental cost cannot be blank.")
            print()
        elif not RentCost.replace('.', '', 1).isdigit():
            print()
            print("   Data Entry Error - Rental cost must be a number.")
            print()
        else:
            RentCost = float(RentCost)
            break

    HSTRate = RentCost * HST
    Total = RentCost + HSTRate

    # Save the rental information to the specific car file
    car_file = f"Car{CarNum}.dat"
    with open(car_file, "a") as file:
        file.write(f"{RentalID}, {StartDate}, {RentalDur}, {NumDays}, {RentCost:.2f}, {HSTRate:.2f}, {Total:.2f}\n")

    print(f"\nRental saved: RentalID={RentalID}, StartDate={StartDate}, CarNum={CarNum}, RentalDur={RentalDur}, NumDays={NumDays}, RentCost={RentCost:.2f}, HST={HSTRate:.2f}, Total={Total:.2f}\n")

    Continue = input("Would you like to input another transaction? (Y/N): ").upper()
    if Continue == "N":
        break
    elif Continue != "Y":
        print()
        print("   Data Entry Error - Please enter Y or N.")
        print()

# Close the Rentals.dat file
rentals_file.close()

# Any housekeeping duties at the end of the program

# Save updated defaults to Defaults.dat
f = open("Defaults.dat", "w")

f.write(f"{TransNum}, {EmpNum}, {MonthStandFee}, {DayRentFee}, {WeekRentFee}, {HST}\n")  # Write all values on the same line, separated by commas
f.close()  # Close the file after writing