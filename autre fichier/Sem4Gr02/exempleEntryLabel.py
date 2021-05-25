from tkinter import *

#création de la fenêtre
principal = Tk()
principal.geometry('350x100')

frame = Frame(principal)
frame.pack()

#ajout d'un étiquette 
lbl_usager = Label(frame, text="Nom d'utilisateur")
lbl_usager.grid(column=0, row=0)
#ajout d'un champ de saisie
ety_utilisateur = Entry(frame)
ety_utilisateur.grid(column=1, row=0)

#ajout pour mot de passe
lbl_motpasse = Label(frame, text="Mot de passe")
lbl_motpasse.grid(column=0, row=1)
ety_motpasse = Entry(frame)
ety_motpasse.grid(column=1, row=1)

principal.title("Exemple d'un champ de saisie")
principal.mainloop()