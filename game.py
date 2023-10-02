# For ASCII Art
import pyfiglet

# Request the api from Oobabooga (can be replaced with a genuine openai api with some edits)

# Change to the openai api url from Ooba
key = 'URL HERE'
import openai
try:
    openai.api_key = "sk-111111111111111111111111111111111111111111111111"
    openai.api_base = key
except Exception as e:
    print(f"OpenAI Key not Found: {e}")
    quit()

# Prompt for title, this has nothing to do with the actual game, just generates a cool title!
title_prompt = "Create a title for a fantasy story. Only write the title. Do not explain the title. Do not ask if there are any questions. Only respond with the title."
title = openai.ChatCompletion.create(
  model='x',
  messages=[{'role': 'system', 'content': f"{title_prompt}"}]
)

# Creates and prints the generated title using pyfiglet
title_result = pyfiglet.figlet_format(title['choices'][0]['message']['content'], font="invita")
print(title_result)

# Generate the initial game message. This will create the initial context for the game. Streams the text for a ChatGPT-like view.
prompt = 'Write me a prologue for a fantasy short story in 1 paragraph max. It should describe an introduction to a story. It should be in the 3rd person. Do not ask if this was a good response. Do not ask if I have questions. You are the game.'
begin = 'What is your first action player?'
next_begin = 'What is your action player?'
# Messages is the chat history for context.
messages = [{'role': 'system', 'content': f"{prompt}"}]

initial_response = openai.ChatCompletion.create(
    model='x',
    messages=messages,
    stream=True
)
final_response = ''
# Prints the response
for chunk in initial_response:
    final_response += chunk['choices'][0]['message']['content']
    print(chunk['choices'][0]['message']['content'], end='', flush=True)

# Append the messages for context and prints a beginning statement
messages.append({'role': 'system', 'content': f"{final_response}"})
print('\n\n' + begin)
messages.append({'role': 'system', 'content': f"{begin}"})
print('\n')

# Game loop, goes on infinitely
while True:
    user_input = input('You >>> ')
    print('\n\n')
    # Add the player's response to the context history
    messages.append({'role': 'user', 'content': f"{user_input}"})

    # Generates the AI's response with the context. Streams the text for a ChatGPT-like view.
    response = openai.ChatCompletion.create(
        model='x',
        messages=messages,
        stream=True
    )
    final_response = ''
    for chunk in response:
        final_response += chunk['choices'][0]['message']['content']
        print(chunk['choices'][0]['message']['content'], end='', flush=True)
    messages.append({'role': 'system', 'content': f"{final_response}"})

    # Beginning prompt again
    print('\n\n' + next_begin)
    messages.append({'role': 'system', 'content': f"{next_begin}"})
    print('\n')