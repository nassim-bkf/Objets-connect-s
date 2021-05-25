from tkinter import *

fenetre = Tk()

fenetre.title("Exemple d'une fenêtre")

fenetre.geometry("400x250")

# ajout d'étiquettes
lbl_nom = Label(fenetre, text="Nom de la personne")
#positionnement de l'étiquette
lbl_nom.grid(column=0, row=0)

lbl_age = Label(fenetre, text="Age", font=("Arial Bold", 20))
#positionnement de l'étiquette
lbl_age.grid(column=1, row=1, sticky=W)


fenetre.mainloop() 