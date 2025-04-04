import customtkinter as ctk
def botao_callback():
    usuario = input_usuario.get()
    senha = input_senha.get()

    if usuario == 'Janjos' and senha == 'jumento123':
        login_correto.configure(text='Login realizado corretamente!', text_color='green')
    else:
        login_correto.configure(text='Login incorreto!', text_color='red')
        

ctk.set_appearance_mode('amoled')
janela = ctk.CTk()
janela.title('Sistema de login')
janela.geometry('300x300')

label_usuario = ctk.CTkLabel(janela, text='Usuario:')
label_usuario.pack(pady=10, side = 'top')

input_usuario = ctk.CTkEntry(janela, placeholder_text='Digite seu usuario', justify = 'center')
input_usuario.pack(pady = 10,)

label_usuario1 = ctk.CTkLabel(janela, text='Senha:')
label_usuario1.pack(pady = 10, side = 'top')

input_senha = ctk.CTkEntry(janela, placeholder_text='Digite sua senha', justify = 'center')
input_senha.pack(pady = 10)

botao = ctk.CTkButton(janela, text='Entrar', command=botao_callback)
botao.pack(pady = 20, side = 'top')

login_correto = ctk.CTkLabel(janela, text='')
login_correto.pack(side = 'top')

janela.mainloop()

