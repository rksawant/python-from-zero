import os
from groq import Groq

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("This is Groq Text Summarizer")

msgs = [
    {
        "role":"system",
        "content":"Your are text summarizer. Summarize text in two bullet points only"
    }
]

print("Enter a text to Summarize")
user_input = input("User: ").strip()

msgs.append(
    {
        "role":"user",
        "content":user_input
    }
    )

response = groq_client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages= msgs,
    temperature=0.2,
    max_completion_tokens=1000
)

print(response.choices[0].message.content)