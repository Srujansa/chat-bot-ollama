import litellm

def chatbot(prompt):
    response = litellm.completion(
        model="ollama/mistral",
        messages=[{'role': 'user', 'content': prompt}],
    )

    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit', 'bye']:
            break

        print("Chatbot: " + chatbot(user_input))
