import requests  # noqa: F401
from tkinter import * # noqa: F403

num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
m = num * num1
print(f'Este é o resultado da multiplicação: {m}')

janela = Tk()  # noqa: F405
janela.title('Multiplicação')
janela.attributes('-fullscreen', True)

t_orienta = Label(janela, text="Clique no botão para somar")  # noqa: F405
t_orienta.grid(column=8, row=0)

janela.mainloop()


