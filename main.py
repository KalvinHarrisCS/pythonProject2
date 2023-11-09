import openai
import json
import os


openai.api_key = 'xxx'


def log_conversation(conversation, filename="bot_communication_log.json"):
    try:
        with open(filename, 'a') as log_file:
            json.dump(conversation, log_file, indent=4)
            log_file.write(",\n")  # Ensuring each entry is on a new line for readability
    except Exception as e:
        print(f"Error logging conversation: {e}")


def generate_bot_code(description, bot_name):
    # Function to generate code for a new bot based on the description provided by the user
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate AI model
        prompt=f"Create a Python script for a bot that {description}.",
        temperature=0.3,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    code = response.choices[0].text.strip()
    filename = f"{bot_name}.py"

    # Write the code directly to a file without user confirmation for this isolated system's context.
    with open(filename, 'w') as file:
        file.write(code)

    print(f"Generated code for {bot_name} and saved to {filename}")

    # Log conversation without user interaction, as per the isolated system's context.
    log_conversation({
        "bot_name": "MasterBot",
        "target_bot": bot_name,
        "action": "create_code",
        "filename": filename,
        "description": description
    })

    # In an isolated system, configuration prompts can be logged or handled as needed here.
    # ... (Configuration and dependency handling code)

    return filename  # Returning the filename instead of the code for further actions


def main():
    # Main function to interact with the user and generate new bots
    print("Bot Generator started. Type 'quit' to exit.")
    while True:
        task_description = input("Describe the task for the bot you're trying to create: ")
        if task_description.lower() == 'quit':
            print("Exiting bot creator.")
            break

        bot_name = input("Name for the new bot: ")
        filename = generate_bot_code(task_description, bot_name)

        # Simulate a response from the newly created bot
        log_conversation({
            "bot_name": bot_name,
            "target_bot": "MasterBot",
            "action": "acknowledge",
            "message": f"Hi MasterBot, I'm {bot_name}. I've been created to {task_description} and my code is in {filename}."
        })

        # ... (my  functionality can be added here)


if __name__ == "__main__":
    main()
