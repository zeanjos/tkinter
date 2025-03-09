import requests  # noqa: F401
from tkinter import * # noqa: F403
def janelasd():
    jan = 1

janela = Tk()  # noqa: F405
janela.title('Multiplicação')


t_orienta = Label(janela, text="Clique no botão para somar")
t_orienta.grid(column=0, row=0)
t_orienta1 = Label(janela, text="Clique aqui agora")
t_orienta1.grid(column=3, row=0)

botao = Button(janela, text="Clique aqui", command= janelasd)
botao.grid(column=2, row=2)
janela.mainloop()