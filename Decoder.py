import json
count_10 = (num for num in range(10, 1010, 10))
count_1 = (num for num in range(1, 1001, 1))
last_line = ''

with open('C:\\Users\\Alex_job\\Documents\\Program_job\\Copy.txt', mode= 'r', encoding= 'UTF-8') as program, open('C:\\Users\\Alex_job\\Documents\\Program_job\\Paste.txt', mode= 'w', encoding= 'UTF-8') as res:
    file = program.readlines()

    for line in file:
        if last_line == '\n' or 'M1' in last_line or 'if' in last_line or '(B270)' in last_line:
            count = next (count_10)
        else:
            count = next(count_1)
        if 'N' in line and '(' in line:
            line = line.replace(line[line.index('N'):line.index('(')], 'N' + str(count))
            res.write(line)
        elif 'N['in line:
            res.write(line)
        elif 'END' in line:
            res.write(line)
        elif 'N' in line:
            line = line.replace(line, 'N' + str(count))
            res.write(line)
        else:
            res.write(line)
        last_line = line