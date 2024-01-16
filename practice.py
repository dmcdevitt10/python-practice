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




# if/else
# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm?"))

# if height == 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you can't ride it!")



# Odd or Even
number = int(input("Choose a whole number"))

if number % 2 != 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
