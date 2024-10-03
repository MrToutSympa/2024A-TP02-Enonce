"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""     
import csv
import copy
########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
with open('collection_bibliotheque.csv', mode='r', newline='') as fichier:
    lecteur = csv.DictReader(fichier)
    next(lecteur, None)
    bibliotheque = {row.pop('cote_rangement'): row for row in lecteur}
print(bibliotheque)






########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici


with open('nouvelle_collection.csv', mode='r', newline='') as fichier:
    lecteur1 = csv.DictReader(fichier)
    next(lecteur1, None)
    new_bibliotheque = {row.pop('cote_rangement'): row for row in lecteur1}
bibliotheque_finale = {}


def merge_dicts(dict1, dict2):
    for d in (dict1, dict2):
        for k, v in d.items():
            if k in bibliotheque_finale and v in bibliotheque_finale.values():
                valeur = list(v.values())
                print(f"Le livre{k} {valeur[0]} de {valeur[1]} est deja dans le dictionnaire ")
            else:
                valeur = list(v.values())
                bibliotheque_finale[k] = v
                print(f"Le livre{k} {valeur[0]} de {valeur[1]} a ete ajoute avec succes ")


merge_dicts(bibliotheque, new_bibliotheque)




########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

copy_de_la_bibliotheque_finale = copy.deepcopy(bibliotheque_finale)

for cote, donnees in copy_de_la_bibliotheque_finale.items():
    if donnees['auteur'] == 'William Shakespeare':
        del bibliotheque_finale[cote]
        nouvelle_cote = 'W'+cote
        bibliotheque_finale[nouvelle_cote] = donnees
print(bibliotheque_finale)






########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






