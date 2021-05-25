from tkinter import *

#création de la fenêtre
principal = Tk()
principal.geometry("350x100")
principal.title("Exemple d'un champ de saisie")

#ajout d'un cadre
frm_principal = Frame(principal)
frm_principal.pack()

#ajout étiquette et champ saisie usager
lbl_usager = Label(frm_principal, text="Nom d'utilisateur")
lbl_usager.grid(column=0, row=0)
ety_usager = Entry(frm_principal)
ety_usager.grid(column=1, row=0)

#ajout étiquette et champ saisie mot de passe
lbl_motpasse = Label(frm_principal, text="Mot de passe")
lbl_motpasse.grid(column=0, row=1)
ety_motpasse = Entry(frm_principal)
ety_motpasse.grid(column=1, row=1)


principal.mainloop()