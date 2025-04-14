# Description: Track Car Rentals
# Author: Kass Fequet
# Date(s): April 14/24

# Define required libraries.
import datetime as DT
import FormatValues as FV

# Define program constants.

#Define program functions.

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


# Main program starts here.
while True:
    # Gather user inputs for employee details and report dates.

    while True:
        RentalID = input("Enter the rental ID: ")
        if RentalID == "":
            print()
            print("   Data Entry Error - Employee Name cannot be blank.")
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
        RentalID = input("Enter the rental ID: ")
        if RentalID == "":
            print()
            print("   Data Entry Error - Employee Name cannot be blank.")
            print()
        else:
            break


# Any housekeeping duties at the end of the program

# Save updated defaults to Defaults.dat
f = open("Defaults.dat", "w")
f.write(f"{TransNum}, {EmpNum}, {MonthStandFee}, {DayRentFee}, {WeekRentFee}, {HST}\n")  # Write all values on the same line, separated by commas
f.close()  # Close the file after writing