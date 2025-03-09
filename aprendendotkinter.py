import time as time
from tkinter import *
janela = Tk()  # noqa: F405
janela.title('Multiplicação')

texto_ano = Label(janela, text='Ano atual: ')
texto_ano.grid(column=2, row=3)

def ano():
    atual = time.strftime('%Y')
    texto_ano.config(text=atual)




t_orienta = Label(janela, text="Clique no botão para somar")
t_orienta.grid(column=0, row=0)
t_orienta1 = Label(janela, text="Clique no botão para somar")
t_orienta1.grid(column=3, row=0)

botao = Button(janela, text="Clique aqui para ver o ano atual", command= ano)
botao.grid(column=2, row=2)




janela.mainloop()