import tkinter as tk

def btn_afficher_clicked():
    print("index: " + str(lst_cours.curselection()))
    print("item: " + str(lst_cours.get(lst_cours.curselection())))

#création de la fenêtre
principal = tk.Tk()
principal.geometry('200x150')
lbl_cours = tk.Label(principal, text = "Liste des cours")
lbl_cours.pack()

#ajout d'éléments dans la liste 
lst_cours = tk.Listbox(principal, height= 5)
lst_cours.insert(1, "Interface")
lst_cours.insert(2, "IoT")
lst_cours.insert(3, "Base de données")
lst_cours.insert(4, "App. Mobiles")
lst_cours.pack()

frm_p = tk.Frame(principal)
frm_p.pack()
btn_afficher = tk.Button(frm_p, text="Soumettre", 
                         command = btn_afficher_clicked)
btn_afficher.pack()

principal.title("Exemple case à cocher")
principal.mainloop()