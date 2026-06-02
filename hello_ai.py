from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Be concise and friendly."},
        {"role": "user", "content": "What is Python?"}
    ],
    max_tokens=100
)


reply = response.choices[0].message.content
used_tokens = response.usage.total_tokens
cost = used_tokens * 0.00000015   # gpt-4o-mini: $0.15 per 1M tokens

print(f"AI says: {reply}")
print(f"Tokens used: {used_tokens}")
print(f"Cost: ${cost:.6f}") 