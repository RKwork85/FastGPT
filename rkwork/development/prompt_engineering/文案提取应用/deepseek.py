
from openai import OpenAI

client = OpenAI(api_key="sk-13870ed83bb741e59db6ca2877726057", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好啊"},
    ],
    stream=False
)

print(response.choices[0].message.content)