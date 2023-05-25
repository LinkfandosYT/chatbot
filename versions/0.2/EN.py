import wikipedia
import subprocess

def get_definition(word, lang="fr"):
    try:
        if lang == "fr":
            wikipedia.set_lang("fr")
        elif lang == "en":
            wikipedia.set_lang("en")
        else:
            print("Unsupported language.")
            return

        page = wikipedia.page(word)
        summary = page.summary
        print(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("The query has multiple possible results. Please specify:")
        options = e.options[:5]  # Limit the displayed ambiguity options
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
    except wikipedia.exceptions.PageError:
        print("No page found.")
    except Exception as e:
        print("An error occurred during the search.")
        print(str(e))

def execute_program(program):
    try:
        subprocess.run(program, shell=True)
    except Exception as e:
        print("An error occurred while executing the program.")
        print(str(e))

def chat():
    print("Welcome to the chatbot!")
    print("You can use the following commands:")
    print("- definition <word> <fr/en>: Look up a definition on Wikipedia.")
    print("- execute <program>: Execute a program.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Parse the command
        parts = user_input.split(" ")
        command = parts[0]

        if command == "definition":
            if len(parts) >= 3:
                word = parts[1]
                lang = parts[2]
                get_definition(word, lang)
            else:
                print("Incorrect command. Format: definition <word> <fr/en>")
        elif command == "execute":
            if len(parts) >= 2:
                program = " ".join(parts[1:])
                execute_program(program)
            else:
                print("Incorrect command. Format: execute <program>")
        else:
            print("Unrecognized command.")

# Start the chatbot
chat()
