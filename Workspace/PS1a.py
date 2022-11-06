annual_salary = float(input('What is your annual salary: '))
portion_saved = float(input('Portion you want to save: '))
total_costs = float(input('Enter your total costs: ' ))

if portion_saved > 1:
    portion_saved = portion_saved/100

portion_down_payment = 0.25
current_savings = 0
r = 0.04
num_months = 0

while current_savings < (portion_down_payment*total_costs):
    current_savings *= (1+(r/12))
    current_savings += ((annual_salary*portion_saved)/12)
    num_months += 1

print()
print(num_months)