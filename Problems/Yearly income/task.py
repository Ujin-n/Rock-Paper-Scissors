with open('salary.txt', 'r') as m, open('salary_year.txt', 'w') as y:
    for line in m.readlines():
        y.write(str(int(line) * 12) + '\n')
