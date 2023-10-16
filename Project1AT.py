# Project1.py
# Author: Ayisha Taher 


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.
points = 0
user_name = input("What is your name? ")
print("Hello " + user_name + "!")
# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome_message():
    print("Welcome to the quiz game! You will be asked a series of questions and you will have to answer them. You will be given a score at the end. Good luck!")
print(welcome_message())
# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct
def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
    print(question)
    print("A"+  option_1)
    print("B" + option_2)
    print("C" + option_3)
    print("D" + option_4)
    user_answer = input("What is your answer? ")
    if user_answer == correct_answer:
        return True
        points = points + 1
    else:
        return False
QuestionA = ask_question("What is Spongebob's pet's name?", "Gary", "Bob", "Greg", "Sandy", "A")
QuestionB = ask_question("What is the name of the building that Spongebob works at?", "Chum Bucket", "Krusty Krab", "Krusty Chum", "Krusty Plankton", "B")
QuestionC = ask_question("What is the name of Spongebob's best friend?", "Larry", "Sandy", "Patrick", "Squidward", "C")
QuestionD = ask_question("What is the name of Spongebob's favorite food?", "Pizza", "Chum", "Kelp Fries", "Krabby Patty", "D")
# Create a function to display the final score, which takes the score as a parameter and displays a message.
def final_score(points): 
    print("Your score is " + str(points))    
print(final_score(points))

# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).
