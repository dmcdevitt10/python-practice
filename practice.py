# Length of string
name = input("What is your name?\n")
length = len(name)
print(length)

# What is your band name
city = input("What city did you grow up in?\n")

pet = input("What is the name of your pet?\n")

print("Your band name is " + city + " " + pet)



# How many weeks till 90 years old
age = input("What is your age?\n")

age_int = int(age)

age_90 = 4680

your_age = age_int * 52

weeks_left = age_90 - your_age

print(f"You have {weeks_left} weeks left.")