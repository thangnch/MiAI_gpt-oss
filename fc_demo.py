# Viết 1 hàm lấy 1 số random. Khi người dùng hỏi LLM cho 1 số random, LLM sẽ gọi hàm này
import random

def get_random_number() -> int:
    return random.randint(1, 10)


import ollama
from ollama import Client

client = Client(
    host="http://103.78.3.95:8888"
)

available_functions = {
    'get_random_number': get_random_number,
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_random_number",
            "description": "Get a random number",
            "parameters": {
            },
        },
    }
]

messages = [
    {
        'role':'system',
        'content': 'Base on the information return by function calling to answer question. Try to answer polite.'
    }
    ,
    {
        'role':'user',
        'content':'Give a random number'
    }
]

response = client.chat(
    model="gpt-oss:20b",
    messages=messages,
    tools = tools
)

response_message = response.message
print("*"*30, "THINKING:\n")
print(response_message)


for tool in response.message.tool_calls or []:
    function_to_call = available_functions.get(tool.function.name)
    if function_to_call == get_random_number:
        resp = function_to_call()
        messages.append(
          {
            "role": "system",
            "content": "Random number return from get_random_number function is " + str(resp),
          }
        )
    else:
        print('Function not found:', tool.function.name)


print("*"*30, "MESSAGE:\n")
print(messages)
# Call LLM 2nd time with function response
second_response = client.chat(
    "gpt-oss:20b",
    messages=messages
)


print("*"*30, "THINKING:\n")
print(second_response.message.thinking)
print("*"*30, "ANSWER:\n")
print(second_response.message.content)
