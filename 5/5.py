# https://www.codewars.com/kata/582dace555a1f4d859000058/train/python

# Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins


def find_admin(lst, lang):
    answer = []
    if not lst or not lang:
        return answer
    for i in lst:
        values = i.values()
        if lang in values:
            if i.get('githubAdmin') == "yes":
                answer.append(i)

    return answer
