with open('text.txt', 'r') as f:
    l = [line.strip() for line in f]

    for i in l:
        s = []
        s += i.split()
        print(s)

        fizz = int(s[0])
        buzz = int(s[1])
        n = int(s[2])
        output = ""

        for x in range(1, n + 1):
            if not x % fizz and not x % buzz:
                output += "FB "
            elif not x % fizz:
                output += "F "
            elif not x % buzz:
                output += "B "
            else:
                output += f'{x} '

        with open("answer.txt", "a") as t:
            t.write(f'{output}\n')

        print(output)
