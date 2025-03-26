import ollama

def ai_response(user_input):
    response = ollama.chat("mistral", messages=[{"role": "user", "content": user_input}])
    return response['message']['content']

# Function Call:
# response = ai_response("Hello, what can you do?")
# print(response)
