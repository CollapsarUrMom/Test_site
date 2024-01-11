import json
count = 10
last_line = ''

with open('C:\\Users\\Alex_job\\Documents\\Program_job\\Copy.txt', mode= 'r', encoding= 'UTF-8') as program, open('C:\\Users\\Alex_job\\Documents\\Program_job\\Paste.txt', mode= 'w', encoding= 'UTF-8') as res:
    file = program.readlines()

    for line in file:
        if last_line == '\n' or 'M1' in last_line or 'if' in last_line or '(B270)' in last_line:
            num = 1
        elif 'GOTO' in last_line:
            count = count - (count // 10)
        else:
            num = 10
        if 'N' in line and '(' in line:
            line = line.replace(line[line.index('N'):line.index('(')], 'N' + str(count))
            res.write(line)
            count += num
        elif 'N['in line:
            res.write(line)
        elif 'END' in line:
            res.write(line)
        elif 'N' in line:
            line = line.replace(line, 'N' + str(count))
            res.write(line)
            count += num
        else:
            res.write(line)
        last_line = line