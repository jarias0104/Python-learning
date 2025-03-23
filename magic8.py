# Jeshua Nauel Arias Santos
# This exercise consists in creating a program that can reply to yes or no questions with a different answer each time

#here i used the random librarie to import random values to the code
import random


question = input("Question: ")

random_Number = random.randint (1,9)


if question:
     if random_Number == 1:
          print("Yes - definitely.")

     if random_Number == 2:
          print("It is decidedly so.")

     if random_Number == 3:
          print("Without a doubt")

     if random_Number == 4:
          print("Reply hazy, try again.")
     
     if random_Number == 5:
          print("Ask again later.")

     if random_Number == 6:
          print("Better not tell you now.")

     if random_Number == 7:
          print("My sources say no.")

     if random_Number == 8:
          print("Outlook not so good.")

     if random_Number == 9:
          print("Very doubtful.")
