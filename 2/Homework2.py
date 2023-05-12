gender = input("What's your gender? (m/w)")
age = int(input('How old are you? - '))
name = input("Wat's your name? - ")

if 'c' and 't' in name:
    print("We didn't recommend sport for you")
elif age < 15:
    print("We recommend tennis")
elif gender == "m":
    print("We recommend football")
elif gender == "w":
    print("We recommend basketball")

