# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

# The Hashtag Generator

def generate_hashtag(s):
    if len(s) > 140:
        return False
    new = ''
    for i in s.split():
        if i != " ":
            new += i.capitalize()
    if not new:
        return False
    return f'#{new}'
