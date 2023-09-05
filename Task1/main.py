import tkinter as tk    
from tkinter import messagebox

def add_the_task(task_list, task_entry):
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_the_task(task_list):
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected.")
        
def update_the_task(task_list, task_entry):
    try:
        index = task_list.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_list.delete(index)
            task_list.insert(index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected.")       

def clear_the_tasks(task_list):
    task_list.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry("800x800")
    root.config(bg="#ADD8E6")
    root.title("To-Do List")
    
    heading = tk.Label(root, text="TO-DO LIST", font=("Anastasia", 30, "bold"))
    heading.pack(pady=30)
    
    enter_task = tk.Entry(root, font=("Helvetica", 15), bg="white" , width=30)
    enter_task.pack(pady=20)

    list_of_tasks = tk.Listbox(root, font=("Sudo", 12), bg="white" , width=50, height=10)
    list_of_tasks.pack(pady=10)

    buttons = tk.Frame(root)
    buttons.pack(pady=10)

    add = tk.Button(buttons, text="Enter Task", bg="#FFDBAC" , command=lambda: add_the_task(list_of_tasks, enter_task))
    add.pack(side=tk.LEFT, padx=5)
    
    update = tk.Button(buttons, text="Update Task", bg="#FFDBAC" , command=lambda: update_the_task(list_of_tasks, enter_task))
    update.pack(side=tk.LEFT, padx=5)

    delete = tk.Button(buttons, text="Delete Task", bg="#FFDBAC" , command=lambda: delete_the_task(list_of_tasks))
    delete.pack(side=tk.LEFT, padx=5)


    root.mainloop()

if __name__ == '__main__':
    main()
