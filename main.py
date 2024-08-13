import ai_helper
import env_set_up


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
else:
    print('User opts to delete chat permanently.')
