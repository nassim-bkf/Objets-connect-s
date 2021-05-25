from tkinter import *

principal = Tk()
principal.geometry("300x150")

#ajout de cadre (frame)
frm_principal = Frame(principal)

#ajustement automatique de la fenêtre
frm_principal.pack()

lbl_defaut = Label(frm_principal, text="Défaut")
lbl_defaut.pack()

#ajout cadre haut
frm_haut = Frame(principal)
frm_haut.pack(side=TOP)
lbl_haut = Label(frm_haut, text="Haut")
lbl_haut.pack()

#ajout cadre gauche
frm_gauche = Frame(principal)
frm_gauche.pack(side=LEFT)
lbl_gauche = Label(frm_gauche, text="Gauche")
lbl_gauche.pack()

#ajout cadre droite
frm_droite = Frame(principal)
frm_droite.pack(side=RIGHT)
lbl_droite = Label(frm_droite, text="Droite")
lbl_droite.pack()

#ajout cadre bas
frm_bas = Frame(principal)
frm_bas.pack(side=BOTTOM)
lbl_bas = Label(frm_bas, text="Bas")
lbl_bas.pack()


principal.mainloop()
