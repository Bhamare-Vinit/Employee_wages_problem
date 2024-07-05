
import random
FULL_DAY_HOUR=8
WAGES_PER_HOUR=20
def employee():
    attendance=random.randint(0,1)
    if attendance == 0:
        print("Employee is present!")
        employee_wages=FULL_DAY_HOUR*WAGES_PER_HOUR
        print(f"Today's wage for the employee is: ${employee_wages:.2f}")
    else:
        print("Employee is absent!")
employee()
