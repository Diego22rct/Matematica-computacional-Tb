import tkinter as tk
import tkinter.filedialog
import customtkinter
import time
from app import *

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1080x720")
app.title("Equalizacion y expansion de histograma")


def progressBar():
    per = 0
    progressBar = customtkinter.CTkProgressBar(app, 400, 30, 50, 2)
    progressBar.set(per)
    progressBar.place(relx=0.3, rely=0.6)
    textDone.configure(text="Proceso en curso", text_color="red")
    textDone.pack()
    while per < 1:
        per = per + 0.1
        progressBar.set(per)
        progressBar.update()
        time.sleep(0.1)

    progressBar.place_forget()
    progressBar.destroy()
    textDone.configure(text="Proceso terminado", text_color="green")
    # esperar 1 segundo
    app.after(2000, textDone.configure(text=""))


def button_function():
    # desabled butons
    button.configure(state="disabled")
    button1.configure(state="disabled")
    selectionImage.configure(state="disabled")
    doHistogram.configure(state="disabled")
    # process part
    progressBar()
    # set buttons to normal
    button.configure(state="normal")
    button1.configure(state="normal")
    selectionImage.configure(state="normal")
    doHistogram.configure(state="normal")


def abrirArchivo():
    global imagen
    imageSelected = tk.filedialog.askopenfilename(
        initialdir="/",
        title="Seleccione archivo",
        filetypes=(("png files", "*.png"), ("all files", "*.*")),
    )
    print(imageSelected)
    if imageSelected:
        imagen = tk.PhotoImage(file=imageSelected)
        imageStart.configure(image=imagen)


tituloCentral = customtkinter.CTkLabel(
    app, text="Equalizacion y expansion de histograma", font=("Arial", 20)
)
tituloCentral.place(relx=0.5, rely=0.06, anchor="center")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=app, text="Eqaualización", command=button_function
)
button.place(relx=0.1, rely=0.1)

button1 = customtkinter.CTkButton(app, text="Expanción", command=button_function)
button1.place(relx=0.1, rely=0.15)

# image
image = tkinter.PhotoImage("image3.jpg", master=app)
imageStart = customtkinter.CTkLabel(app, 300, 200, 3, "black", image=image)
imageStart.place(relx=0.35, rely=0.1)


selectionImage = customtkinter.CTkButton(
    app, 80, 30, 5, text="Seleccionar imagen", command=abrirArchivo
)
selectionImage.place(relx=0.7, rely=0.1)

doHistogram = customtkinter.CTkButton(
    app, 80, 30, 5, text="Hacer el histograma", command=button_function
)
doHistogram.place(relx=0.7, rely=0.15)

textDone = customtkinter.CTkLabel(app, text="", text_color="red")

app.mainloop()
