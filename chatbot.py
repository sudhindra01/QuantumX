import openai
openai.api_key = "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"

content = input("User: ")
response = openai.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
    model="gpt-3.5-turbo",

)
chat_response = response.choices[0]
print(f'ChatGPT: {chat_response}')
