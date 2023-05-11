import openai
import time

# Set up OpenAI API key
openai.api_key = "sk-U2Pdbcls56J9i6go0A9jflaT3BlbkFJNyvu2Ne7zNaE2n57n1WX"

# Define the prompt for the conversation
prompt = "Let's have a conversation!"

# Define the temperature for generating responses
temperature = 0.7

# Define the maximum number of tokens to generate in each response
max_tokens = 60

# Define the number of responses to generate for each prompt
num_responses = 5

# Set up the conversation API parameters
model_engine = "gpt3"
model_prompt = prompt
model_temperature = temperature
model_max_tokens = max_tokens
model_num_responses = num_responses

# Start the conversation
def converse(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=model_prompt + "\nUser: " + prompt + "\nChatGPT:",
        temperature=model_temperature,
        max_tokens=model_max_tokens,
        n=model_num_responses,
        stop=None,
        )
    message = response.choices[0].text.strip()
    return message

# Have a conversation with ChatGPT
while True:
    user_input = input("You: ")
    response = converse(user_input)
    print("ChatGPT: " + response)
    time.sleep(1)
    