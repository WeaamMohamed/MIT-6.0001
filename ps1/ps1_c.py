"""
created at 4 Feb 2022
 a particular goal, e.g. to be able to afford the down payment in three years.
 How much should you save each month to achieve this?
 
You are now going to try to find the best rate of savings to achieve a down payment 
on a $1M house in 36 months.

Using bisection search 
 """



@the problem of starting with middle of high and low 
#annual_salary = float(input("Annual salary: "))
annual_salary = 10000
#portion_saved = float(input("portion saved: "))



total_cost = 1000000

def bisection_search_portion_payment(original_annual_salary, semi_annual_raise = .07,portion_down_payment = 0.25, r = 0.04 ):
    ''' to calculate the best portion saved in 36 months '''

    bisection_steps = 0
    epsilon = 100
    semi_annual_raise = .07
    high_portion_saved = 10000
    low_portion_saved = 0
    int_best_portion_saved = high_portion_saved

    while True: 
        #print(high_portion_saved, low_portion_saved)

        bisection_steps +=1

        annual_salary = original_annual_salary
        current_savings = 0.0
        #int_best_portion_saved = (high_portion_saved + low_portion_saved) //2
        best_portion_saved = (int_best_portion_saved) /10000
        
        #print("best_portion_saved:",best_portion_saved)


        months = 0
        monthly_investment = current_savings*r/12

        while (months <= 36):
            #to update annual salary after semi annual raise
            if(months % 6 == 0 and months != 0): 
                annual_salary = calculate_semi_annual_raise(annual_salary,semi_annual_raise)


            monthly_salary = annual_salary/12

            monthly_salary_saved = best_portion_saved * monthly_salary 
            # total savings in current month
            current_savings += monthly_investment + monthly_salary_saved
            months +=1
            
        required_payment =  (portion_down_payment * total_cost)
        
        if(abs(current_savings -required_payment) <= epsilon):
            print("bisection step:", bisection_steps)
            print("done: ", best_portion_saved)
            break
        
        if(current_savings < required_payment):
            low_portion_saved = int_best_portion_saved
        else:
            high_portion_saved = int_best_portion_saved
            
        
        if(low_portion_saved >= high_portion_saved):
            print("It is not possible to pay the down payment in three years.")
            break  
        int_best_portion_saved = (high_portion_saved + low_portion_saved)//2
        best_portion_saved = int_best_portion_saved /10000


        print("bisection steps",bisection_steps)
        print("bisection high",high_portion_saved)
        print("bisection low",low_portion_saved)



        




def calculate_semi_annual_raise(annual_salary, semi_annual_raise):
    """return the monthly salary after semi annual raise
    parameters: 
        1. annual_salary
        2. semi_annual_raise: float"""
        
    return annual_salary + (annual_salary * semi_annual_raise)
    
    


bisection_search_portion_payment(annual_salary)
