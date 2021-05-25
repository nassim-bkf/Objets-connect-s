from tkinter import *

# fonction pour l'événement du bouton Afficher
def btn_afficher_clicked():
    print("Bonjour " + ety_utilisateur.get())

#création de la fenêtre
principal = Tk()
principal.geometry('350x100')
#deux cadres : un pour le champ et un pour le bouton
frm_haut = Frame(principal)
frm_haut.pack(side=TOP)
frm_btn = Frame(principal)
frm_btn.pack()

#Étiquette, champ de saisie et bouton
lbl_usager = Label(frm_haut, text="Nom d'utilisateur")
lbl_usager.grid(column=0, row=0)
ety_utilisateur = Entry(frm_haut)
ety_utilisateur.grid(column=1, row=0)

btn_afficher = Button(frm_btn, 
                      text="Afficher message", 
                      command = btn_afficher_clicked)
btn_afficher.pack()

principal.title("Exemple d'un bouton en action")
principal.mainloop()