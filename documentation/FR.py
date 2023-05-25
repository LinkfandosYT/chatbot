import wikipediaapi
import subprocess


def search_definition(keyword):
    wiki_wiki = wikipediaapi.Wikipedia('fr')
    page_py = wiki_wiki.page(keyword)
    if page_py.exists():
        return page_py.summary
    else:
        return None


def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output


def chat():
    print("Bonjour ! Je suis un chatbot qui peut vous donner des définitions et exécuter des commandes sur votre PC.")

    while True:
        user_input = input("Vous: ")

        if user_input.lower() == "quitter":
            print("Au revoir !")
            break

        if user_input.startswith("definition"):
            _, keyword = user_input.split(" ", 1)
            definition = search_definition(keyword)
            if definition:
                print("Chatbot: La définition de", keyword, "est :", definition)
            else:
                print("Chatbot: Je n'ai pas trouvé de définition pour", keyword)
        elif user_input.startswith("execute"):
            _, command = user_input.split(" ", 1)
            output = execute_command(command)
            print("Chatbot: Résultat de la commande :", output)
        else:
            print("Chatbot: Je suis désolé, je ne comprends pas. Pouvez-vous reformuler votre question ?")


chat()
