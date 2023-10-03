import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    try:
        # Call the OpenAI API to generate a response based on the prompt
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=3000  # You can adjust this as needed
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Main program loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # Generate a response based on user input
    response = generate_response(user_input)

    # Print the AI's response
    print("AI: " + response)
