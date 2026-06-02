from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

r = client.chat.completions.create(
    model    = 'gpt-4o-mini',
    messages = [{'role': 'user', 'content': 'Say hello!'}]
)
print(r.choices[0].message.content)     # Hello! How can I help you?
