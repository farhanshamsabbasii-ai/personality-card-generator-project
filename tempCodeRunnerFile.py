# taking user input and then making a Personality card

# Taking user inputs
name = input("Enter your name: ")
city = input("Enter your city's name: ")
age = int(input("Enter your age: "))
superpower = input("Enter a superpower(something fun you are good at — e.g. Chai + Code): ")
lucky_number = int(input("Enter your Lucky number: "))
favorite_food = input("Enter your favorite food: ")
dream_job = input("Enter your dream job: ")
hobby = input("Enter your hobby: ")

# calculations
age_in_months = age * 12
age_in_2050 = 2050 - 2026 + age

# Personality card design with print() and f string
print("\n\n◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◪ ◩ ◪ ◩ ◪ ◩")
print("◪                                               ◩")
print("◪   📝           PERSONALITY CARD           📝  ◩")
print("◪                                               ◩")
print("◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◪ ◩ ◪ ◩ ◪ ◩")
print(f"◪  👤  Name               : {name}")
print(f"◪  🏢  City               : {city}")
print(f"◪  🎂  Age                : {age}  ({age_in_months}) months")
print(f"◪  😎  Superpower         : {superpower}")
print(f"◪  📅  In 2050            : {age_in_2050}")
print(f"◪  ☘   Lucky number x 7   : {lucky_number * 7}")
print(f"◪  🕵️‍♀️  'a' in name        : {'a' in name}")  
print(f"◪  🔞  Over 18?           : {age > 18}")
print(f"◪  🍔  Favorite food      : {favorite_food}")
print(f"◪  😍  Dream job          : {dream_job}")
print(f"◪  🏂  Hobby              : {hobby}")
print("◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◩ ◪ ◪ ◩ ◪ ◩ ◪ ◩")