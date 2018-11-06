
#Clay Kynor and Glen Passow
#11.17.18
#CalculusProject.py

d = int(input('Please enter what type of function you have: 1. polynomial '))

if d == 1:
    n = int(input('Enter the highest degree in your polynomial: '))
    for i in range (0,n):
        a = int(input('Please enter the coefficient of the ' + str(i) + ' term '))
        