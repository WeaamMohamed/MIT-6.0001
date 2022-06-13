# -*- coding: utf-8 -*-
"""
created at 4 Feb 2022
calculate how many months it will take you to save up enough money for a down payment.
   with raise every six months."""


#the cost of your dream home total_cost .
# the portion of the cost needed for a down payment portion_down_payment .


annual_salary = float(input("Annual salary: "))
portion_saved = float(input("portion saved: "))
total_cost = float(input("Dream home cost: "))
semi_annual_raise =  float(input("semi annual raise: "))



def calculate_down_payment_months(annual_salary,portion_down_payment = 0.25, r = 0.04):
    """return how many months it will take you to save up enough money for a down payment 
     parameters: optional  
     1. portion_down_payment: float
     2. r: an annual return of r, float
     
    """
    current_savings = 0
    months = 0
    while (current_savings  < total_cost * portion_down_payment):
        
        
        #to update annual salary after semi annual raise
        if(months % 6 == 0 and months != 0): 
            annual_salary = calculate_semi_annual_raise(annual_salary,semi_annual_raise)
            print(months, "-->", annual_salary )


        monthly_salary = annual_salary/12

        monthly_investment = current_savings*r/12
        monthly_salary_saved = portion_saved * monthly_salary 
        # total savings in current month
        current_savings += monthly_investment + monthly_salary_saved
        months +=1

        #print(current_savings)
    return months




def calculate_semi_annual_raise(annual_salary, semi_annual_raise):
    """return the monthly salary after semi annual raise
    parameters: 
        1. annual_salary
        2. semi_annual_raise: float"""
        
    print("calculate_semi_annual_raise is invoked")
    return annual_salary + (annual_salary * semi_annual_raise)
    
    


print(calculate_down_payment_months(annual_salary))
