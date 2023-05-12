size = input("Please, insert your size - ")


def your_size(s):
    XXS = {'Россия': 42,
           'Германия': 36,
           'США': 8,
           'Франция': 38,
           'Великобритания': 24}

    if s.lower() == "xxs":
        return '\n'.join(f'{key} - {str(value)}' for key, value in XXS.items())

    elif s.lower() == "xs":
        answer = {key: value + 2 for key, value in XXS.items()}
        return '\n'.join(f'{key} - {str(value)}' for key, value in answer.items())

    elif s.lower() == "s":
        answer = {key: value + 4 for key, value in XXS.items()}
        return '\n'.join(f'{key} - {str(value)}' for key, value in answer.items())

    elif s.lower() == "m":
        answer = {key: value + 6 for key, value in XXS.items()}
        return '\n'.join(f'{key} - {str(value)}' for key, value in answer.items())

    elif s.lower() == "l":
        answer = {key: value + 8 for key, value in XXS.items()}
        return '\n'.join(f'{key} - {str(value)}' for key, value in answer.items())

    elif s.lower() == "xl":
        answer = {key: value + 10 for key, value in XXS.items()}
        return '\n'.join(f'{key} - {str(value)}' for key, value in answer.items())

    elif s.lower() == "xxl":
        answer = {key: value + 12 for key, value in XXS.items()}
        return '\n'.join(f'{key} - {str(value)}' for key, value in answer.items())

    elif s.lower() == "xxxl":
        answer = {key: value + 14 for key, value in XXS.items()}
        return '\n'.join(f'{key} - {str(value)}' for key, value in answer.items())
    else:
        return "Error insert data!!!"


print(your_size(size))
