import tkinter as t
import time  as time
from skourrouproject import*
def boutonfinal():
    """Fonction qui exécute d'autre fonction pour pouvoir affiche les batons et le gagnant"""
    canvagagnant.delete("all")
    labelgagnant= t.Label(fenetre,width=50,height=3, font=('Times','50'))
    Listetotal = distribution()
    L1,L2 = Listetotal[0], Listetotal[1]
    battonliste(L1,L2)
    gagnant = gagnanDebutant(L1,L2)
    canvagagnant.create_text(200, 100, text=gagnant, fill="white", font=('Helvetica 15 bold'))
def battonliste(L1,L2):
    """Affiche les baton de la liste 1 et 2"""
    canvaj1.delete("all")
    canvaj2.delete("all")
    compteurl1 = 1
    compteurl2 = 1
    for k in L1:
        if k == "G":
            canvaj1.create_line(compteurl1 * 40 + 2, 0, compteurl1 * 40 + 2, 400, fill ='green',width=20)
            compteurl1 = compteurl1 + 1
        elif k == "M":
            canvaj1.create_line(compteurl1 * 40 + 2, 100, compteurl1 * 40 + 2, 400, fill ='orange',width=20)
            compteurl1 = compteurl1 + 1
        elif k =="P":
            canvaj1.create_line(compteurl1 * 40 + 2 , 150, compteurl1 * 40 + 2, 400, fill ='red',width=20)
            compteurl1 = compteurl1 + 1
    batonL2(L2,compteurl2)
def batonL2(L2,compteurl2):
    """Cette fonction dessine les batons de la liste 2"""
    for k in L2:
        if k == "G":
            canvaj2.create_line(compteurl2 * 40 + 2, 0, compteurl2 * 40 + 2, 400, fill ='green',width=20)
            compteurl2 = compteurl2 + 1
        elif k == "M":
            canvaj2.create_line(compteurl2 * 40 + 2, 100, compteurl2 * 40 + 2, 400, fill ='orange',width=20)
            compteurl2 = compteurl2 + 1
        elif k =="P":
            canvaj2.create_line(compteurl2 * 40 + 2 , 150, compteurl2 * 40 + 2, 400, fill ='red',width=20)
            compteurl2 = compteurl2 + 1


fenetre = t.Tk()
canvaj1 = t.Canvas(fenetre, width =400, height =400, bg ='#EEEEEE')
canvaj2 = t.Canvas(fenetre, width =400, height =400, bg ='#EEEEEE')
canvagagnant = t.Canvas(fenetre, width =400, height =200, bg ='#052A19')
fenetre.configure(bg = '#00A127')
fenetre.title("Projet NSI - Parti 1 Tkinter")
etiquette=t.Label(fenetre,text="Jeux du skourrou",width=100,height=2,bg="#052A19",fg="white", font=('Times','50'))
etiquette.pack()
j1 = t.Canvas(fenetre, width =200, height =100, bg ='#052A19')
j2 = t.Canvas(fenetre, width =200, height =100, bg ='#052A19')
canvaj1.pack(side ='left')
canvaj2.pack(side ='right')
j1.create_text(100, 50, text="Joueur 1", fill="white", font=('Helvetica 15 bold'))
j2.create_text(100, 50, text="Joueur 2", fill="white", font=('Helvetica 15 bold'))
j1.pack(side ='left')
j2.pack(side ='right')
canvagagnant.pack(side ='top')
bouton1=t.Button(text='Commencer',height = 5,width = 20,command= boutonfinal) # création d'un bouton
bouton1.pack(side='bottom')
fenetre.mainloop()
    


        
