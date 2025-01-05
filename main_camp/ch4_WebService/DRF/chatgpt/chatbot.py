from openai import OpenAI
from api_pjt import config

CLIENT = OpenAI(
    api_key=config.OPENAI_API_KEY,
)

system_instructions = "You ara a helpful assistant."

def chatbot(user_message):
    completion = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_instructions,
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
    )

    return completion.choices[0].message