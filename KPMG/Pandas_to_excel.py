import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel('./MyExcel.xlsx', sheet_name='Datasheet_RawData')

print(x)

x['BMI'] = round(x['Weight']/ (x['Height']/100)**2,1)

with pd.ExcelWriter('Solution.xlsx') as writer:
    x.to_excel(writer, sheet_name = 'Data_BMI')

Namen = x['Name']
BMI = x['BMI']

plt.bar(Namen, BMI)
plt.axhline(y = 25, color = 'r', linestyle = '-')

plt.title('Wer muss abspecken?')
plt.xlabel('Name')
plt.ylabel('BMI')

plt.show()
