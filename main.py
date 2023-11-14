import json
import os 
import tempfile

#Manual

def manual():
    print("\nWelcome to flash cards game!")
    print("\nType answer under every question. Correct answers will give you 1 point.")
    print("\nIf you need any help type ':help'. If you want to exit the game type ':quit'.\n")

#Loading Json File

question = json.load(open('data.json'))

tf = tempfile.TemporaryFile()

def game():
    user_score = 0
    os.system('cls')

    for x in range(len(question)):
        print(f"\nQuestion number: {x+1}")
        print("Your score: " + str(user_score))
        print(f"{question[x].get('question')}")
              
        answer = input("Odpowiedź: ")

        if(answer == ":help"):
            print("\nType answer under every question. Correct answers will give you 1 point.")
        elif(answer == ":quit"):
            print("Thanks for playing the game! See you next time!")
            break;
        elif(answer == question[x].get('answer')):
            os.system('cls')
            user_score = user_score +1
        elif(answer !=question[x].get('answer')):
            with tempfile.NamedTemporaryFile(mode='w') as temp_file:
                temp_file.write("To są moje dane tymczasowe!")
            os.system('cls')

    print(f"Your score is: {user_score}/{x} ")   
    print(tf.print())

game()
