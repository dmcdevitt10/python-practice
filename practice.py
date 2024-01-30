# Length of string
# name = input("What is your name?\n")
# length = len(name)
# print(length)

# What is your band name
# city = input("What city did you grow up in?\n")

# pet = input("What is the name of your pet?\n")

# print("Your band name is " + city + " " + pet)



# How many weeks till 90 years old
# age = input("What is your age?\n")

# age_int = int(age)

# age_90 = 4680

# your_age = age_int * 52

# weeks_left = age_90 - your_age

# print(f"You have {weeks_left} weeks left.")



# Tip Calculator
# print("Welcome to the tip calculator.")

# bill_total_without_tip = input("What was the total bill? $")

# tip_size = input("What percentage tip would you like to give? 15, 20, or 25?")

# people_to_split_the_bill = input("How many people to split the bill?")

# bill_total_with_tip = float(bill_total_without_tip) + (float(bill_total_without_tip) * (int(tip_size) / 100))

# print(bill_total_with_tip)

# cost_per_person = bill_total_with_tip / int(people_to_split_the_bill)

# cost_per_person = round(cost_per_person, 2)

# print(f"Each person should pay: ${cost_per_person}")




# # if/else
# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#     age = int(input("What is your age?"))
#     if age >= 18:
#         print("Adult tickets are $12")
#         bill = 12
#     elif age >= 12:
#         print("Youth tickets are $8")
#         bill = 8
#     elif age >= 45 and age <= 55:
#         print("You ride for free!")
#     else:
#         print("Child tickets are $5")
#         bill = 5

#     wants_photo = input("Do you want a photo taken? Y or N")

#     if wants_photo == "Y":
#         bill += 3

#     print(f"You final bill is ${bill}")

# else:
#     print("Sorry, you can't ride it!")



# Odd or Even
# number = int(input("Choose a whole number"))

# if number % 2 != 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")



# BMI Calculator
# height = float(input("What is your height in meters"))

# weight = int(input("What is your weight in pounds?"))

# bmi = weight / (height * height)

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")





# Pizza Order 
# print("Thank you for choosing Python Pizza Deliveries!")

# bill = 0

# size = input("What size pizza do you want? S, M, or L")

# add_pepperoni = input("Do you want pepperoni? Y or N")

# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#     bill += 2
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#     bill += 3
# else:
#     bill = 25


# extra_cheese = input("Do you want extra cheese? Y or N")

# if extra_cheese == "Y":
#     bill +1

# print(f"Your final bill is: ${bill}.")




# Love calculator
# print("The Love Calculator is calculating your score...")
# name1 = input("What is your name?")
# name2 = input("What is their name?")

# names = name1 + name2

# lower_case_names = names.lower()

# t = lower_case_names.count("t")
# r = lower_case_names.count("r")
# u = lower_case_names.count("u")
# e = lower_case_names.count("e")
# l = lower_case_names.count("l")
# o = lower_case_names.count("o")
# v = lower_case_names.count("v")
# e = lower_case_names.count("e")

# true = t + r + u + e
# love = l + o + v + e


# str_score = str(true) + str(love)

# score = int(str_score)

# message = f"Your score is {score}, "

# if score < 10 or score > 90:
#   message += "you go together like coke and mentos."
# elif score >= 40 and score <= 50:
#   message += "you are alright together."
# else:
#   message = f"Your score is {score}."


# print(message)




# random numbers
# import random
# import new_module

# random_float = random.random() * 5

# print(random.randint(0,1))



# appending and extending lists
# states_of_america = ["delaware", "utah", "idaho"]

# states_of_america[1] = "Hawaii"

# states_of_americaappend("Florida")
# states_of_americaextend(["cali", "new york"])

# print(states_of_america)



#random name/string from a list
# import random

# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# number_of_people = len(names) - 1

# random_person = random.randint(0, number_of_people)

# person_to_pay = names[random_person]

# print(f"{person_to_pay} is going to buy the meal today!")





# X marks the spot: nested lists and changing values
# line1 = [" ","️ ","️ "]
# line2 = [" "," ","️ "]
# line3 = [" "," "," "]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input("Where do you want the treasure? A1 - C3\n")

# column = 0

# if position[0] == "A":
#   column = 0
# elif position[0] == "B":
#   column = 1
# else:
#   column = 2

# if position[1] == "1":
#   map[0][column] = "X"
# elif position[1] == "2":
#   map[1][column] = "X"
# else:
#   map[2][column] = "X"


# print(map)




# rock paper scissors
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# options = ["rock", "paper", "scissors"]

# players_choice = options[int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))]

# computers_choice = options[random.randint(0,2)]

# if players_choice == "rock":
#     print(f"You chose\n{rock}")
#     if computers_choice == "rock":
#         print(f"Computer chose\n{rock}")
#         print("Draw")
#     if computers_choice == "paper":
#         print(f"Computer chose\n{paper}")
#         print("You lose")
#     if computers_choice == "scissors":
#         print(f"Computer chose\n{scissors}")
#         print("You Win")
# elif players_choice == "paper":
#     print(f"You chose\n{paper}")
#     if computers_choice == "paper":
#         print(f"Computer chose\n{paper}")
#         print("Draw")
#     if computers_choice == "scissors":
#         print(f"Computer chose\n{scissors}")
#         print("You lose")
#     if computers_choice == "rock":
#         print(f"Computer chose\n{rock}")
#         print("You Win")
# elif players_choice == "scissors":
#     print(f"You chose\n{scissors}")
#     if computers_choice == "scissors":
#         print(f"Computer chose\n{scissors}")
#         print("Draw")
#     if computers_choice == "rock":
#         print(f"Computer chose\n{rock}")
#         print("You lose")
#     if computers_choice == "paper":
#         print(f"Computer chose\n{paper}")
#         print("You Win")





# for loops - finding the highest number
# numbers = [13, 78, 34, 69, 16, 62]

# highest_number = 0

# for number in numbers:
#     if number > highest_number:
#         highest_number = number

# print(f"The highest number is {highest_number}")


# total = 0

# for number in range(1,101):
#     total += number

# print(total)




# FizzBuzz
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)




# Password generator
# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# num_of_letters= int(input("How many letters would you like in your password?\n")) 
# num_of_symbols = int(input(f"How many symbols would you like?\n"))
# num_of_numbers = int(input(f"How many numbers would you like?\n"))

# letters_length = len(letters) - 1
# numbers_length = len(numbers) - 1
# symbols_length = len(symbols) - 1

# password_characters = []


# # Letters
# chosen_letters_indexes = []

# for iteration in range(0, num_of_letters):
#     new_letter = random.randint(0, letters_length)
#     chosen_letters_indexes.append(new_letter)

# for index_number in chosen_letters_indexes:
#     password_characters.append(letters[index_number])

# random.shuffle(password_characters)


# # Numbers
# chosen_numbers_indexes = []

# for iteration in range(0, num_of_numbers):
#     new_number = random.randint(0, numbers_length)
#     chosen_numbers_indexes.append(new_number)

# for index_number in chosen_numbers_indexes:
#     password_characters.append(numbers[index_number])

# random.shuffle(password_characters)


# # Symbols
# chosen_symbols_indexes = []

# for iteration in range(0, num_of_symbols):
#     new_symbol = random.randint(0, symbols_length)
#     chosen_symbols_indexes.append(new_symbol)

# for index_symbol in chosen_symbols_indexes:
#     password_characters.append(symbols[index_symbol])

# random.shuffle(password_characters)
# random.shuffle(password_characters)

# new_password = ''.join(password_characters)

# print(f"Here is your password: {new_password}")




# functions
# def my_function():
#     print("Hello")

# my_function()


#while loop
# number1 = 6

# while not number1 == 0:
#     print(number1)
#     number1 -= 1

# number2 = 6

# while number2 > 0:
#     print(number2)
#     number2 -= 1





# Hangman
# import random
# import hangman_words
# import hangman_art

# print(hangman_art.logo)

# word_list = hangman_words.word_list

# random_word = random.choice(word_list)




# display = []

# for letter in random_word:
#     display.append("_")



# stages = hangman_art.stages

# lives = 6

# end_of_game = False

# while not end_of_game:


#     guessed_letter = input("Guess a letter: ").lower()


#     if guessed_letter in random_word:
#         for position in range(len(random_word)):
#             correct_letter = random_word[position]
#             if guessed_letter == correct_letter:
#                 display[position] = guessed_letter
#     else:
#         lives -= 1
            
#     print(' '.join(display))

#     if "_" in display:
#         print(stages[lives])



#     if lives == 0:
#         end_of_game = True
#         print(f"\n\nSorry, You Lose! The word was {random_word}.")
            
#     if "_" not in display:
#         end_of_game = True
#         print(f"\n\nCongratulations! You win! The word was {random_word}.")




#function arguments/parameters
# def greet(name):
#     print(f"Hello {name}")

# greet("greg")

# # positional arguments
# def greet_with(name, location):
#     print(f"{name} lives in {location}")

# greet_with("Daniel", "Salt lake")


# #keyword arguments
# def greet_with(location, name):
#     print(f"{name} lives in {location}")

# greet_with(name = "Daniel", location = "Salt lake")





# number of cans to paint an area
# import math

# def paint_calc(height, width, cover):
#   num_cans = (height * width) / cover
#   round_up_cans = math.ceil(num_cans)
#   print(f"You'll need {round_up_cans} cans of paint.")

# test_h = int(input("Height in meters: ")) 
# test_w = int(input("Width in meters: ")) 
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



# # prime number checker
# def prime_checker(number):
#   prime = True
#   for n in range(2, number):
#     if number % n == 0:
#       prime = False
#       break
#   if prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")

    
# n = int(input("Number between 1 and 100: "))
# prime_checker(number=n)





#caesar cipher
# import cipher_art
# logo = cipher_art.logo
# print(logo)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def caesar(text, shift, direction):
#     new_text = ""
#     for letter in text:
#         old_position = alphabet.index(letter)
#         new_position = 0
#         if direction == "encode":
#             new_position = old_position + shift
#             if new_position >= len(alphabet):
#                 new_position -= len(alphabet)
#             new_text += alphabet[new_position]
#         if direction == "decode":
#             new_position = old_position - shift
#             new_text += alphabet[new_position]

#     print(f"The {direction} text is {new_text}")

# caesar(text, shift, direction)





#dictionaries
# dictionary = {
#     "bug": "an error"
# }

# dictionary["Loop"] = "doing something"

# print(dictionary)


# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille"]},
# }

# print(travel_log["France"]["cities_visited"])



# Add country to travel log
# country = input("Country: ")
# visits = int(input("Number of visits: "))
# list_of_cities = eval(input("list of cities: "))

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]

# def add_new_country(country, visits, list_of_cities):
#   travel_log.append({
#     "country": country,
#     "visits": visits,
#     "cities": list_of_cities
#   })

# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")




# #auction
# import auction_art
# print(auction_art.logo)
# print("Welcome to the auction!\n\n")


# bids = {}

# more_bidders = True

# winner = ""
# winning_bid = 0

# while more_bidders:

#     name = input("What is your name?: ")
#     bid = input("What is your bid?: ")

#     bids[name] = int(bid)

#     other_bidders = input("Are there any other bidders?")

#     if other_bidders == "no":
#         more_bidders = False

# for bidder in bids:
#     if bids[bidder] > winning_bid:
#         winner = bidder
#         winning_bid = bids[bidder]

# print(bids)
# print(f"The winner is {winner} with a bid of ${winning_bid}.")




# # Functions with outputs (return)
# def my_function():
#     return "hello"


# print(my_function())




# days in a month based off year
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year):
#     month_days[1] += 1
#   return month_days[month - 1]
  
  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)




# Calculator (with recursion)
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }


# def calculator():
#     number1 = float(input("What's the first number?: "))
#     for symbol in operations:
#         print(symbol)
        
#     should_continue = True

#     while should_continue:

#         operation_symbol = input("Pick an operation: ")
#         number2 = float(input("What's the next number?: "))

#         function = operations[operation_symbol]
#         answer = function(number1, number2)

#         print(f"{number1} {operation_symbol} {number2} = {answer}")

#         if input(f"Type 'y' to continue calculation with {answer}: ") == "y":
#             number1 = answer
#         else:
#             should_continue = False
#             calculator()

# calculator()





# Higher or Lower
import random
import higher_lower_art
import higher_lower_data

logo = higher_lower_art.logo
vs = higher_lower_art.vs
data = higher_lower_data.data

print(logo)

game_over = False

a = random.choice(data)
data.remove(a)

b = random.choice(data)
data.remove(b)

while not game_over:
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.\n\n")
    print(vs)
    print(f"\n\nAgainst B: {b["name"]}, a {b["description"]}, from {b["country"]}.")
    players_guess = input("Who has more followers? Type 'A' or 'B': ")
    if players_guess == "A": 
        if a["follower_count"] > b["follower_count"]:
            print(a["name"], a["follower_count"])
            print(b["name"], b["follower_count"])
            print("you win")
            a = b
            b = random.choice(data)
            data.remove(b)
        else:
            print(b["name"], b["follower_count"])
            print(a["name"], a["follower_count"])
            print("you lose")
            game_over = True
    elif players_guess == "B": 
        if b["follower_count"] > a["follower_count"]:
            print(b["name"], b["follower_count"])
            print(a["name"], a["follower_count"])
            print("you win")
            a = b
            b = random.choice(data)
            data.remove(b)
        else:
            print(a["name"], a["follower_count"])
            print(b["name"], b["follower_count"])
            print("you lose")
            game_over = True
