#Referencias
#https://www.youtube.com/watch?v=7PGFin30c4o&t=42s
#https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
#https://www.youtube.com/watch?v=-GLaHb-s4kA
#https://stackoverflow.com/questions/11073553/open-function-python-default-directory
#https://pythonspot.com/tk-file-dialogs/
#https://www.geeksforgeeks.org/python-string-split/
#https://www.youtube.com/watch?v=772XCgm-Mr4&list=PLamqrZ7b2mV5IM9_xGkNT2CPGP9wWKN3c&index=4&t=0s


import tkinter as tk
from tkinter import filedialog
import os


class MenuBar:

    def __init__(self, parent):
        font_specs = ("Consolas", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File", accelerator="Ctrl+N", command=parent.new_file)
        file_dropdown.add_command(label="Open File", accelerator="Ctrl+O", command=parent.open_file)
        file_dropdown.add_command(label="Save", accelerator="Ctrl+S", command=parent.save)
        file_dropdown.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit", command=parent.master.destroy)

        menubar.add_cascade(label="File", menu=file_dropdown)



class StatusBar:

    def __init__(self, parent):
        
        font_specs = ("Consolas", 10)

        self.status = tk.StringVar()
        self.status.set("DodeFast IDE - No errors.")

        label = tk.Label(parent.textarea, textvariable=self.status, fg="black", bg="lightgrey", anchor='sw', font=font_specs)

        label.pack(side=tk.BOTTOM, fill=tk.BOTH)
    
    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Your file has been saved.")
        else:
            self.status.set("DodeFast IDE - No errors.")



class IDE:

    def __init__(self, master):
        master.title("Untitled - DodeFast IDE")
        master.geometry("1200x700")

        font_specs = ("Consolas", 18)

        self.master = master
        self.filename = None

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        
        self.textarea.configure(yscrollcommand=self.scroll.set)
        
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = MenuBar(self)
        self.statusbar = StatusBar(self)

        self.bind_shortcuts()

    def set_window_title(self, name=None):
        if name:
            self.master.title(name.split('/')[-1].split('.')[0] + " - DodeFast IDE")
        else:
            self.master.title("Untitled - DodeFast IDE")

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            initialdir = os.getcwd(),
            defaultextension=".df",
            filetypes=[("DodeFast Scripts", ".df"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("All Files", "*.*")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)
    
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
            initialfile="Untitled.df",
            initialdir = os.getcwd(),
            defaultextension=".df",
            filetypes=[("DodeFast Scripts", ".df"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("All Files", "*.*")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as e:
            print(e)
    
    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Key>', self.statusbar.update_status)



if __name__ == "__main__":
    master = tk.Tk()
    ide = IDE(master)
    master.mainloop()