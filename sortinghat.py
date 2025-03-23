answer1 = int(input("Q1) Do you like Dawn or Dusk? 1) Dawn, 2) Dusk: "))

# Initialize house scores
ravenclaw = 0
gryffindor = 0
hufflepuff = 0
slytherin = 0

# Question 1
if answer1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer1 == 2:
    hufflepuff += 1
    slytherin += 1

# Question 2
answer2 = int(input("Q2) When I'm dead, I want people to remember me as:\n"
                    "1) The good  2) The great  3) The wise  4) The bold: "))

if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin += 2
elif answer2 == 3:
    ravenclaw += 2
elif answer2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# Question 3
answer3 = int(input("Q3) Which kind of instrument most pleases your ear?\n"
                    "1) The violin  2) The trumpet  3) The piano  4) The drum: "))

if answer3 == 1:
    slytherin += 4
elif answer3 == 2:
    hufflepuff += 4
elif answer3 == 3:
    ravenclaw += 4
elif answer3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")

# Print final house scores
print("Scores:")
print(f"Gryffindor: {gryffindor}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Slytherin: {slytherin}")
