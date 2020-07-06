import random

# Greetings
name = input("Enter you name: ")
print(f'Hello, {name}')

# Defining option list
input_option = input('> ')
if input_option == '':
    options = ['paper', 'scissors', 'rock']
else:
    options = input_option.split(",")

# Checking scores
file = open('rating.txt', 'r')
score = {}
for line in file.readlines():
    score[line.split()[0]] = int(line.split()[1])
file.close()
if name not in score:
    score[name] = 0

# Welcoming message
print()
print("Okay, let's start")

# user choice
user_choice = input()

# Main cycle
while user_choice != '!exit':
    if user_choice == '!rating':
        print(f'Your rating: {score[name]}')
    elif user_choice not in options:
        print("Invalid input")
    elif user_choice in options:
        computer_choice = random.choice(options)

        if user_choice == computer_choice:
            print(f'There is a draw ({computer_choice})')
            score[name] += 50
        else:
            i = options.index(user_choice)
            final_list = options[(i + 1):] + options[:i]
            final_list.insert(len(final_list) // 2, user_choice)

            if final_list.index(computer_choice) < final_list.index(user_choice):
                print(f'Sorry, but computer chose {computer_choice}')
            else:
                print(f'Well done. Computer chose {computer_choice} and failed')
                score[name] += 100

    user_choice = input()

print("Bye!")
