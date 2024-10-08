import ai_helper
import os
import message
import env_set_up
from datetime import datetime

FILE_NAME = 'conversation.txt'


def save_to_file(message_list):
    with open(FILE_NAME, 'w') as f:
        for msg in message_list:
            f.write(msg + '\n')

    pass
    # for each message in the list, put it in the file


def create_new_chat():
    print('New chat\n')
    print('Instruction: enter your message, and hit enter. \nEnter \'quit\' if you want to end the chat.\n')

    user_message = ''
    message_list = []

    while True:
        user_message = input('Enter message: ')
        user_message = user_message.strip()
        if user_message == 'quit':
            # if the message_list's length > 0, save it to the file by using save_to_file function
            break
        else:
            response = ai_helper.send_message(user_message)
            print('ChatGPT: ' + response)
            # create a message object and add it to message_list
            current_time = datetime.now().time()
            message_from_user = message.Message(current_time, 'user', response)
            message_from_ai = message.Message(current_time, 'ChatGPT', response)
            message_list.append(message_from_user)
            message_list.append(message_from_ai)

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


# initial setup
print('Welcome to AI Helper!')
env_set_up.check_and_set_api_key()

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
    delete_chat()
