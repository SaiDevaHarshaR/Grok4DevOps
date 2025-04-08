# app/grok_engine.py

from gpt4all import GPT4All
from app.helpers import explain_jenkins_error

model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

def grok_response(prompt: str) -> str:
    # Check for Jenkins logs
    if "jenkins" in prompt.lower() or "ERROR:" in prompt:
        parsed = explain_jenkins_error(prompt)
        return f"Log Analysis:\n{parsed}"

    # Custom instruction-style prompt template
    formatted_prompt = f"""
You are Grok4DevOps, a senior DevOps engineer and expert in AWS, Jenkins, Linux, Docker, Kubernetes, and infrastructure automation.

Only answer DevOps-related queries. Be concise, technical, and helpful. Use bullet points or code blocks if needed.

User asked: {prompt}

Your response:
"""
    return model.generate(prompt=formatted_prompt, max_tokens=200)

