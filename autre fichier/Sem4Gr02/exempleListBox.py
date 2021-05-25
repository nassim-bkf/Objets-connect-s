from tkinter import *

def onSelect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    valeur = lst_ville.get(lst_ville.curselection())
    print("nom: " + str(index) + " valeur: " + valeur)

#creation de la fenetre
principal = Tk()
principal.geometry("200x200")
principal.title("Exemple de boîte de liste")

frm_principal = Frame(principal)
frm_principal.pack()

#ajout d'éléments dans une liste
lst_ville = Listbox(frm_principal)
lst_ville.insert(1, "Laval")
lst_ville.insert(2, "Montréal")
lst_ville.insert(3, "Québec")
lst_ville.insert(4, "Longueuil")
lst_ville.bind("<<ListboxSelect>>", onSelect)
lst_ville.pack()


principal.mainloop()


