# https://www.codewars.com/kata/5a81b78d4a6b344638000183/train/python

# Spanish Conjugator

def conjugate(verb):
    answer = {}
    if verb[-2:] == "ar":
        answer[verb] = [f'{verb[:-2]}o', f'{verb[:-2]}as', f'{verb[:-2]}a', f'{verb[:-2]}amos', f'{verb[:-2]}ais', f'{verb[:-2]}an']
    elif verb[-2:] == "er":
        answer[verb] = [f'{verb[:-2]}o', f'{verb[:-2]}es', f'{verb[:-2]}e', f'{verb[:-2]}emos', f'{verb[:-2]}eis', f'{verb[:-2]}en']
    elif verb[-2:] == "ir":
        answer[verb] = [f'{verb[:-2]}o', f'{verb[:-2]}es', f'{verb[:-2]}e', f'{verb[:-2]}imos', f'{verb[:-2]}is', f'{verb[:-2]}en']
    return answer
