import openai
openai.api_key = "INSERT YOUR SECRET KEY"

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
