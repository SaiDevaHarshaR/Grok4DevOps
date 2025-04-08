# app/cli_bot.py

from app.grok_engine import grok_response

print("Ask Grok DevOps Bot → ", end="")
while True:
    query = input()
    response = grok_response(query)
    print(f"🤖 Grok says:\nA: {response}")
    print("Ask Grok DevOps Bot → ", end="")
