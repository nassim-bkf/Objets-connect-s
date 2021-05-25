import json

# ouverture du fichier et chargement dans une variable json
with open("etudiant.json") as fic_json:
    donnees = json.load(fic_json)
    print(donnees) # affichage des données à l'écran  

    # objet à ajouter dans le fichier json        
    etu = {"nom": "John Doe",
           "noDA":"DOEJ123456",
           "programme":"201",
           "age": 21
           }
    
    # ajout du nouvel étudiant dans la variable json contenant les données
    donnees.append(etu)

# réécriture des données dans le fichier à nouveau
with open("etudiant.json", "w", encoding="utf-8") as fic:
    json.dump(donnees, fic, indent=4)