# import re
# import random

# class JarvisBrain:
#     def __init__(self):
#         self.memory = {}  # Store past interactions

#     def analyze_command(self, command):
#         # Ensure command is a string
#         if isinstance(command, tuple):  
#             command = command[0]  # Extract first element from tuple
        
#         command = command.lower().strip()

#         # Checking greetings
#         if any(word in command for word in ["hello", "hi", "hey", "jarvis"]):
#             return random.choice(["Hello! How can I assist you?", "Hey! What do you need?", "Hi, ready for commands!"])

#         # Checking system control commands
#         elif "open" in command:
#             app_name = self.extract_app_name(command)
#             if app_name:
#                 return f"Opening {app_name}..."
#             return "Specify the application to open."

#         elif "search for" in command or "google" in command:
#             query = self.extract_search_query(command)
#             if query:
#                 return f"Searching Google for {query}..."
#             return "Please provide a search term."

#         elif "who is" in command or "what is" in command:
#             return f"Fetching information about {command.replace('who is', '').replace('what is', '').strip()}."

#         elif "remember" in command:
#             key, value = self.extract_memory(command)
#             if key and value:
#                 self.memory[key] = value
#                 return f"Got it! I'll remember that {key} is {value}."
#             return "What should I remember?"

#         elif "what do you remember" in command or "recall" in command:
#             return self.recall_memory()

#         elif "joke" in command:
#             return random.choice([
#                 "Why don’t programmers like nature? Too many bugs!", 
#                 "I told my computer a joke… now it won’t stop giggling."
#             ])

#         else:
#             return "I'm still learning. Can you rephrase?"

#     def extract_app_name(self, command):
#         """Extracts the application name from the command."""
#         match = re.search(r'open (\w+)', command)
#         return match.group(1) if match else None

#     def extract_search_query(self, command):
#         """Extracts search query from the command."""
#         match = re.search(r'search for (.+)', command)
#         return match.group(1) if match else None

#     def extract_memory(self, command):
#         """Extracts key-value pairs to remember."""
#         match = re.search(r'remember that (\w+) is (.+)', command)
#         return match.groups() if match else (None, None)

#     def recall_memory(self):
#         """Returns stored memory."""
#         if self.memory:
#             return "Here’s what I remember: " + ", ".join(f"{k} is {v}" for k, v in self.memory.items())
#         return "I don't remember anything yet."



import re
import random
import ollama  # AI-powered responses

class JarvisBrain:
    def __init__(self):
        self.memory = {}  # Store past interactions

    def analyze_command(self, command):
        if isinstance(command, tuple):  
            command = command[0]  
        command = command.lower().strip()

        # Predefined responses
        greetings = ["hello", "hi", "hey", "jarvis"]
        if any(word in command for word in greetings):
            return random.choice(["Hello! How can I assist you?", "Hey! What do you need?", "Hi, ready for commands!"])

        elif "remember" in command:
            key, value = self.extract_memory(command)
            if key and value:
                self.memory[key] = value
                return f"Got it! I'll remember that {key} is {value}."
            return "What should I remember?"

        elif "what do you remember" in command or "recall" in command:
            return self.recall_memory()

        elif "joke" in command:
            return random.choice([
                "Why don’t programmers like nature? Too many bugs!", 
                "I told my computer a joke… now it won’t stop giggling."
            ])

        # AI-powered response if no match
        else:
            return self.get_ai_response(command)

    def extract_memory(self, command):
        """Extracts key-value pairs to remember."""
        match = re.search(r'remember that (\w+) is (.+)', command)
        return match.groups() if match else (None, None)

    def recall_memory(self):
        """Returns stored memory."""
        if self.memory:
            return "Here’s what I remember: " + ", ".join(f"{k} is {v}" for k, v in self.memory.items())
        return "I don't remember anything yet."

    def get_ai_response(self, command):
        """Uses Ollama AI for smart responses."""
        try:
            response = ollama.chat(model="mistral:latest", messages=[{"role": "user", "content": command}])
            return response.get('message', {}).get('content', 'I don’t understand that yet.')
        except Exception as e:
            return f"Error with AI response: {e}"
