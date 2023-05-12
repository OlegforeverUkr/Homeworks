# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/python

# CSV representation of array

def to_csv_text(array):
    new = ""
    for i in array:
        for k in i:
            new += "".join(f'{str(k)},')
        new = new[:-1]
        new += f'\n'
    new = new[:-1]
    return new
