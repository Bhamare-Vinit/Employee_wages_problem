import random
'''
@Author: Vinit Bhamare
@Date: 07/05/2024 02:10:30
@Title : To find the monthly wages of employees till a condition of total working hours or days is reached using class
'''
PER_HR_WAGE=20
class employee:
    def __init__(self,name,max_days,max_hours):
        self.name=name
        self.max_days=max_days
        self.max_hours=max_hours

    def employee_monthly_wage (self):
        """
        Description: function is used to find the monthly wages of employees till a condition of total working hours or days is reached using class
        Parameter:None
        Return: {total_monthly_wage} total monthly wages of employee
        """

        full_day = 0
        part_time = 0
        absent = 0
        total_hours=0
        i = 1 
        while i <= self.max_days :
            work = random.choice([ 0,1, 2])
            if work == 0:
                absent += 1

            elif work == 1:
                full_day += 1
                total_hours+=8

            else:
                part_time += 1
                total_hours+=4
            if total_hours>=self.max_hours:
                break
            i += 1
        full_day_wage = full_day * 8 * PER_HR_WAGE
        half_day_wage = part_time * 4 * PER_HR_WAGE
        total_days=full_day+part_time
        absent_wage =  0
        total_monthly_wage = full_day_wage + half_day_wage + absent_wage
        return print(f"At {self.name}, the employee worked for {total_hours} hours over {total_days} days, earning a monthly wage of ${total_monthly_wage:.2f}.")
company_name=input("Enter the name of company: ")
max_days=int(input("Enter the Maximum working days: "))
max_hours=int(input("Enter maximum number of hours employee can work: "))
emp=employee(company_name,max_days,max_hours)
emp.employee_monthly_wage()

            