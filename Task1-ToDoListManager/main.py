from tkinter import *
import time

class TodoApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("ToDo List Manager")
        self.geometry("800x600")
        self.resizable(False, False)
        self.tasks = []
        self.initialize_ui()

    def initialize_ui(self):
        self.create_app_heading()
        self.create_input_frame()
        self.create_display_frame()
        self.create_operation_frame()

    def create_app_heading(self):
        app_heading = Label(self, text="ToDo List Manager", font=('Pristina', 27, 'bold'), pady=20, bg="#e9ecf4")
        app_heading.pack(fill=X)

    def create_input_frame(self):
        self.item_input_frame = Frame(self, bg="#e9ecf4", pady=10)
        self.item_input_frame.pack(fill=X)

        self.item_entry_box = Entry(self.item_input_frame, width=50, font=('Helvetica', 16))
        self.item_entry_box.pack(side=LEFT, padx=10)

        self.create_add_button()

    def create_add_button(self):
        add_button = Button(self.item_input_frame, text="Add Task", font=('Helvetica', 12), command=self.add_item)
        add_button.pack(side=LEFT, padx=10)

    def create_display_frame(self):
        self.list_display_frame = Frame(self, bg="#ffffff")
        self.list_display_frame.pack(fill=BOTH, expand=True)

        self.canvas = Canvas(self.list_display_frame, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

    def create_operation_frame(self):
        self.operation_button_frame = Frame(self, bg="#e9ecf4")
        self.operation_button_frame.pack(fill=X)

        edit_button = Button(self.operation_button_frame, text="Edit", font=('Helvetica', 12), command=self.edit_task)
        edit_button.pack(side=LEFT, padx=10, pady=10)

        delete_button = Button(self.operation_button_frame, text="Delete", font=('Helvetica', 12), command=self.delete_crossed_item)
        delete_button.pack(side=LEFT, padx=10, pady=10)

        clear_button = Button(self.operation_button_frame, text="Clear All", font=('Helvetica', 12), command=self.clear_list)
        clear_button.pack(side=LEFT, padx=10, pady=10)

    def add_item(self):
        new_item = self.item_entry_box.get()
        if new_item:
            self.tasks.append(new_item)
            self.item_entry_box.delete(0, END)
            self.list_display()
            self.animate_task(new_item)
        else:
            msg.showwarning("Warning", "Please enter a task.")

    def list_display(self):
        self.canvas.delete("all")
        y_pos = 50
        for task in self.tasks:
            self.canvas.create_text(400, y_pos, text=task, font=('Helvetica', 16), fill="#0e0c49")
            y_pos += 30

    def animate_task(self, task):
        text_id = self.canvas.create_text(400, -20, text=task, font=('Helvetica', 16), fill="#0e0c49")
        for i in range(20):
            self.canvas.move(text_id, 0, 2)
            self.update()
            time.sleep(0.03)
        self.canvas.delete(text_id)

    def edit_task(self):
        pass

    def delete_crossed_item(self):
        pass

    def clear_list(self):
        pass

if __name__ == '__main__':
    app = TodoApp()
    app.mainloop()
