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
import random
import new_module

random_float = random.random() * 5

print(random.randint(0,1))