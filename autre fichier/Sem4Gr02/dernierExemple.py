from tkinter import *

def btn_afficher_clicked():
    print("Bonjour " + ety_utilisateur.get())

principal = Tk()
principal.geometry('350x100')

frame = Frame(principal)
frame.pack()
#deux cadres : un pour le champ et un pour le bouton


frm_haut = Frame(principal)
frm_haut.pack(side=TOP)
frm_btn = Frame(principal)
frm_btn.pack()

messageACoder = Entry(frm_haut)
messageACoder.insert(0, "Message à coder")
messageACoder.grid(column=1, row=0)
btn_afficher = Button(frm_btn, 
                      text="Transmettre")
btn_afficher.pack()





frm_bas = Frame(principal)
frm_bas.pack(side=TOP)
frm_bouton = Frame(principal)
frm_bouton.pack()

messageCode = Entry(frm_haut)
messageCode.insert(0, "Message codé")
messageCode.grid(column=1, row=0)
btn_afficher = Button(frm_bouton, 
                      text="Quitter")
btn_afficher.pack()


principal.title("exemlpe")
principal.mainloop()