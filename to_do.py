from tkinter import *
from tkinter import messagebox

#method to add the task
def add_task():
    string = entry_field.get()
    if(len(string) == 0):
        messagebox.showinfo("Error", "Field is empty, please enter any task.")
    else:
        tasks.append(string)
        list_update()
        entry_field.delete(0, 'end')

#method to update the list
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

#method to delete the task from the list
def delete_task():
    try:
        value = task_listbox.get(task_listbox.curselection())
        if value in tasks:
            tasks.remove(value)
            list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected')

#method to clear the list
def clear_list():
    task_listbox.delete(0, 'end')

#method to close the application
def close():
    print(tasks)
    window.destroy()

window = Tk()
window.title("TO-DO LIST USING PYTHON")
window.geometry("460x480")
window.configure(bg = "plum")

#defining an empty list
tasks = []

#defining required labels and place label in the application using place() method
lbl1 = Label(window, text="TO-DO LIST", font=("TIMES NEW ROMAN", "20", "bold"), bg="purple", fg="white")
lbl1.place(x=0, y=0, width=460, height=50)

lbl2 = Label(window, text="Enter the task", font=("TIMES NEW ROMAN", "11", "bold"), fg="black")
lbl2.place(x=30, y=80)

lbl3 = Label(window, text="All Tasks", font=("TIMES NEW ROMAN", "11", "bold"), fg="black")
lbl3.place(x=30, y=200)

entry_field = Entry(window, font=("Arial", "12", "bold"), width=30, bg="#FFF8DC", fg="black")
entry_field.place(x=140, y=80)

#Buttons
add_btn = Button(window, text="Add Task", font=("Arial", "10", "bold"), command=add_task, bg="white", fg="green")
add_btn.place(x=140, y=120)

delete_btn = Button(window, text="Delete Task", font=("Arial", "10", "bold"), command=delete_task, bg="white", fg="red")
delete_btn.place(x=240, y=120)

exit_btn = Button(window, text="Exit", font=("Arial", "10", "bold"), command=close, bg="white", fg="red")
exit_btn.place(x=200, y=420)

#list of tasks added
task_listbox = Listbox(window, width=45, height=12, selectmode='SINGLE', bg="#FFFFFF", fg="#000000")
task_listbox.place(x=140, y=200)

window.mainloop()

