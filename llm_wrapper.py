import os
from openai import OpenAI


client = OpenAI(api_key="sk-fd448f29651d428f96028f6670ce58bf", base_url="https://api.deepseek.com")
def ask_llm(prompt):
    response = client.chat.completions.create(
        model="deepseek-chat",  # 使用 ChatCompletion API
        messages=[{"role": "user", "content": prompt}]  # 使用 prompt 作为用户消息
    )

    return response.choices[0].message.content.strip()  # 获取聊天回复的内容
