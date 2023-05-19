# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

# Pete, the baker

def cakes(recipe, available):
    cakes = []
    for i, x in recipe.items():
        if i in available:
            cakes.append(available[i] // x)
        else:
            return 0

    return min(cakes)
