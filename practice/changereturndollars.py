"""practice/change return with dollars"""
#setup
print('How much change to dispense?')
payment = float(input())

dollars = payment // 1
print(str(payment))
cents = payment - dollars

hundreds = dollars // 100
dollars = dollars % 100
fifties = dollars // 50
dollars = dollars % 50
twenties = dollars // 20
dollars = dollars % 20
tens = dollars // 10
dollars = dollars % 10
fives = dollars // 5
ones = dollars % 5



quarters = cents // 25
left = cents % 25
dimes = left // 10
left = left % 10
nickels = left // 5
pennies = left % 5
print('Your change will be, ' +
    str(int(hundreds)) + ' hundreds ' +
    str(int(fifties)) + ' fifties ' +
    str(int(twenties)) + ' twenties ' +
    str(int(tens)) + ' tens ' +
    str(int(fives)) + ' fives ' +
    str(int(ones)) + ' ones ' +
    str(int(quarters)) + ' quarters, ' +
    str(int(dimes)) + ' dimes, ' +
      str(int(nickels)) + ' nickels, and ' +
       str(int(pennies)) + ' pennies.')
