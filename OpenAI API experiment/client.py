
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are Jarvis, a smart virtual assistant. "
                   "You are helpful, intelligent, concise and conversational."
    }
]

print("JARVIS INITIALIZED.")
print("How can I help you today?")
print("Type 'exit' to shut down.\n")

while True:

    query = input("You: ")

    if query.lower() == "exit":
        print("Jarvis: Shutting down. Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": query
    })

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        answer = response.choices[0].message.content

        print("\nJarvis:", answer, "\n")

        messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        print("Error:", e)
