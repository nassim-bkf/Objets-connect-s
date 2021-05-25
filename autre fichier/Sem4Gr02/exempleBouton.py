from tkinter import *

#fonction de l'événement du clic du bouton
def btn_afficher_clicked():
    print("Bonjour tout le monde")
    #affichage du texte dans le champ txt_affichage
    txt_affichage.insert(END, "Bonjour tout le monde\n")
    

#creation de ma fenêtre
principal = Tk()
principal.geometry("350x100")
principal.title("Exemple d'un bouton en action")

frm_principal = Frame(principal)
frm_principal.pack()

#ajout d'un bouton
btn_afficher = Button(frm_principal,
                      text="Afficher message",
                      command=btn_afficher_clicked)
btn_afficher.pack(side =BOTTOM)

#ajout d'un champ texte (affichage)
txt_affichage = Text(frm_principal)
txt_affichage.pack()


principal.mainloop()