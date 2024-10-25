import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.environ["API_KEY"])

system_prompt = "You are a friendly and supportive teching assitant for CS50. You also a duck"

user_prompt = input("Cual es tu pregunta=?")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    model="gpt-4"
)

response_text = chat_completion.choices[0].message.content

print(response_text)
