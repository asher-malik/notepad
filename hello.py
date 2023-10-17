import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = tkinter.Tk()
root.title("notepad")
root.resizable(0, 0)
root.geometry("600x600")
root.iconbitmap("pad.ico")
root.config(bg="#6B7F82")

def close_note():
    yesno = tkinter.messagebox.askyesno(title="close note", message="Are you sure you want to close your note?")
    if yesno:
        root.destroy()

def change_font(*args):
    text_frame.config(font=(font_var.get(), size_var.get(), type_var.get()))

def new_note():
    question = tkinter.messagebox.askyesno(title="new note", message="Are you sure you want to start a new note?")
    if question:
        text_frame.delete("1.0", "end")

def save():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                text_content = text_frame.get("1.0", tkinter.END)
                file.write(text_content)
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def open_note():
    try:
        open_note = filedialog.askopenfilename()
        if open_note:
            with open(open_note, "r") as file:
                text_content = file.read()
                text_frame.delete("1.0", tkinter.END)
                text_frame.insert("1.0", text_content)
    except:
        pass

font_var = tkinter.StringVar()
font_var.set("Terminal")
size_var = tkinter.IntVar()
size_var.set(12)
type_var = tkinter.StringVar()
type_var.set("normal")

font_list = ["Terminal", "Modern", "Script", "Courier", "Arial", "Calibri", "Cambria", "Georgia", "MS Gothic", "SimSun"]
size_list = [0, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
type = ["normal", "bold", "italic"]


scrollbar = tkinter.Scrollbar(root)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y, padx=(0, 10), pady=(77, 15))

button_frame = tkinter.Frame(root, width=200, height=40, bg="#D5DFE5")
text_frame = tkinter.Text(root, width=570, height=520, bg="#FFF5B2", font=(font_var.get(), size_var.get()), yscrollcommand=scrollbar.set)


button_frame.pack(pady=(10, 0))
scrollbar.config(command=text_frame.yview)
text_frame.pack(pady=(20, 15), padx=(10, 0), side=tkinter.LEFT, fill=tkinter.BOTH)

new_note_image = ImageTk.PhotoImage(Image.open("new.png"))
new_note_button = tkinter.Button(button_frame, image=new_note_image, command=new_note)
new_note_button.grid(row=0, column=0, pady=5, padx=5)

open_note_image = ImageTk.PhotoImage(Image.open("open.png"))
open_note_button = tkinter.Button(button_frame, image=open_note_image, borderwidth=2, command=open_note)
open_note_button.grid(row=0, column=1, pady=5, padx=5)

save_note_image = ImageTk.PhotoImage(Image.open("save.png"))
save_note_button = tkinter.Button(button_frame, image=save_note_image, borderwidth=2, command=save)
save_note_button.grid(row=0, column=2, pady=5, padx=5)

close_note_image = ImageTk.PhotoImage(Image.open("close.png"))
close_note_button = tkinter.Button(button_frame, image=close_note_image, borderwidth=2, command=close_note)
close_note_button.grid(row=0, column=3, pady=5, padx=5)

font_box = tkinter.OptionMenu(button_frame, font_var, *font_list, command=change_font)
font_box.config(width=10)
font_box.grid(row=0, column=4, pady=5, padx=5)

font_size = tkinter.OptionMenu(button_frame, size_var, *size_list, command=change_font)
font_size.config(width=5)
font_size.grid(row=0, column=5, padx=5, pady=5)

font_type = tkinter.OptionMenu(button_frame, type_var, *type, command=change_font)
font_type.config(width=5)
font_type.grid(row=0, column=6, padx=5, pady=5)

root.mainloop()