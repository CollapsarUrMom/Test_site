import json
count = 10
with open('C:\\Users\\Alex_job\\Documents\\Program_job\\Copy.txt', mode= 'r', encoding= 'UTF-8') as program, open('C:\\Users\\Alex_job\\Documents\\Program_job\\Paste.txt', mode= 'w', encoding= 'UTF-8') as res:
    file = program.readlines()

    for line in file:
        if line[0] == 'N':
            for letter in line:
                if letter == 'N' or letter != '(':
                    del[letter]
            res.write('N' + str(count) + line + '\n')
            count += 10
        else:
            res.write(line)