import requests  # noqa: F401
from tkinter import * # noqa: F403


janela = Tk()  # noqa: F405
janela.title('Multiplicação')


t_orienta = Label(janela, text="Clique no botão para somar")  # noqa: F405
t_orienta.grid(column=0, row=0)
t_orienta1 = Label(janela, text="Clique aqui agra")  # noqa: F405
t_orienta1.grid(column=1, row=1)

janela.mainloop()
