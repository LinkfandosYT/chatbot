import wikipedia
import subprocess

def get_definition(word, lang="fr"):
    try:
        if lang == "fr":
            wikipedia.set_lang("fr")
        elif lang == "en":
            wikipedia.set_lang("en")
        else:
            print("Langue non prise en charge.")
            return

        page = wikipedia.page(word)
        summary = page.summary
        print(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("La requête a plusieurs résultats possibles. Veuillez préciser :")
        options = e.options[:5]  # Limiter les options d'ambiguïté affichées
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
    except wikipedia.exceptions.PageError:
        print("Aucune page trouvée.")
    except Exception as e:
        print("Une erreur s'est produite lors de la recherche.")
        print(str(e))

def execute_program(program):
    try:
        subprocess.run(program, shell=True)
    except Exception as e:
        print("Une erreur s'est produite lors de l'exécution du programme.")
        print(str(e))

def chat():
    print("Bienvenue dans le chatbot !")
    print("Vous pouvez utiliser les commandes suivantes :")
    print("- definition <mot> <fr/en> : Rechercher une définition sur Wikipedia.")
    print("- execute <programme> : Exécuter un programme.")

    while True:
        user_input = input("Vous: ")

        if user_input.lower() == "quitter":
            print("Au revoir !")
            break

        # Analyser la commande
        parts = user_input.split(" ")
        command = parts[0]

        if command == "definition":
            if len(parts) >= 3:
                word = parts[1]
                lang = parts[2]
                get_definition(word, lang)
            else:
                print("Commande incorrecte. Format : definition <mot> <fr/en>")
        elif command == "execute":
            if len(parts) >= 2:
                program = " ".join(parts[1:])
                execute_program(program)
            else:
                print("Commande incorrecte. Format : execute <programme>")
        else:
            print("Commande non reconnue.")

# Démarrer le chatbot
chat()
