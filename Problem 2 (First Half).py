from sys import stdin, stdout

t = int(stdin.readline().strip())

results = []

for i in range(t):
    string = stdin.readline().strip()

    lstring = list(string)

    nd = 0

    newl = []

    for x in lstring:
        if x == '1':
            newl.append('(')
            newl.append(x)
            newl.append(')')
            continue
        elif x == '2':
            for i in range(2):
                newl.append('(')
            newl.append(x)
            for i in range(2):
                newl.append(')')
            continue
        elif x == '3':
            for i in range(3):
                newl.append('(')
            newl.append(x)
            for i in range(3):
                newl.append(')')
            continue
        elif x == '4':
            for i in range(4):
                newl.append('(')
            newl.append(x)
            for i in range(4):
                newl.append(')')
            continue
        elif x == '5':
            for i in range(5):
                newl.append('(')
            newl.append(x)
            for i in range(5):
                newl.append(')')
            continue
        elif x == '6':
            for i in range(6):
                newl.append('(')
            newl.append(x)
            for i in range(6):
                newl.append(')')
            continue
        elif x == '7':
            for i in range(7):
                newl.append('(')
            newl.append(x)
            for i in range(7):
                newl.append(')')
            continue
        elif x == '8':
            for i in range(8):
                newl.append('(')
            newl.append(x)
            for i in range(8):
                newl.append(')')
            continue
        elif x == '9':
            for i in range(9):
                newl.append('(')
            newl.append(x)
            for i in range(9):
                newl.append(')')
            continue

        newl.append(x)

    str_newl = ''.join(newl)

    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0
    counter8 = 0
    counter9 = 0

    for char in list(str_newl):
        if char == '1':
            counter1 == 1
        elif char == '2':
            counter2 += 1
        elif char == '3':
            counter3 += 1
        elif char == '4':
            counter4 += 1
        elif char == '5':
            counter5 += 1
        elif char == '6':
            counter6 += 1
        elif char == '7':
            counter7 += 1
        elif char == '8':
            counter8 += 1
        elif char == '9':
            counter9 += 1

    for i in range(counter1):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter2):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter3):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter4):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter5):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter6):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter7):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter8):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    for i in range(counter9):
        if ')(' in str_newl:
            list_snewl = str_newl.split(')(')
            str_newl = ''.join(list_snewl)

    results.append(str_newl)

for index in range(len(results)):
    print("Case #{}: {}".format(index + 1, results[index]))
