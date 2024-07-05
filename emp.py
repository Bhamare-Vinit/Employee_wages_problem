import random
'''
@Author: Vinit Bhamare
@Date: 07/05/2024 12:50:30
@Title : To find the monthly wages of employees
'''
PER_HR_WAGE=20
def employee_monthly_wage ():
    """
    Description: function is used to find the monthly wages of employees
    Parameter:None
    Return:None
    """
    full_day = 0
    part_time = 0
    absent = 0
    i = 1 
    while i <= 20:
        work = random.choice([0, 1, 2])
        if work == 0:
            absent += 1
        elif work == 1:
            full_day += 1
        else:
            part_time += 1
        i += 1
    full_day_wage = full_day * 8 * PER_HR_WAGE
    half_day_wage = part_time * 4 * PER_HR_WAGE
    absent_wage =  0
    total_monthly_wage = full_day_wage + half_day_wage + absent_wage
    
    return print(f"The Mothly Wage of the employee is : {total_monthly_wage:.2f}")


employee_monthly_wage()
            