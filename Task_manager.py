from datetime import datetime
import tkinter as tk
from tkinter import messagebox
#Développement informatique
root = tk.Tk()
root.title("task manager pro -cv project")
import os
import sys
def load_tasks():
     if os.path.exists("tasks.txt"):
          with open("tasks.txt","r", encoding="utf-8") as file:
               for line in file:
                 listbox.insert(tk.END,line.strip())
def save_tasks():
     tasks = listbox.get(0 ,tk.END)
     with open("tasks.txt","w",encoding="utf-8") as file:
          for task in tasks:
               file.write(task +"\n")
root.geometry("400x600")
#Ajouter un titre
label = tk.Label (root,text="ma liste de taches",font=("Arial",14,"bold"))
label.pack(pady=10)
#champ dee saisie des taches
entry = tk.Entry(root,width=35)
entry.pack(pady=5)
#fonction d'ajout d'une tache
def add_task():
    task = entry.get()
    if task !="":
        now = datetime.now().strftime("%H:%M")
        task_with_time = f"{task} ({now})"
        listbox.insert(tk.END,task_with_time)
        if "urgent"in task.lower():
            listbox.itemconfig(tk.END,fg="red")
        #Effacer le champ de saisie 
        entry.delete(0,tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Attention","veullez écrire une tache!")
        # fonction de suppression d'une tache sélectionnée 
def save_tasks():
    tasks = listbox.get(0,tk.END) 
    with open("tasks.txt","w")as f:
     for task in tasks:
          f.write(task + "\n")
def complete_task():
    try:
         index = listbox.curselection()[0]
         task_text = listbox.get(index)
         new_text = f"\u2713" + task_text
         listbox.delete(index)
         listbox.insert(index,new_text)
         listbox.intemconfig(index,fg="gray")
    except:
         messagebox.showwarning("Attention","Veuillez sélectionner une tache!")
         save_tasks()
def load_tasks():
    try:
         with open("tasks.txt" ,"r") as f:
              for line in f:
                   listbox.insert(tk.END,line.strip())
    except FileNotFoundError:
                   pass
#(GUT)
def delete_task():
     try:
                selected_task = listbox.curselection() #Identifier l'élément sélectionné
                listbox.delete(selected_task)#Appeler la fonction de sauvegarde immédiatement après la suppression
                save_tasks()
     except:
           messagebox.showwarning("Attention""sélectionnez une tache")
# Boutons de controle
btn_add = tk. Button(root,text="Ajouter la tache",command=add_task, bg="#4CAF50",fg="white",width=20,activebackground="#45a049")
btn_add.pack(pady=5)
#(listbox)
listbox = tk.Listbox=tk.Listbox(root,width=45, height=4,font=("Arial",12,"bold"))
listbox.pack(pady=10)
btn_delete = tk.Button(root,text="supprimer la tache",command=delete_task,bg="#f44336",fg="white",width=20,activebackground="#da190b")
btn_done = tk.Button(root,text="Tache terminée",command=complete_task,bg="#2196F3",fg="white")
btn_delete.pack(pady=5)
btn_done.pack(pady=5)
#lancer le programme 
load_tasks()
root.bind('<Return>',lambda event:add_task())
root.mainloop()