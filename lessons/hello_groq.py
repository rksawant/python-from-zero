import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# client.chat.completions.create:
# client → Groq API client initialized earlier.
# chat → Accesses the chat API.
# completions → Generates a response based on messages.
# create() → Sends the API request to the AI model.
# response → Stores the result returned by Groq.

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a python and groq expert.",
        },
        {
            "role": "user", 
            "content": "First step for Python to work with Groq?"
        },
    ],
)

print(response.choices[0].message.content)

"""  response.choices[0].message.content
The response has a structure similar to:
{
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Python is a programming language."
            }
        }
    ]
}

"""
