from openai import OpenAI
import os


os.environ['ARK_API_KEY'] = '4d290b00-884f-4072-b364-ef790a2a6276'
client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.environ.get("ARK_API_KEY")
)

print("----- standard request -----")
completion = client.chat.completions.create(
    model="<YOUR_ENDPOINT_ID>",
    messages = [
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "常见的十字花科植物有哪些？"},
    ],
)
print(completion.choices[0].message.content)