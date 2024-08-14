# helper for all AI related functions

from openai import OpenAI

import env_set_up


def send_message(message):
    # client = OpenAI(api_key=env_set_up.get_api_key())
    #
    # completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": message},
    #     ]
    # )

    # return completion.choices[0].message.content
    return 'Placeholder'
