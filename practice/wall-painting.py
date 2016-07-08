"""Wall Painting"""
# pull in math for cieling function#
import math
# set wall area to 0#
wallarea = 0

print('How many walls do you plan on painting?')
wallstopaint = int(input())

print('how many coats of paint do you plan on doing?')
coats = int(input())

print('How much does paint cost per gallon?')
paintcost = float(input())

while wallstopaint > 0:
    print('How wide is your wall?')
    wallwidth = float(input())

    print('How high is your wall?')
    wallheight = float(input())
    wallarea = wallwidth * wallheight + wallarea
    wallstopaint = wallstopaint - 1
    if wallstopaint >= 1:
        print('and the next wall:')
        pass
    pass

print('wallarea = ' + str(int(wallarea)) + ' sq ft')

# 400 is the the sq ft value one gallon covers
gallonsneeded = wallarea / 400
print('the number of coats is ' + str(int(coats)))
print('gallonsneeded = ' + str(float(gallonsneeded)))

math.ceil(gallonsneeded)
gallonsneeded = math.ceil(gallonsneeded) * coats
print('gallonsneeded = ' + str(float(gallonsneeded)))


totalcost = gallonsneeded * paintcost
print('your project will cost $' + str(int(totalcost)))
