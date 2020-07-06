# read animals.txt
# and write animals_new.txt
file_1 = open('animals.txt')
file_2 = open('animals_new.txt', 'w')
for line in file_1.readlines():
    file_2.write(line.rstrip('\n') + ' ')
file_1.close()
file_2.close()
