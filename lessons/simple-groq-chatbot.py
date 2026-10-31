import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role":"system",
        "content":"You are a good python teacher"
    },
]

print("Welcome to the Groq Chatbot! Type 'exit' or 'quit' to end the conversation.")

while True:
    user_input = input("User: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if not user_input:
        print("Please enter a message.")
        continue

    messages.append({"role":"user", "content":user_input})

    try:
        response = client.chat.completions.create(
            model = "openai/gpt-oss-120b",
            messages= messages
        )

        answer = response.choices[0].message.content
        print("\nAI:", answer)

        messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )
    except Exception as e:
        print("Error:", e)