import tkinter as tk
from tkinter import messagebox

def btn_afficher_clicked():
    messagebox.showinfo("Message de bienvenue", 
                        "Bonjour tout le monde")

#création de la fenêtre
principal = tk.Tk()
principal.geometry('350x50')

frame = tk.Frame(principal)
frame.pack()

btn_afficher = tk.Button(frame, 
                         text="Afficher message", 
                      command = btn_afficher_clicked)
btn_afficher.pack()

principal.title("Exemple d'une boîte de message")
principal.mainloop()