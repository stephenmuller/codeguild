"""practice/change return"""
#setup
print('How much change to dispense?')
payment = int(input())

quarters = payment // 25
left = payment % 25
dimes = left // 10
left = left % 10
nickels = left // 5
pennies = left % 5
print('Your change will be, ' +
    str(quarters) + ' quarters, ' +
    str(dimes) + ' dimes, ' +
      str(nickels) + ' nickels, and ' +
       str(pennies) + ' pennies.')
