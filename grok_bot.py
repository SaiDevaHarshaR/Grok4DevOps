from gpt4all import GPT4All

model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf", allow_download=False)

print("🤖 Grok 4 DevOps - Your terminal DevOps buddy (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    response = model.generate(prompt=user_input, max_tokens=200)
    print(f"Grok: {response}\n")
