import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("To Do List by")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:    
       tkinter.messagebox.showwarning(title="Warning!",message="You must enter a option.")
       
def delete_task():
    try:
       tasks_index = listbox_tasks.curselection()[0]
       listbox_tasks.delete(tasks_index)
    except:
       tkinter.messagebox.showwarning(title="Warning!",message="You must enter a option.")
            
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0,tkinter.END)
        for task in tasks:
           listbox_tasks.insert(tkinter.END, task)
    except:
         tkinter.messagebox.showwarning(title="Warning!",message="cannot find tasks.dat.")


def save_task():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks,open("tasks.dat","wb"))

frame_task = tkinter.Frame(window)
frame_task.pack()
       

listbox_tasks = tkinter.Listbox(frame_task,height=3,width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_task)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(window,width=50)
entry_task.pack()

button_add_task = tkinter.Button (window, text="add option",width=58, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button (window, text=" delete option",width=58, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button (window, text="load option",width=58, command=load_tasks)
button_load_tasks.pack()

button_save_task = tkinter.Button (window, text="save option",width=58, command=save_task)
button_save_task.pack()

window.mainloop()
