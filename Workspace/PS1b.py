annual_salary = float(input('What is your annual salary: '))
semi_annual_raise = float(input('Enter your semi annual raise: '))
portion_saved = float(input('Portion you want to save: '))
total_costs = float(input('Enter your total costs: ' ))

if portion_saved > 1:
    portion_saved = portion_saved/100

if semi_annual_raise > 1:
    semi_annual_raise = semi_annual_raise/100

semi_annual_salary = annual_salary/2
portion_down_payment = 0.25
current_savings = float(0)
r = 0.04
num_months = 0

while current_savings < (portion_down_payment*total_costs):
    if num_months == 0:
        current_savings *= (1 + (r / 12))
        current_savings += ((semi_annual_salary * portion_saved)) / 6
    elif num_months%6 == 0:
        semi_annual_salary *= (1+semi_annual_raise)
        current_savings *= (1 + (r / 12))
        current_savings += ((semi_annual_salary * portion_saved)) / 6
    else:
        current_savings *= (1 + (r / 12))
        current_savings += ((semi_annual_salary * portion_saved)) / 6
    num_months += 1

print()
print(num_months)