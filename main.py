answer1 = input("Is it raining?")
answer1 = answer1.lower()
if answer1 == "yes":
    answer2 = input("Is it windy?")
    answer2 = answer2.lower()
    if answer2 == "yes":
        print('It is too windy for an umbrella.')
    else:
        print('Take an umbrella.')
else:
    print('Enjoy your day.')
