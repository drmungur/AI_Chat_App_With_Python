import os


def check_and_set_api_key():
    """
    Check if 'ai-helper-api-key' exists in environment variables.
    If not, prompt the user to enter the key and set it.
    """
    api_key = os.getenv('ai-helper-api-key', 'Not Set')

    if api_key.__eq__('Not Set'):
        api_key = input("Enter your AI Helper API key: ")
        os.environ['ai-helper-api-key'] = str(api_key)
        print("API key set successfully.")


def get_api_key():
    if os.getenv('ai-helper-api-key') is None:
        check_and_set_api_key()
    else:
        return os.getenv('ai-helper-api-key')
