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
coats_of_paint = int(input())

print('How much does paint cost per gallon?')
paint_cost_dollars = float(input())

# add additional walls
while walls_to_paint > 0:
    print('How wide is your wall?')
    wall_width = float(input())

    print('How high is your wall?')
    wall_height = float(input())

    wall_area = wall_width * wall_height + wall_area
    walls_to_paint -= 1
    if walls_to_paint >= 1:
        print('and the next wall:')


print('wallarea = ' + str(int(wall_area)) + ' sq ft')


gallons_needed = wall_area / ONE_GALLON_AREA
print('the number of coats is ' + str(int(coats_of_paint)))
print('gallonsneeded = ' + str(float(gallons_needed)))

gallons_needed = gallons_needed * coats_of_paint
gallons_needed = math.ceil(gallons_needed)
print('gallonsneeded = ' + str(float(gallons_needed)))


total_cost = gallons_needed * paint_cost_dollars
print('your project will cost $' + str(int(total_cost)))
