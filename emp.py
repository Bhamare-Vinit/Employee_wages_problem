'''
@Author: Vinit Bhamare
@Date: 07/05/2024 12:36:30
@Last Modified by: vinit Bhamare
@Last Modified time: 07/05/2024 12:36:30
@Title : To find the Employee wages based on number of hours worked
'''
import random
FULL_DAY_HOUR=8
PART_TIME_HOUR=6
WAGES_PER_HOUR=20
def employee():
    """
    Description: function is used to find the dialy wages of employee
    Parameter:None
    Return:None
    """
    attendance=random.randint(0,2)
    match attendance:
        case 0:
            print("Employee is present!")
            employee_wages=FULL_DAY_HOUR*WAGES_PER_HOUR
            print(f"Today's wage for the employee is: ${employee_wages:.2f}")
        case 2:
            print("Employee is Part time employee!")
            employee_wages=PART_TIME_HOUR*WAGES_PER_HOUR
            print(f"Today's wage for the employee is: ${employee_wages:.2f}")

        case _:
            print("Employee is absent!")
employee()
