"""Wall Painting"""
##pull in math for cieling function
import math

print('How wide is your wall?')
wallwidth = float(input())

print('How high is your wall?')
wallheight = float(input())

print('How much does paint cost per gallon?')
paintcost = float(input())
#paintcost = 10.50
print('how many coats of paint do you plan on doing?')
coats = int(input())

wallarea = wallwidth * wallheight

print('wallarea = ' + str(int(wallarea)) + ' sq ft')

#400 is the the sq ft value one gallon covers
gallonsneeded = wallarea / 400
print('gallonsneeded = ' + str(float(gallonsneeded)))
print('minimum amount of paint you need'), math.ceil(gallonsneeded)
gallonsneeded = math.ceil(gallonsneeded) * coats
print('gallonsneeded = ' + str(float(gallonsneeded)))


totalcost = gallonsneeded * paintcost
print('your project will cost $' + str(int(totalcost)))
