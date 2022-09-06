# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# DNR,9/1/2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
from DataClasses import Employee as Emp
from ProcessingClasses import FileProcessor as FP
from IOClasses import EmployeeIO as EIO

#Global variables
lstEmployees = []
strFileName='EmployeeData.txt'

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts

#Read data from file
tableEmployees=FP.read_data_from_file(strFileName)
#Clear the global list (safety check)
lstEmployees.clear()
#Load the contents into the table as new Employee objects
for line in tableEmployees:
    lstEmployees.append(Emp(line[0], line[1], line[2].strip()))

# Show user a menu of options
while(True):
    EIO.print_menu_items()

# Get user's menu option choice
    strChoice = EIO.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice == "1":
        EIO.print_current_list_items(lstEmployees)
        continue

    # Let user add data to the list of employee objects
    elif strChoice == "2":
        tempEmp = EIO.input_employee_data()
        #Check that the ID is a number
        if tempEmp.employee_id.isnumeric():
            #Check that the first and last name are a-z characters
            if (tempEmp.first_name.isalpha() and 
                tempEmp.last_name.isalpha()):
                    #All conditions checked; add employee to list
                    lstEmployees.append(tempEmp)
                    print("Added Employee "+tempEmp.first_name+" "+tempEmp.last_name
                    +" to the list.\n")
            #Failed the a-z character check
            else:
                print("First name and last name must contains letters only.")
                print("Employee not added.\n")
        #Failed the ID is numeric check
        else:
            print("The ID entered was not numeric; employee not added.\n")
        continue

    # let user save current data to file
    elif strChoice == "3":
        #save the file and capture if it succeeded or failed
        boolSuccess=FP.save_data_to_file(strFileName,lstEmployees)
        #Success...print confirmation
        if boolSuccess:
            print("Data has been saved to "+strFileName)
            print()
        #Failed...print it
        else:
            print("Something went wrong. Data was not saved.\n")
        continue

    # Let user exit program
    elif strChoice == "4":
        print("Now exiting...")
        break

    #Wrong choice input validation
    else:
        print("Wrong choice. Try again")

# Main Body of Script  ---------------------------------------------------- #
