# Description: Driver Financial Listing Report
# Author: Kass Fequet
# Date(s): April 10/24


# Define required libraries.
import datetime as DT
import FormatValues as FV


# Define program constants.



# Define program functions.
HST = .15# HST tax rate

TransIDLst = []
TransDateLst = []
DescLst = []
SubtotalLst = []
HSTAmtLst = []
TotalLst = []

# Main program starts here.
while True:
    
    # Gather user inputs.
    while True:
        print()
        EmpNum = input("Enter the employee number: ")
        if EmpNum == "":
            print()
            print("   Data Entry Error - Employee number cannot be blank.")
            print()
        if EmpNum.isdigit() == False:
            print()
            print("   Data Entry Error - Employee number must be numeric.")
            print()
        else:
            break
    
    while True:
        EmpName = input("Enter the employee name: ")
        if EmpName == "":
            print()
            print("   Data Entry Error - Employee Name cannot be blank.")
            print()
        else:
            break
        
    while True:
        StartDate = input("Enter the start date (YYYY-MM-DD): ")
        if StartDate == "":
            print()
            print("   Data Entry Error - Start date cannot be blank.")
            print()
        else:
            try:
                StartDate = DT.datetime.strptime(StartDate, "%Y-%m-%d").date()
                break
            except ValueError:
                print()
                print("   Data Entry Error - Start date must be in YYYY-MM-DD format.")
                print()
                
    while True:
        EndDate = input("Enter the end date (YYYY-MM-DD): ")
        if EndDate == "":
            print()
            print("   Data Entry Error - End date cannot be blank.")
            print()
        else:
            try:
                EndDate = DT.datetime.strptime(EndDate, "%Y-%m-%d").date()
                break
            except ValueError:
                print()
                print("   Data Entry Error - End date must be in YYYY-MM-DD format.")
                print()
                

    # Prompt for transaction details
    while True:
        print()
        TransID = input("Enter the transaction ID number (###): ")
        if TransID.isdigit() and len(TransID) == 3:
            TransIDLst.append(TransID)
            break
        else:
            print()
            print("   Data Entry Error - Please enter a 3-digit number.")
            print()

    while True:
        TransDate = input("Enter the transaction date (YYYY-MM-DD): ")
        try:
            TransDate = DT.datetime.strptime(TransDate, "%Y-%m-%d").date()
            TransDateLst.append(TransDate)
            break
        except ValueError:
            print()
            print("   Data Entry Error - Please enter the date as YYYY-MM-DD.")
            print()

    while True:
        Desc = input("Enter a brief description of the transaction (max 25 characters): ")
        if Desc == "":
            print()
            print("   Data Entry Error - Description cannot be blank.")
            print()
        elif len(Desc) > 25:
            print()
            print("   Data Entry Error - Description must be 25 characters or less.")
            print()
        else:
            DescLst.append(Desc)
            break

    while True:
        Subtotal = input("Enter the transaction amount: ")
        try:
            Subtotal = float(Subtotal)
            SubtotalLst.append(Subtotal)
            break
        except ValueError:
            print()
            print("   Data Entry Error - Amount must be numeric.")
            print()




    # Perform required calculations.
    HSTAmt = Subtotal * HST
    Total = Subtotal + HSTAmt
    HSTAmtLst.append(HSTAmt)
    TotalLst.append(Total)


    # Display results
    print()
    print(f"HAB Taxi Services                                         Employee Name: {EmpName:>25s}")
    print(f"                                                          Employee Number:                    {EmpNum:<3s}")
    print(f"                                                          Start Date:                     {StartDate}")
    print(f"Driver Financial Listing Report                           End Date:                       {EndDate}")
    print()
    print(f"Transaction ID   Transaction Date         Description	           Subtotal      HST        Total")
    print(f"==================================================================================================")

    # Loop through the lists and print each claim's details
    for i in range(len(TransIDLst)):
        print(f"      {TransIDLst[i]:3s}             {TransDateLst[i]:<10s}         {DescLst[i]:<25s}      {FV.FDollar2(SubtotalLst[i]):>8s}   {FV.FDollar2(SubtotalLst[i]):>8s}   {FV.FDollar2(SubtotalLst[i]):>8s}")

    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program