import random as r #On importe la biblioèque Ramdom avec comme alias la lettre r

# Partie 1 : gagnant aléatoire selon une liste
#question 1
def JeuDebutant(n1,n2,n3):
    """Fonction qui renvoie une liste composé du nombre de fois qu'on veut de baton"""
    assert type(n1) == int,"il faut que ça soit un entier s'il te plait"
    assert type(n2) == int,"il faut que ça soit un entier s'il te plait"
    liste = []
    for g in range(n1):
            liste.append("G")
    for m in range(n2):
            liste.append("M")
    for p in range(n3):
            liste.append("P")
    return liste



#Question n °2:
def distribution():
    """Fonction qui distribue les batons de façon ramdom et doit contenir 18 baton en total """
    somme = 0
    listetotal = []
    L1= []
    L2=[]
    assert type(L1) == list,"il faut que ça soit une liste s'il te plait"
    assert type(L1) == list,"il faut que ça soit une liste s'il te plait"
    listetotal = JeuDebutant(2,6,10)
    for k in listetotal:
        d = r.randint(1, 2)
        if d == 2:
            if len(L1) < 9:
                L1.append(k)
            else:
                L2.append(k)
        else:
            if len(L2) < 9:
                L2.append(k)
            else:
                L1.append(k)
    return L1,L2
    

#Question n°3:
def compteDebutant(L):
    """Fonction qui prend en paramètre une liste de bâton L et renvoie un dictionnaire,
indiquant le nombre de point et le nombre de baton de chaque type dans la liste"""
    assert type(L) == list,"il faut que ça soit une liste s'il te plait"
    compteur = 0
    nombreG = 0
    nombreM = 0
    nombreP = 0
    for k in L:
        if k =="G":
            compteur = compteur + 3
            nombreG = nombreG + 1
        elif k =="M":
            compteur = compteur + 2
            nombreM = nombreM + 1
        elif k =="P":
            compteur = compteur + 1
            nombreP = nombreP + 1 
        else:
            compteur = compteur + 0
    dicoliste ={"points": compteur,"G": nombreG, "M": nombreM, "P": nombreP}
    return dicoliste


#Question n°4:


def gagnanDebutant(L1,L2):
    assert type(L1)==list,"il faut que ça soit une liste s'il te plait"
    assert type(L2) == list,"il faut que ça soit une liste s'il te plait"
    L1point= compteDebutant(L1)
    L2point= compteDebutant(L2)
    if L1point["points"] > L2point["points"]:
        return "Le joueur n°1 a gagné"
    elif L2point["points"] > L1point["points"]:
        return "le joueur n°2 a gagné"
    else:
        return "Math nul"
# Partie 2 : 1v1 joueur
def creationJeu():
    """Fonction qui renvoie une liste de 18 bouts de bois composée de façon aléatoire entre les petits, les moyens et les grands"""
    somme = 0
    while somme != 18:
         n1 = r.randint(0, 9)
         n2 = r.randint(0, 9)
         n3 = r.randint(0, 9)
         somme = n1 + n2 + n3
    listedebut= JeuDebutant(n1,n2,n3)
    assert len(listedebut) == 18,"il faut que ça soit une liste de 18 élément"
    return listedebut


def creationdeuxliste():
    """Cette fonction créer deux listes aléatoires d'une liste former auparavant"""
    L1= []
    L2= []
    listetotal = creationJeu()
    for k in listetotal:
        pileface = r.randint(1, 2) #si le chiffre choisi par ramdom c'est 1 , il le met dans la la liste1. Si le chiffre choisi par ramdom c'est 2, il le met dans la liste 2.
        if pileface == 2:
            if len(L1) < 9:
                L1.append(k)
            else: # si la liste 1 est complete il met le reste dans la liste 2
                L2.append(k)
        else:
            if len(L2) < 9: 
                L2.append(k)
            else: # si la liste 2 est complete il met le reste dans la liste 1
                L1.append(k)
    return L1,L2
    assert type(L1)==list,"il faut que ça soit une liste s'il te plait"
    assert type(L2)==list,"il faut que ça soit une liste s'il te plait"
def pointj1(lettreJ1,L1,scoreJ1,scoreJ2):
    """Cette fonction permet de compter le nombre de point du Joueur 1"""
    if lettreJ1 == "G":
        scoreJ1["point"] = 3
        L1.remove("G")
    elif lettreJ1 == "M":
        scoreJ1["point"] = 2
        L1.remove("M")
    elif lettreJ1 == "P":
        scoreJ1["point"] = 1
        L1.remove("P")
    assert type(scoreJ1) == dict, "Il faut que ça soit un dictionnaire"
    assert type(L1) == list, "Il faut que ça soit une liste"
    return scoreJ1,L1

def pointj2(lettreJ2,L2,scoreJ2):
    """Cette fonction permet de compter le nombre de point du Joueur 2"""
    if lettreJ2 == "G":
        scoreJ2["point"] = 3
        L2.remove("G")
    elif lettreJ2 == "M":
        scoreJ2["point"] = 2
        L2.remove("M")
    elif lettreJ2 == "P":
        scoreJ2["point"] = 1
        L2.remove("P")
    assert type(scoreJ2) == dict, "Il faut que ça soit un dictionnaire"
    assert type(L2) == list, "Il faut que ça soit une liste"
    return scoreJ2,L2

def verifpoint(L1,lettreJ1,L2,lettreJ2,tour,scoreJ1,scoreJ2):
    """Fonction qui vérifie le nombre de point de chaque joueur et déclare le gagnant et  décide qui commence"""
    if scoreJ1["point"] > scoreJ2["point"]:
        print("Le joueur 1 a gagné par conséquent il commence en premier")
        tour = "j1"
        scoreJ1["pointstotal"] = scoreJ1["pointstotal"] + scoreJ1["point"] + scoreJ2["point"]
        commenceJ1(L1,L2,tour, scoreJ1,scoreJ2)
    elif scoreJ1["point"] < scoreJ2["point"]:
        print("Le joueur 2 a gagné par conséquent il commence en premier")
        tour = "j2"
        scoreJ2["pointstotal"] = scoreJ2["pointstotal"] + scoreJ1["point"] + scoreJ2["point"]
        commenceJ2(L1,L2,tour, scoreJ1,scoreJ2)
    else:
        matchnul(scoreJ1,scoreJ2,L1,L2,tour)
    assert scoreJ1["point"] != 0 , "Il faut que ça soit différents de 0"
    assert scoreJ2["point"] != 0,  "Il faut que ça soit différents de 0"
    return scoreJ1,scoreJ2,L1,L2

def matchnul(scoreJ1,scoreJ2,L1,L2,tour):
    """cette fonction traite le cas ou les points sont égaux et match nul et décide qui commence"""
    if scoreJ1["point"] == scoreJ2["point"]:
        scoreJ1["pointstotal"] == scoreJ1["pointstotal"] - scoreJ1["point"] and scoreJ2["pointstotal"] == scoreJ2["pointstotal"] -scoreJ2["point"]
        print("Math Nul")
        if tour == "j1":
            tour = "j2"
            print("Joueur 2 c'est a ton tour")
            commenceJ2(L1,L2,tour,scoreJ1,scoreJ2)
        elif tour == "j2":
            tour = "j1"
            print("Joueur 1 c'est a ton tour")
            commenceJ1(L1,L2,tour,scoreJ1,scoreJ2)
    assert type(scoreJ1) == dict , "Il faut que ça soit un dictionnaire"
    assert type(scoreJ2) == dict,  "Il faut que ça soit un dictionnaire"



def commenceJ1(L1,L2,tour,scoreJ1,scoreJ2):
    """Cette fonction a pour but de faire commencer le joueur 1"""
    if veriftailleliste(L1,L2,scoreJ1,scoreJ2)== "true":
        pass
    else:
        lettreJ1 = input("Joueur 1: Tapez une lettre:")
        lettreJ2 = input("Joueur 2: Tapez une lettre:")
        assert type(lettreJ1) == str, "Il faut que ça soit une chaine de caractère"
        assert type(lettreJ2) == str, "Il faut que ça soit une chaine de caractère"
        assert lettreJ1 == "G" or lettreJ1 == "M" or lettreJ1 == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        assert lettreJ2 == "G" or lettreJ2 == "M" or lettreJ2 == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        pointj1(lettreJ1,L1,scoreJ1,scoreJ2)
        pointj2(lettreJ2,L2,scoreJ2)
        verifpoint(L1,lettreJ1,L2,lettreJ2,tour,scoreJ1,scoreJ2)
   
    
def commenceJ2(L1,L2,tour,scoreJ1,scoreJ2):
    """Cette fonction a pour but de faire commencer le joueur 2"""
    if veriftailleliste(L1,L2,scoreJ1,scoreJ2)== "true":
        pass
    else:
        lettreJ2 = input("Joueur 2: Tapez une lettre:")
        lettreJ1 = input("Joueur 1: Tapez une lettre:")
        assert type(lettreJ1) == str, "Il faut que ça soit une chaine de caractère"
        assert type(lettreJ2) == str, "Il faut que ça soit une chaine de caractère"
        assert lettreJ1 == "G" or lettreJ1 == "M" or lettreJ1 == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        assert lettreJ2 == "G" or lettreJ2 == "M" or lettreJ2 == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        pointj1(lettreJ1,L1,scoreJ1,scoreJ2)
        pointj2(lettreJ2,L2,scoreJ2)
        verifpoint(L1,lettreJ1,L2,lettreJ2,tour,scoreJ1,scoreJ2)
    
    



def veriftailleliste(L1,L2,scoreJ1,scoreJ2):
    """cette fonction sert a verifier si il reste des éléments dans la liste ou non """
     
    if len(L1) == 0 or len(L2) == 0:
        assert len(L1) == 0, "Ta liste n'est pas vide"
        assert len(L2) == 0, "Ta liste n'est pas vide"
        if scoreJ1["pointstotal"] > scoreJ2["pointstotal"]:
            print("Joueur 1 a gagné ", scoreJ1["pointstotal"], "à", scoreJ2["pointstotal"])
        elif scoreJ1["pointstotal"] < scoreJ2["pointstotal"]:
            print("Joueur 2 a gagné ", scoreJ2["pointstotal"], "à", scoreJ1["pointstotal"])
        else :
            print("Match nul ", scoreJ1["pointstotal"], "à", scoreJ2["pointstotal"])
        return "true"
def deroulementJeu():
    """Fonction qui affiche au début deux listes de bouts de bois, puis qui déroule le jeux demandant au fur et à mesure à chaque joueur ce qu'il joue"""
    L1 = creationdeuxliste()[0]
    L2 = creationdeuxliste()[1]
    assert len(L1) == 9, "Ta liste ne contient pas 9 éléments"
    assert len(L2) == 9, "Ta liste ne contient pas 9 éléments"
    scoreJ1 ={"pointstotal": 0, "point": 0}
    scoreJ2 = {"pointstotal": 0, "point": 0}
    print("Joueur 1 :", L1,"Joueur 2 :" ,L2)
    tour = "j1"
    commenceJ1(L1,L2,tour,scoreJ1,scoreJ2)

#Partie 3 : un joueur contre l'ordinateur imbattable

def moiContremachine():
    """Cette fonction affiche la liste de bout de bois du joueur et fait jouer en premier le bot"""
    listetotal = creationdeuxliste()
    listej1 = listetotal[0]
    listemachine = listetotal[1]
    assert type(listej1) == list, "il faut que ça soit une liste"
    assert type(listemachine) == list, "il faut que ça soit une liste"
    print("Liste Joueur:",listej1)
    tour = "bot"
    lettrebot = r.choice(listemachine)
    lettrej1 = input("Joueur 1: Tapez une lettre:")
    return lettrej1, lettrebot,listej1,listemachine,tour

def pointmachine(listemachine,lettrebot,scoremachine):
    """cette fonction compte les points de la machine"""
    if lettrebot == "G":
        scoremachine["point"] = 3
        listemachine.remove("G")
    elif lettrebot == "M":
        scoremachine["point"] = 2
        listemachine.remove("M")
    elif lettrebot == "P":
        scoremachine["point"] = 1
        listemachine.remove("P")
    assert type(scoremachine) == dict, "il faut que ça soit un dictionnaire"
    assert type(listemachine) == list, "il faut que ça soit une liste"
    return scoremachine,listemachine


def pointjoueur1machine(listej1,lettrej1,scoreJ1):
    """cette fonction compte les points du joueur qui joue contre la machine"""
    if lettrej1 == "G":
        scoreJ1["point"] = 3
        listej1.remove("G")
    elif lettrej1 == "M":
        scoreJ1["point"] = 2
        listej1.remove("M")
    elif lettrej1 == "P":
        scoreJ1["point"] = 1
        listej1.remove("P")
    assert type(scoreJ1) == dict, "il faut que ça soit un dictionnaire"
    assert type(listej1) == list, "il faut que ça soit une liste"
    return scoreJ1,listej1
        
def commencemachine(listej1,listemachine,tour,scoreJ1,scoremachine):
    """Cette fonction a pour but de faire commencer la machine"""
    if veriftaillelistemachine(listej1,listemachine,scoreJ1,scoremachine)== "true":
        pass
    else:
        lettrebot = r.choice(listemachine)
        lettrej1 = input("Joueur 1: Tapez une lettre:")
        assert type(lettrej1) == str, "Il faut que ça soit une chaine de caractère"
        assert type(lettrebot) == str, "Il faut que ça soit une chaine de caractère"
        assert lettrebot == "G" or lettrebot == "M" or lettrebot == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        assert lettrej1 == "G" or lettrej1 == "M" or lettrej1 == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        pointmachine(listemachine,lettrebot,scoremachine)
        pointjoueur1machine(listej1,lettrej1,scoreJ1)
        verifpointmachine(listej1,lettrej1,listemachine,lettrebot,tour,scoreJ1,scoremachine)

def intelligentemachine(lettrej1,listemachine):
    """Cette fonction permet a la machine de choisir meilleur coup a jouer pour gagner contre l'humain"""
    bislettrebot = "r"
    assert type(lettrej1) == str, "il faut que ça soit une chaine de caractère"
    assert type(listemachine) == list,"il faut que ça soit une liste"
    if lettrej1 == "P":
        for lettre in listemachine:
            bislettrebot = lettre
            if bislettrebot == "M":
                return "M"
        if bislettrebot =="P":
            return "P"
        elif bislettrebot =="G":
            return "G"
    elif lettrej1 == "G":
        for lettre in listemachine:
            bislettrebot = lettre
            if bislettrebot == "G":
                return "G"
        if bislettrebot =="P":
            return "P"
        elif bislettrebot =="M":
            return "M"
    elif lettrej1 == "M":
        for lettre in listemachine:
            bislettrebot = lettre
            if bislettrebot == "G":
                return "G"
        if bislettrebot =="M":
            return "M"
        elif bislettrebot =="P":
            return "P"
        
def commenceJ1machine(listej1,listemachine,tour,scoreJ1,scoremachine):
    """Cette fonction a pour but de faire commencer le joueur 1"""
    if veriftaillelistemachine(listej1,listemachine,scoreJ1,scoremachine)== "true":
        pass
    else:
        lettrej1 = input("Joueur 1: Tapez une lettre:")
        lettrebot = intelligentemachine(lettrej1,listemachine)
        assert type(lettrej1) == str, "Il faut que ça soit une chaine de caractère"
        assert type(lettrebot) == str, "Il faut que ça soit une chaine de caractère"
        assert lettrebot == "G" or lettrebot == "M" or lettrebot == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        assert lettrej1 == "G" or lettrej1 == "M" or lettrej1 == "P", "Il faut que ça soit soit un G , soit un M ou un p"
        pointjoueur1machine(listej1,lettrej1,scoreJ1)
        pointmachine(listemachine,lettrebot,scoremachine)
        verifpointmachine(listej1,lettrej1,listemachine,lettrebot,tour,scoreJ1,scoremachine)


def verifpointmachine(listej1,lettrej1,listemachine,lettrebot,tour,scoreJ1,scoremachine):
    """Fonction qui vérifie le nombre de point de chaque jouer"""
    if scoreJ1["point"] > scoremachine["point"]:
        print("Le joueur 1 a gagné par conséquent il commence en premier")
        tour = "j1"
        scoreJ1["pointstotal"] = scoreJ1["pointstotal"] + scoreJ1["point"] + scoremachine["point"]
        commenceJ1machine(listej1,listemachine,tour,scoreJ1,scoremachine)
    elif scoreJ1["point"] < scoremachine["point"]:
        print("la machine a gagné par conséquent il commence en premier")
        tour = "bot"
        scoremachine["pointstotal"] = scoremachine["pointstotal"] + scoreJ1["point"] + scoremachine["point"]
        commencemachine(listej1,listemachine,tour,scoreJ1,scoremachine)
    else:
        matchnulmachine(scoreJ1,scoremachine,listej1,listemachine,tour)
    assert scoreJ1["point"] != 0 , "Il faut que ça soit différents de 0"
    assert scoremachine["point"] != 0,  "Il faut que ça soit différents de 0"
    return scoreJ1,scoremachine,listej1,listemachine,tour

def matchnulmachine(scoreJ1,scoremachine,listej1,listemachine,tour):
    """cette fonction traite le cas ou les points sont égaux et match nul et décide qui commence"""
    if scoreJ1["point"] == scoremachine["point"]:
        scoreJ1["pointstotal"] == scoreJ1["pointstotal"] - scoreJ1["point"] and scoremachine["pointstotal"] == scoremachine["pointstotal"] -scoremachine["point"]
        print("Math Nul")
        if tour == "j1":
            tour = "bot"
            print("bot c'est à ton tour")
            commencemachine(listej1,listemachine,tour,scoreJ1,scoremachine)
        elif tour == "bot":
            tour = "j1"
            print("Joueur 1 c'est à ton tour")
            commenceJ1machine(listej1,listemachine,tour,scoreJ1,scoremachine)
    assert type(scoreJ1) == dict , "Il faut que ça soit un dictionnaire"
    assert type(scoremachine) == dict,  "Il faut que ça soit un dictionnaire"

def veriftaillelistemachine(listej1,listemachine,scoreJ1,scoremachine):
    """cette fonction permet de verifier ci il reste des éléments dans les listes """
    if len(listej1) == 0 or len(listemachine) == 0:
        assert len(listej1) == 0, "Ta liste n'est pas vide"
        assert len(listemachine) == 0, "Ta liste n'est pas vide"
        if scoreJ1["pointstotal"] > scoremachine["pointstotal"]:
            print("Joueur 1 a gagné ", scoreJ1["pointstotal"], "à", scoremachine["pointstotal"])
        elif scoreJ1["pointstotal"] < scoremachine["pointstotal"]:
            print("la machine a gagné ", scoremachine["pointstotal"], "à", scoreJ1["pointstotal"])
        else :
            print("Match nul ", scoreJ1["pointstotal"], "à", scoremachine["pointstotal"])
        return "true"


def moiContremachine2():
    """ Cette fonction permet de lancer le jeux contre la machine"""
    scoreJ1 = {"pointstotal": 0, "point": 0}
    scoremachine = {"pointstotal": 0, "point": 0}
    assert scoreJ1["pointstotal"] == 0 , "Il faut que ça soit les scores soit égales a 0"
    assert scoremachine["pointstotal"] == 0,  "Il faut que ça soit les scores soit égales a 0"
    debut = moiContremachine()
    lettrej1, lettrebot,listej1,listemachine,tour = debut[0],debut[1],debut[2],debut[3],debut[4]
    pointmachine(listemachine,lettrebot,scoremachine)
    pointjoueur1machine(listej1,lettrej1,scoreJ1)
    verifpointmachine(listej1,lettrej1,listemachine,lettrebot,tour,scoreJ1,scoremachine)
    
    
