import requests  # noqa: F401
from tkinter import * # noqa: F403

num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
m = num * num1
print(f'Este é o resultado da multiplicação: {m}')

janela = Tk()
janela.title('Multiplicação')
janela.attributes('-fullscreen', True)


janela.mainloop()