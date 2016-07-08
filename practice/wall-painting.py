"""Wall Painting"""
# pull in math for cieling function#
import math
# set wall area to 0#
wall_area = 0
# 1 gallon covers 400sq ft
ONE_GALLON_AREA = 400 # square feet

# establish the user data
print('How many walls do you plan on painting?')
walls_to_paint = int(input())
print('how many coats of paint do you plan on doing?')
coats = int(input())
print('How much does paint cost per gallon?')
paint_cost = float(input())

while walls_to_paint > 0:
    print('How wide is your wall?')
    wall_width = float(input())
    print('How high is your wall?')
    wall_height = float(input())
    wall_area = wall_width * wall_height + wall_area
    walls_to_paint = walls_to_paint - 1
    if walls_to_paint >= 1:
        print('and the next wall:')
        pass
    pass

print('wallarea = ' + str(int(wall_area)) + ' sq ft')

# 400 is the the sq ft value one gallon covers
gallons_needed = wall_area / ONE_GALLON_AREA
print('the number of coats is ' + str(int(coats)))
print('gallonsneeded = ' + str(float(gallons_needed)))

gallons_needed = gallons_needed * coats
gallons_needed = math.ceil(gallons_needed)
print('gallonsneeded = ' + str(float(gallons_needed)))


total_cost = gallons_needed * paint_cost
print('your project will cost $' + str(int(total_cost)))


# it's calculating the amount of paint vs
