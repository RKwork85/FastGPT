'''
api 对接oneapi平台模型
'''

'''http方式  不可用
curl --location --request POST 'http://127.0.0.1:3000/api/v1/chat/completions' \
--header 'Authorization: Bearer fastgpt-xX2FbZzgsKIJIVXH1Kng0GtBY89kYXJbRZ2Bre1N1Zh0ajU6jIOW9' \
--header 'Content-Type: application/json' \
--data-raw '{
    "chatId": "111",
    "stream": true,
    "detail": false,
    "messages": [
        {
            "content": "写一篇800字的文章，题目为：论当代大学生的社会担当",
            "role": "user"
        }
    ]
}'

'''

from openai import OpenAI
import os
os.environ["OPENAI_API_"] = "sk-proj-"
client = OpenAI()         
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "你是谁"}],
    stream=True,
    
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")


#  default_headers={
#         'Authorization': 'Bearer fastgpt-xX2FbZzgsKIJIVXH1Kng0GtBY89kYXJbRZ2Bre1N1Zh0ajU6jIOW9',
#         'Content-Type': 'application/json'
#     }



