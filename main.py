import tkinter as tk

ventana = tk.Tk()

ventana.title("MI PRIMER INTERFAZ GRAFICA")
ventana .geometry("600x400+500+150")
ventana.minsize(400, 200)
ventana.maxsize(800, 600)
ventana. iconbitmap("per.ico")
ventana.config(bg="lightblue")
ventana.resizable(False, True)
ventana.attributes("-alpha", 0.9)

ventana.mainloop()