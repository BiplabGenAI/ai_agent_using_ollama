import ollama
response = ollama.chat(model='llama3:latest', messages=[
  {
    'role': 'user',
    'content': 'What is GenAI?',
  },
])
print(response['message']['content'])