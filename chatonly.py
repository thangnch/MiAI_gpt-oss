from ollama import chat, Client
from ollama import ChatResponse
client = Client(
    host="http://103.78.3.95:8888"
)

response: ChatResponse = client.chat(
    model="gpt-oss:20b",
    messages=[
        {
            'role':'user',
            'content':'Tại sao cá lại bơi được. Trả lời ngắn gọn.'
        }
    ]
)

print("*"*30, "THINKING:\n")
print(response.message.thinking)
print("*"*30, "ANSWER:\n")
print(response.message.content)