import time
import tkinter
from tkinter import*
from tkinter import messagebox
from time import strftime

okcliqué = {'cliqué': False}
historique = True
print("cela ne devrait pas s'écrire")

with open("log.txt", "a") as fichier:
    fichier.truncate(0)

def ajournercpu():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    lecturecpu = int(tempFile.read())
    tempcpu.config(text=lecturecpu/1000)
    if lecturecpu/1000 > 89:
        cpuhealth.config(text="Overheated",bg="red")
    else:
        if lecturecpu/1000 > 59:
            cpuhealth.config(text="Normal",bg="orange")
        else:
            cpuhealth.config(text="Good",bg="green")
    if int(lecturecpu/1000) > 90:
        if okcliqué['cliqué'] == False:
            messagebox.showwarning('Attention', 'La température a dépassé les 90°C !')
            okcliqué['cliqué'] = True
    if historique == True:
        with open("log.txt", "a") as fichier:
            fichier.write(f"\n{strftime('%d-%b-%y/%H:%M:%S')}- - - - - - -Température CPU ==>{lecturecpu/1000}°C")


    tempcpu.after(100, ajournercpu)


def fermerfenetre():
    root.destroy()


couleurpardef = {'couleur': 2}


def changercouleur():
    if couleurpardef["couleur"] == 1:
        couleurpardef["couleur"] = 2
        # action:
        print("C sombre")
        root.config(background=couleur1sombre)
        superframe.config(background=couleur2sombre)
        framegeneralecpu.config(background=couleur2sombre)
        framegeneralegpu.config(background=couleur2sombre)
        framecpu.config(background=couleur2sombre)
        framegpu.config(background=couleur2sombre)
        titrecpu.config(background=couleur2sombre)
        titregpu.config(background=couleur2sombre)
        return
    else:
        if couleurpardef["couleur"] == 2:
            couleurpardef["couleur"] = 1
            # action:
            print("C clair")
            root.config(background=couleur1clair)
            superframe.config(background=couleur2clair)
            framegeneralecpu.config(background=couleur2clair)
            framegeneralegpu.config(background=couleur2clair)
            framecpu.config(background=couleur2clair)
            framegpu.config(background=couleur2clair)
            titrecpu.config(background=couleur2clair)
            titregpu.config(background=couleur2clair)
            return

def cleanhistorique():
    with open("log.txt", "a") as fichier:
        fichier.truncate(0)

def consulterhistorique():

    def actuhistorique():

        with open("log.txt", "r+") as fichier:
            contenu.insert(END,fichier.readlines())
            contenu.see("end")
            contenu.after(100, actuhistorique)


    fenetrehistorique = Tk()
    fenetrehistorique.geometry("600x450")
    fenetrehistorique.config(background=couleur1sombre)
    fenetrehistorique.title("Historique de thempérature")
    fenetrehistorique.minsize(600, 450)


    contenu = tkinter.Text(fenetrehistorique,font=("Nimbus Mono PS",12))
    contenu.pack(expand=YES,fill=X)

    actuhistorique()
    fenetrehistorique.mainloop()

#coul d'arrière plan:
couleur1sombre = str("#1D2932")
couleur1clair = str("#668683")
#coul d'accent:
couleur2sombre = str("#2F4552")
couleur2clair = str("#A4C2C0")



root = Tk()
root.geometry("800x450")
root.config(background=couleur1sombre)
root.title("Thempérature système")
root.minsize(800, 450)
root.maxsize(800,450)


superframe = Frame(root, background=couleur2sombre, pady=20,)
superframe.pack(side=LEFT, fill=X)


framegeneralecpu = Frame(superframe, background=couleur2sombre, relief=FLAT, bd=1, width=100)
framegeneralecpu.pack(side=TOP, fill=X)

framecpu = Frame(framegeneralecpu, pady=70, bd=5, bg=couleur2sombre)
framecpu.pack(side=LEFT, fill=X)

titrecpu =  Label(framecpu, text="Thempérature CPU:", font=("Cantarell Extra Bold", 12), bg=couleur2sombre, fg="White", width=18)
titrecpu.pack(side=LEFT)

tempcpu =  Label(framecpu, text="Loading...", font=("Free Mono", 20), fg="Black", bg="White", pady=0, width=5)
tempcpu.pack(side=RIGHT)

cpuhealth = Label(framegeneralecpu, text="...", font=("Cantarell Extra Bold", 16),bg="grey", width=10)
cpuhealth.pack(side="right")

framegeneralegpu = Frame(superframe, background=couleur2sombre, relief=FLAT, bd=1, width=100)
framegeneralegpu.pack(side=TOP, fill=X)

framegpu = Frame(framegeneralegpu, pady=70, bd=5, bg=couleur2sombre)
framegpu.pack(side=LEFT, fill=X)

titregpu =  Label(framegpu, text="Thempérature GPU:", font=("Cantarell Extra Bold", 12), bg=couleur2sombre, fg="White", width=18)
titregpu.pack(side=LEFT)

tempgpu =  Label(framegpu, text="...", font=("Free Mono", 20), fg="Black", bg="White", pady=0, width=5)
tempgpu.pack(side=RIGHT)

gpuhealth = Label(framegeneralegpu, text="...", font=("Cantarell Extra Bold", 16),bg="grey", width=10)
gpuhealth.pack(side="right")


frameparametres = Frame(root, background=couleur2sombre)
frameparametres.pack(anchor=SE)


boutouvrirhistorique = Button(frameparametres,text="→ Consulter l'historique", command=consulterhistorique, font=("Umpush",10),relief=GROOVE,bd=0,bg="#2C323C",fg="#CAD0DA",width=20,highlightthickness=0,activebackground="#576376")
boutouvrirhistorique.pack(side=TOP)

bouttheme = Button(frameparametres,text="🌓 Basculer le theme", command= changercouleur, font=("Umpush",10),relief=GROOVE,bd=0,bg="#2C323C",fg="#CAD0DA",width=20,highlightthickness=0,activebackground="#576376")
bouttheme.pack(side=TOP)

cleanbutton = Button(frameparametres,text="Vider l'historique", command=cleanhistorique, font=("Umpush",10),relief=GROOVE,bd=0,bg="#2C323C",fg="#CAD0DA",width=20,highlightthickness=0,activebackground="#DEB419")
cleanbutton.pack(side=TOP)

quitter = Button(frameparametres, text=" Quitter", command= fermerfenetre, font=("Umpush", 10), relief=SUNKEN, bd=0, bg="#2C323C", width=20, highlightthickness=0, activebackground="#CC0000")
quitter.pack(side=BOTTOM)

ajournercpu()
root.mainloop()
