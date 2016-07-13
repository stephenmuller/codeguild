"""Wall Painting"""
# pull in math for cieling function#
import math
# set starting value for wall area so it can be added to
wall_area_sqft = 0
# 1 gallon covers 400sq ft
ONE_GALLON_COVERS = 400 # square feet

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
    wall_width_feet = float(input())

    print('How high is your wall?')
    wall_height_feet = float(input())

    wall_area_sqft += wall_width_feet * wall_height_feet
    walls_to_paint -= 1
    if walls_to_paint >= 1:
        print('and the next wall:')


print('wallarea = ' + str(int(wall_area_sqft)) + ' sq ft')


paint_needed_for_area = wall_area_sqft / ONE_GALLON_COVERS
# print('the number of coats is ' + str(int(coats_of_paint)))
# print('gallonsneeded = ' + str(float(gallons_needed)))

gallons_needed = paint_needed_for_area * coats_of_paint
min_gallons_purchaseable = math.ceil(gallons_needed)


total_cost = min_gallons_purchaseable * paint_cost_dollars
print('your project will cost $' + str(int(total_cost)))
