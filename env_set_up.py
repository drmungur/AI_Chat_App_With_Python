import os


def check_and_set_api_key():
    """
    Check if 'ai-helper-api-key' exists in environment variables.
    If not, prompt the user to enter the key and set it.
    """
    api_key = os.getenv('ai-helper-api-key')

    if not api_key:
        api_key = input("Enter your AI Helper API key: ")
        os.environ['ai-helper-api-key'] = api_key
        print("API key set successfully.")
