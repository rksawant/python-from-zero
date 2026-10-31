import os
from groq import Groq

grop_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role":"system",
        "content":(
            "You are an expert Python Developer."
            "Provide simple Python Code"
        )
    }
]

print("Welcome to Python Code Generator! Type 'exit' or 'quit' to end the conversation")

print("Describe you python task")
while True:
    user_input = input().strip()

    if user_input.lower() in ["exit","quit"]:
        print("Bye!")
        break

    if not user_input:
        print("Describe you python task")
        continue

    messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    try:
        response = grop_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            max_completion_tokens=1000,
            temperature=0.2
        )

        print("\nGenerated Solution:")
        print(response.choices[0].message.content)
    except Exception as e:
        print("Error Occurred!")

