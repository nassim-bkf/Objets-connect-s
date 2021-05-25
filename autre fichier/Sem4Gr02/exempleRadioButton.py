import tkinter as tk

def rbtn_afficher_clicked():
    selection = "Vous avez sélectionné l'option " + str(rbtn_var.get())
    lbl_afficher.config(text = selection)

#création de la fenêtre
principal = tk.Tk()
principal.geometry('200x100')
frame = tk.Frame(principal)
frame.pack()

#déclaration variable pour le bouton radio
rbtn_var = tk.IntVar()
#boutons radios avec fct pour afficher message de l'option
rbtn_opt1 = tk.Radiobutton(frame, text = "Option 1", variable = rbtn_var, 
                           value= 1, command = rbtn_afficher_clicked)
rbtn_opt1.pack()
rbtn_opt2 = tk.Radiobutton(frame, text = "Option 2", variable = rbtn_var, 
                           value= 2, command = rbtn_afficher_clicked)
rbtn_opt2.pack()

lbl_afficher = tk.Label(principal)
lbl_afficher.pack()

principal.title("Exemple boutons radio")
principal.mainloop()