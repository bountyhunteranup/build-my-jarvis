# jarvis_v0.py
def handle(command: str) -> str | None:
    if command == "hello":
        return "Hello! I'm Jarvis v0, very dumb but very yours."
    if command == "quit":
        return None
    return f"I heard: {command} (I don't know how to do anything yet)"

print("Jarvis v0 ready. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = handle(user_input)
    if response is None:
        print("Jarvis: Goodbye!")
        break
    print("Jarvis:", response)