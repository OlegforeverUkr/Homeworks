with open('Big_text.txt', 'r') as f:
    line = "\n".join([line.strip() for line in f])


def only_words(txt):
    words = []
    for i in txt.split():
        word = ''
        for n in i.lower():
            if n.isalpha():
                word += n
        words.append(word)
    return words


def count(lst):
    total = {}
    for i in lst:
        if i not in total:
            total.update({i: 1})
        else:
            total[i] += 1
    return total


from_line = only_words(line)
final = count(from_line)

print(sorted(final.items(), key=lambda x: x[1], reverse=True))
