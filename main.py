import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskManagerApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("Список задач")

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Добавить задачу", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=70, height=15)
        self.task_listbox.pack(pady=5)

        self.edit_button = tk.Button(root, text="Редактировать задачу", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Удалить задачу", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Задача выполнена", command=self.mark_task_completed)
        self.complete_button.pack(pady=5)

        self.update_task_listbox()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.tasks.append(Task(description))
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Предупреждение", "Введите описание задачи.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Предупреждение", "Выберите задачу для удаления.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_description = self.task_entry.get()
            if new_description:
                self.tasks[selected_task_index[0]].description = new_description
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Предупреждение", "Введите новое описание задачи.")
        else:
            messagebox.showwarning("Предупреждение", "Выберите задачу для редактирования.")

    def mark_task_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]].completed = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Предупреждение", "Выберите задачу для пометки как выполненной.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Выполнено" if task.completed else "Не выполнено"
            self.task_listbox.insert(tk.END, f"{task.description} - {status}")
            if task.completed:
                self.task_listbox.itemconfig(tk.END, {'fg': 'green'})
            else:
                self.task_listbox.itemconfig(tk.END, {'fg': 'black'})

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
