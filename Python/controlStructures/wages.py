# ================= BONUS Optional Task ==================
# Create a Python file called “Optional_task.py” in this folder.
# Design a program for a department store to calculate the monthly wage for two different types of employees.
# Employees can either be a salesperson or a manager.
# Salespeople earn a 8% commission on their gross sales and a fixed salary of R2000.00 per month. 
# Managers earn an hourly rate of R40.00.
# Determine if the user is a salesperson or a manager.
# Then, depending on their answer, calculate the monthly wage for the employee.
# If the user is a salesperson ask for their gross sales for the month.
# If the user is a manager ask for the number of hours worked for the month.
# Display the total monthly wage for the employee. 

employeeType = input("Are you a Salesman or Manager?:  Salesman/Manager:  ")
salesCommission = 0
managerHours = 0
salesWage = (2000.00 + salesCommission)

if employeeType == "Manager":
    managerHours = input("how many hours have you worked this month?:  ")
    managerWage = (40.00 * float(managerHours))
    print("Your Manager wage this month is: R" + str(managerWage))
else:
    grossSales = input("Please enter your gross sales for the month:  R")
    salesWage = (float(grossSales) * 0.08) + 2000
    print("Your Sales Wage for the month is:  R" + str(salesWage))
