# -*- coding: utf-8 -*-
"""
created at 3 Feb 2022

calculate how many months it will take you to save up enough money for a down payment."""


#the cost of your dream home total_cost .
# the portion of the cost needed for a down payment portion_down_payment .


annual_salary = float(input("Annual salary: "))
portion_saved = float(input("portion saved: "))
total_cost = float(input("Dream home cost: "))


# you invest your current savings wisely, with an annual return of r
r = 0.04
# amount of salary you save each month 
monthly_salary = annual_salary/12

def calculate_down_payment_months(portion_down_payment = 0.25, r = 0.04):
    """return how many months it will take you to save up enough money for a down payment 
     parameters: optional  
    """
    current_savings = 0
    months = 0
    while (current_savings  < total_cost * portion_down_payment):
        months +=1
        monthly_investment = current_savings*r/12
        monthly_salary_saved = portion_saved * monthly_salary 
        # total savings in current month
        current_savings += monthly_investment + monthly_salary_saved
        print(current_savings)
    return months

    

print(calculate_down_payment_months())
