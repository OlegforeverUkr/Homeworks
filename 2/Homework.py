name = input("Wat's your name? - ")

if 'a' in name:
    print("We won't test you.")
else:
    age = int(input('How old are you? - '))
    if age > 100:
        print('You are liar')
    elif age > 18:
        print('Its OK')
        if age % 2:
            print('Not paired')
        else:
            print('Paired')

        if 'v' in name.lower() and not age % 2:
            print('You win!!!')
        else:
            print("You didn't win")

    else:
        print('Somthing wrong!')
