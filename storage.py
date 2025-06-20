import os

from html_parser import read_html_file
from tags_validator import validate_tags
from content_editor import appliquer_corrections, ajouter_contenu, supprimer_contenu, modifier_contenu
from inspector import afficher_arborescence, afficher_statistiques_erreurs, afficher_contenu_balise

def afficher_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Charger un fichier HTML")
    print("2. Afficher l'arborescence des balises")
    print("3. Afficher les statistiques d'erreurs")
    print("4. Appliquer correction automatique")
    print("5. Ajouter du contenu")
    print("6. Supprimer du contenu")
    print("7. Modifier du contenu")
    print("8. Afficher le contenu d'une balise spécifique")
    print("9. Sauvegarder les modifications")
    print("0. Quitter")

def main():
    fichier_html = ""
    lignes = []
    corrections_appliquees = False

    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            fichier_html = input("Entrez le chemin du fichier HTML : ")
            if os.path.exists(fichier_html):
                lignes = lire_fichier_html("Fichier HTML_html")
                print("Fichier chargé avec succès.")
            else:
                print("Fichier introuvable.")

        elif choix == "2":
            if lignes:
                afficher_arborescence(lignes)
            else:
                print("Veuillez d'abord charger un fichier HTML.")

        elif choix == "3":
            if lignes:
                valider_balises(lignes)  # Affiche les erreurs détectées
                afficher_statistiques_erreurs(lignes)
            else:
                print("Veuillez d'abord charger un fichier HTML.")

        elif choix == "4":
            if lignes:
                lignes = appliquer_corrections(lignes)
                corrections_appliquees = True
                print("Corrections automatiques appliquées.")
            else:
                print("Veuillez d'abord charger un fichier HTML.")

        elif choix == "5":
            contenu = input("Contenu à ajouter (ex: <p>Bonjour</p>) : ")
            position = int(input("Position d'insertion (ligne, 0 pour début) : "))
            lignes = ajouter_contenu(lignes, contenu, position)
            print("Contenu ajouté.")

        elif choix == "6":
            position = int(input("Position de la ligne à supprimer : "))
            lignes = supprimer_contenu(lignes, position)
            print("Ligne supprimée.")

        elif choix == "7":
            position = int(input("Position de la ligne à modifier : "))
            nouveau = input("Nouveau contenu : ")
            lignes = modifier_contenu(lignes, position, nouveau)
            print("Ligne modifiée.")

        elif choix == "8":
            balise = input("Nom de la balise à afficher : ")
            afficher_contenu_balise(lignes, balise)

        elif choix == "9":
            if lignes:
                chemin_sortie = input("Nom du nouveau fichier à sauvegarder (ex: fichier_corrige.html) : ")
                with open(chemin_sortie, "w", encoding="utf-8") as f:
                    f.write("\n".join(lignes))
                print(f"Modifications sauvegardées dans {chemin_sortie}.")
            else:
                print("Aucun contenu à sauvegarder.")

        elif choix == "0":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
