"""convert gallons to liters"""
#1 setup
LITERS_PER_GALLON = 3.785
#2 input
print('How many gallons?')
gallons = float(input())

#3 transform
liters = gallons * LITERS_PER_GALLON
#4 Output
print(liters)
