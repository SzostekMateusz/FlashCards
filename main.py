import json
import os 

print("\nWelcome to flash cards game!")
print("\nType answer under every question. Correct answers will give you 1 point.")
print("\nIf you need any help type ':help'. If you want to exit the game type ':quit'.\n")
# val = input("Input data: \n")

# if val == ":help":
#     print("\nType answer under every question. Correct answers will give you 1 point.")
# elif val == ":quit":
#     print("Thanks for playing the game! See you next time!")
# else:
#     print("else")
answer1 = "Mateusz"
answer2 = "Warszawa"



# while True:
#     user_answer = input("What is your name: ")
#     if user_answer == answer1:
#         print("You guessed correcctly")
#         score =+1
#         print("Your score is: " + str(score))

#     else: 
#         print("That's wrong answer. Try again")
#         break
score = 0

with open("data.json") as file:
    data = json.load(file)

i = 0
question_counter = 0

for i in data:
    print(data[question_counter])
    score +=1
    question_counter +=1
    print(score)
    
#       Cleaning the terminal
#os.system("cls")


