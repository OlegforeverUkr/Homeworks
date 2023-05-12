# https://www.codewars.com/kata/582e0e592029ea10530009ce/train/python

# Duck Duck Goose

def duck_duck_goose(players, goose):
    return players[goose % len(players) - 1].name
