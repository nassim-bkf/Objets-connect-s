from tkinter import *
import tkinter as tk
from gpiozero import LED
from time import sleep


  
# Dictionnaire qui représente la charte
#la charte a été reprise dans le site suivant 'http://www.codebug.org.uk/learn/step/540/morsecode-alphabet/'

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
  

#Fonction qui a objectif de transmettre le message en code morse ainsi que le faire fonctionner avec une LED sur raspberryPi
def btn_transmettre_clicked():
    
    message = ety_a_cripter.get()
    message = message.upper()
    
    message_encryptee = ''
     
    for lettre in message:
        if lettre != ' ':
  
            message_encryptee += MORSE_CODE_DICT[lettre] + ' '
        else:


            message_encryptee += ' '
  
    ety_message_codee.delete(0, END)
    ety_message_codee.insert(INSERT, message_encryptee)
    
    # La LED qui est branchee dans le GPIO 14 sera allumé 0.2 seconde 
    # si la lettre du code morse est "." et 0.7 secondes si la lettre du code est "-"
    rouge = LED(14)
    for lettre in message_encryptee:
        if lettre == ".":
            rouge.on()
            sleep(0.2)
            rouge.off()
            sleep(0.2)
        elif lettre == "-":
            rouge.on()
            sleep(0.7)
            rouge.off()
            sleep(0.7)
        else:
            sleep(1)    
    
#foction qui fera quitter la fenetre si l'utilisteur clique sur "quitter"
def btn_quitter_clicked():
    principal.destroy()
    

    



#création de la fenêtre
principal = Tk()
principal.geometry("400x300")
#titre de la fenetre principale
principal.title("Code Morse")

#ajout d'un cadre
frm_principal = Frame(principal)
frm_principal.pack()

#boutton qu'on utilisera pour en faire une fonction qui encryptera les message en code Morse
btn_transmettre = Button(frm_principal, text="Transmettre", width=15, command = btn_transmettre_clicked)
btn_transmettre.grid(column=1, row=0)

#boutton qu'on utilisera pour en faire une fonction qui fera quitter la fenêtre.
btn_quitter = Button(frm_principal, text="Quitter",width=15 , command = btn_quitter_clicked )
btn_quitter.grid(column=1, row=1)

#Entré qui sera utilisé pour entrer le message qu'on veut encrypter. 
ety_a_cripter = Entry(frm_principal, width=27 )
ety_a_cripter.insert(0, "Message à coder:" )
ety_a_cripter.grid(column=0, row=0)

#entré ou le code Morse sera affiché.
ety_message_codee = Entry(frm_principal, width=27,fg = "red" )
ety_message_codee.insert(0, "Message en code Morse")
ety_message_codee.grid(column=0, row=1)



principal.mainloop()
