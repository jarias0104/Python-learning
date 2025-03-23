# Jeshua Nauel Arias Santos
# This code need to calculate the PH Level by saying if its basic, acidic or neutral

ph = int (input("Enter a value between 0-14.." ))

#This if statement prevents the user to go above of the variable range displaying a message that the input exceeds the value that wwas asked
if ph > 14:
 print("Enter a lower value!")

if ph > 7:
 print("pH level is Basic!")

elif ph < 7:
 print("pH level is Acidic!")

else: print("pH level is Neutral!")