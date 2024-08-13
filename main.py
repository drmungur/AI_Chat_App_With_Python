import ai_helper
import os

FILE_NAME = 'conversation.txt'


def create_new_chat():
    print('New chat\n')
    print('Instruction: enter your message, and hit enter. \nEnter \'quit\' if you want to end the chat.\n')

    user_message = ''

    while True:
        user_message = input('Enter message: ')
        user_message = user_message.strip()
        if user_message == 'quit':
            break
        else:
            response = ai_helper.send_message(user_message)
            print('ChatGPT: ' + response)

    print("Program ended.")


def load_latest_chat():
    if not os.path.isfile(FILE_NAME):
        print('No chat\nPress 1 to create new\n Press 2 to exit')

        if input("Enter: ") == '1':
            create_new_chat()
        else:
            exit(0)

    for line in FILE_NAME:
        print(line)


def delete_chat():
    if os.path.isfile(FILE_NAME):
        del FILE_NAME


print('Press 1 for new chat\nPress 2 to load latest chat\nPress 3 to clear chat')
user_input = input("User: ")

if user_input == '1':
    print('User opts for a new chat.')
    create_new_chat()


elif user_input == '2':
    print('User opts to load latest chat.')
    load_latest_chat()
else:
    print('User opts to delete chat permanently.')
