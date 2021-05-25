import tkinter as tk

def chkbtn_afficher_clicked():
    print("Automne: " + str(chkbtn_var1.get()) + 
          " Hiver: " + str(chkbtn_var2.get()))

#création de la fenêtre
principal = tk.Tk()
principal.geometry('200x100')
frame = tk.Frame(principal)
frame.pack()

#déclaration variable pour les cases à cocher
chkbtn_var1 = tk.IntVar()
chkbtn_var2 = tk.IntVar()
#case à cocher avec fct pour afficher message de l'option
chkbtn_opt1 = tk.Checkbutton(frame, text = "Automne", variable = chkbtn_var1, 
                             command = chkbtn_afficher_clicked)
chkbtn_opt1.pack()
chkbtn_opt2 = tk.Checkbutton(frame, text = "Hiver", variable = chkbtn_var2, 
                             command = chkbtn_afficher_clicked)
chkbtn_opt2.pack()

principal.title("Exemple case à cocher")
principal.mainloop()