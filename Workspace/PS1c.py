annual_salary = float(input('What is your annual salary: '))

total_costs = 1000000
semi_annual_raise = 0.07
semi_annual_salary = annual_salary/2
portion_down_payment = 250000
r = 0.04

steps = 0
epsilon = 100
low = 0
high = 10000
current_savings = 0
savings_rate = int(round((high + low) / 2)) # bisection search variable ist savings_rate


while abs(current_savings-portion_down_payment) > epsilon: # absolut savings - 250000 > 100 solange bis < 100
    steps +=1
    current_savings = 0
    monthly_salary = annual_salary/12
    for number_months in range(36): #3 years
        if number_months == 0:
            current_savings *= (1 + (r / 12))
            current_savings += monthly_salary * savings_rate/10000  # bisection search variable / high
        elif number_months%6 == 0: # halbjährliche Gehaltssteigerung
            current_savings *= (1 + (r / 12))
            monthly_salary *= (1 + semi_annual_raise)
            current_savings += monthly_salary * savings_rate / 10000
        else:
            current_savings *= (1 + (r / 12))
            current_savings += monthly_salary * savings_rate / 10000
    if current_savings < portion_down_payment:
        low = savings_rate
    else:
        high = savings_rate
    prev_savings_rate = savings_rate
    savings_rate = int(round((high + low) / 2))
    if prev_savings_rate == savings_rate:
        break

if prev_savings_rate == savings_rate and savings_rate == 10000:
    print(' Is is not Possible to pay the down payment in 3 years')
else:
    print('optimal savings rate: ', savings_rate/10000)
    print('steps bisection search: ', steps)
    print('current_savings: ', current_savings)