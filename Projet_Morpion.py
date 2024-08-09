##----- Définition des Variables globales -----##
Tab2Tab= [[0,0,0],[0,0,0],[0,0,0]]

joueur = 1                              # On commence par le joueur n°1
n = 1                                   # Premier tour de jeu
somme = 0                               # Somme des cases
compteur1=0                             #Cette variable représente le nombre de victoire du joueur 1.
compteur2=0                             #Cette variable représente le nombre de victoire du joueur 2.

##----- Définitions des fonctions utilisées -----##

#Cette fonction affiche à l'écran chaque ligne d'un tableau.
def affichage(tableau):
    n = len(tableau)
    for i in range(n):
        print(tableau[i])



#Cette fonction renvoie la case choisi par le joueur
def demande(numero):
    if numero == 1:
        print('Au tour du joueur n°1 !')
    else:
        print('Au tour du joueur n°2 !')
    ligne = int(input('Numéro de ligne ? '))
    colonne = int(input('Numéro de colonne ? '))
    return [ligne, colonne]

#Cette fonction calcule les sommes de chaque ligne/colonne/diagonale pour vérifier si 3 cases alignés sont remplit avec la même valeur.
def verif(tableau):
    sommes = [0,0,0,0,0,0,0,0]          # Il y a 8 sommes à vérifier
    # Les lignes :
    sommes[0] = sum(tableau[0])
    sommes[1] = sum(tableau[1])
    sommes[2] = sum(tableau[2])
    # Les colonnes
    sommes[3] = tableau[0][0]+tableau[1][0]+tableau[2][0]
    sommes[4] = tableau[0][1]+tableau[1][1]+tableau[2][1]
    sommes[5] = tableau[0][2]+tableau[1][2]+tableau[2][2]
    # Les diagonales
    sommes[6] = tableau[0][0]+tableau[1][1]+tableau[2][2]
    sommes[7] = tableau[0][2]+tableau[1][1]+tableau[2][0]

#Elle renvoie le n° du joueur gagnant.
    for i in range(8):                  # Parcours des sommes
        if sommes[i] == 3:
            return 1                    # Joueur 1 sera 1
        elif sommes[i] == -3:
            return -1                   #Joueur 2 sera -1
    return 0                            # Cela correspond à une case vide

#Cette fonction demande au joueur si il souhaite effectuer une nouvelle partie.
def Rejouer():
    Tab2Tab= [[0,0,0],[0,0,0],[0,0,0]]
    rejouer=input('Voulez-vous faire une nouvelle partie? (la réponse doit être oui ou non):')
    if rejouer=='oui':
        Morpion()

#Cette fonction affiche le score cummulé de toutes les parties pour chaque joueur.
def AffichageScore():
    print('Victoires joueur 1:') and print (compteur1)
    print('Victoires joueur 2:') and print (compteur2)
#Elle définit le vainqueur.
    if compteur1>compteur2:
        print('Le joueur1 a gagné')
    elif compteur2>compteur1:
        print('Le joueur2 a gagné')
    else:
        print('Egalité')

##----- Fonction principale -----##
#Cette Fonction représente le déroulement d'une partie de Morpion.

def Morpion():
    Tab2Tab= [[0,0,0],[0,0,0],[0,0,0]]
    affichage(Tab2Tab)
    joueur = 1
    n = 1
    somme = 0
    compteur1=0
    compteur2=0

    while somme == 0 and n <= 9:
        [ligne, colonne] = demande(joueur)
        while Tab2Tab[ligne][colonne] != 0:   # Recherche d'une case vide
            print('Case occupée')
            [ligne, colonne] = demande(joueur)
        Tab2Tab[ligne][colonne] = joueur
        affichage(Tab2Tab)

        somme = verif(Tab2Tab)                # Vérification de l'alignement
        joueur = -joueur                    # Passage au joueur suivant
        n += 1                              # Passage au tour suivant

    if somme == 1:
        print('Bravo joueur 1 !')
        compteur1=compteur1+1
    elif somme == -1:
        print('Bravo joueur 2 !')
        compteur2=compteur2+1
    else:
        print('Match nul !')

    Rejouer()
    AffichageScore()

Morpion()
