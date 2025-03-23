#Jeshua Arias Santos 
#Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

#Use a combination of relational and logical operators to create the rules:

#If they are tall enough and have enough credits, print "Enjoy the ride!"
#Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
#Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."


height = int(input("Enter a height in cm: "))

credits = int(input("Enter your credits: "))

if height >= 160 and credits >= 10:
  print("Enjoy the ride")

elif credits >= 10 and height < 160:
  print("You are not tall enough to ride")

elif height >= 160 and credits < 10:
  print("You don't have enough credits")

else: print ("You don't met either requirement")
