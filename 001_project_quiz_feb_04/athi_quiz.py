from datetime import datetime

#Global variables
'''
Vairables store data
e.g x = 1, x stores the value 1
e.g2 Oratile = 2010, the variable Oratile stores the value 2010
'''
name = ""
surname = ""
age = ""
school = ""
meal = ""
points = ""

instructions = "\n*************************************************************\
 \nHello nana! Please press enter after typing in your answer to confirm. Always.\
  \n****************************************************************************"

def get_details():
    print(f"{datetime.utcnow()} {instructions}")
    name = input("Hello enter your name: ")
    surname = input(f"Please nter your surname {name}: ")
    age = input(f"What is your age {name} {surname}: ")
    return print(f"Good now that we have all your details {name}, lets dive into the quiz.")

def start_quiz():
    score_points = 0
    answer_1 = input("Who was the first South African democratically elected president ? (2 points)\n")
    if answer_1 == "Nelson Mandela" or answer_1 == "nelson mandela":
        score_points = 2

    answer_2 = input("When is the commemoration of the youth of 1976, mention day and month e.g (11-April) (5 points) \n")
    if answer_2 == "16-June" or answer_2 == "16-june":
        score_points = score_points + 5

    answer_0 = input("Is eleven (11) and odd number? e.g (Yes or No) (5 points) \n")
    if answer_0 == "yes":
        score_points = score_points + 5

    answer_3 = input("How many siblings does Dineo have ? (3 points)\n")
    if answer_3 == "2":
        score_points = score_points + 3

    answer_4 = input("Why dont you play any sports at school? (0 points)\n")
    print(f"mmmmmh okay....")

    answer_5 = input("What do you want to be when you grow up? (0 points)\n")

    answer_6 = input("Which subjects will you have to take in High School in order to achieve your goal?\
     (General Stream, Science Stream, Technical Science Stream, Commerce Stream) \n")

    return print(f"You scored {score_points} points. Hooray nana {name}. Now change change this code. Make it fun for Rati.\n \
    run this script with : python3 athi_quiz.py to retry this quiz.")

if __name__ == "__main__":
    get_details()
    start_quiz()
