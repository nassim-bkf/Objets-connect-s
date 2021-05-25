from tkinter import *
import codeMorseCodeSource
import tkinter as tk

# fonction pour l'événement du bouton Afficher



def action():
    message = ety_utilisateur.get()
    
    

#création de la fenêtre
principal = tk.Tk()
principal.geometry('400x300')
#deux cadres : un pour le champ et un pour le bouton
frame = Frame(principal)
frame.pack()
frm_btn = Frame(principal)
frm_btn.pack()


frm_haut = Frame(principal)
frm_haut.pack(side=TOP)
frm_btn = Frame(principal)
frm_btn.pack()
# message qui affiche le message à coder
ety_utilisateur = Entry(frame, width = 25)
ety_utilisateur.insert(0, "Message à coder:")
ety_utilisateur.pack(side=tk.LEFT)


btn_afficher = Button(frm_btn, 
                      text="Afficher message", command = action)
btn_afficher.pack()
btn_afficher.pack(side=tk.LEFT)



messageACoder = Entry(frame, width = 25)
messageACoder.insert(0, "Message en code Morse")
messageACoder.pack(padx = 5 , pady = 5)

#boutton qui affiche le message de quitter.

btn_afficher_quitter = Button(frm_btn, 
                      text="Quitter")
btn_afficher_quitter.pack()

#titre principale
principal.title("Code Morse")
principal.mainloop()