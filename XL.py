from forex_python.converter import CurrencyRates

class Salary:
    def __init__(self, salary, currency):
        self.salary = salary
        self.currency = currency

c = CurrencyRates()
x = Salary

x.salary = input('What is your current monthly salary? ')
x.currency = input('What currency did you introduce your salary in? (ENTER 3 LETTER ABREVIATION): ')

wantedCurrency = input('What currency do you want to convert this to? (ENTER 3 LETTER ABREVIATION): ')

transformedSalary = round(float(x.salary) * c.get_rate(x.currency, wantedCurrency), 2)

print('*************************************************')
print('Your salary is: ' + str(transformedSalary) + ' ' + wantedCurrency + ' per month.')
print('*************************************************')

if(input('Do you want a more detailed analysis of your salary? (Write Y for Yes): ').upper()=='Y'):
    print('*************************************************')
    print('Currently, you are looking at ' + str(transformedSalary) + ' ' + wantedCurrency + ' per month.')
    print('Which averages out at ' + str(round(transformedSalary*12, 2)) + ' ' + wantedCurrency + ' per year.')
    print('It is recommended that you do not take loans for over ' + str(round(transformedSalary * 0.5, 2)) + ' ' + wantedCurrency + ' per month.')
    print('*************************************************')
    input('Press Enter to terminate the application...')
else:
    print('*************************************************')
    input('Press Enter to terminate the application...')

