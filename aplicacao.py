import customtkinter as ctk
import time
from database import insert_date
def botao_callback():
    
    usuario = input_usuario.get()
    senha = input_senha.get()

    if usuario == 'Janjos' and senha == 'jumento123':
        login_correto.configure(text='Login realizado corretamente!', text_color='green')
    else:
        login_correto.configure(text='Login incorreto!', text_color='red')

def registro():
    botao.place_forget()
    checkbox.place_forget()
    login_correto.place_forget()
    cadastro.place_forget()
    def botao_callback_dois():
        usuario_cadastro = input_usuario.get()
        senha_cadastro = input_senha.get()
        email_cadastro = input_email.get()
        telefone_cadastro = input_telefone.get()
        insert_date(usuario_cadastro, senha_cadastro, email_cadastro, telefone_cadastro)

    input_email = ctk.CTkEntry(janela, placeholder_text='Digite seu E-mail', justify = 'center')
    input_email.place(relx = 0.5, rely = 0.4, anchor = 'center')
    pegar_email = input_email.get()

    input_telefone = ctk.CTkEntry(janela, placeholder_text='Digite seu telefone', justify = 'center')
    input_telefone.place(relx = 0.5, rely = 0.5, anchor = 'center')
    pegar_telefone = input_telefone.get()

    criar_cadastro = ctk.CTkButton(janela, text='Criar cadastro', command=botao_callback_dois)
    criar_cadastro.place(relx = 0.5, rely = 0.6, anchor = 'center')

ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.title('Sistema de login')
janela.geometry('600x600')


input_usuario = ctk.CTkEntry(janela, placeholder_text='Digite seu usuario', justify='center')
input_usuario.place(relx = 0.5, rely = 0.2, anchor = 'center')
pegar_usuario = input_usuario.get()

input_senha = ctk.CTkEntry(janela, placeholder_text='Digite sua senha', justify = 'center', show='*')
input_senha.place(relx = 0.5, rely = 0.3, anchor = 'center')
pegar_senha = input_senha.get()


checkbox = ctk.CTkCheckBox(janela, text = 'Lembrar login')
checkbox.place(relx = 0.5, rely = 0.6, anchor = 'center')


botao = ctk.CTkButton(janela, text='Entrar', command=botao_callback)
botao.place(relx = 0.5, rely = 0.4, anchor = 'center')


cadastro = ctk.CTkButton(janela, text='Primeiro acesso', command= registro)
cadastro.place(relx = 0.5, rely = 0.5, anchor = 'center')

login_correto = ctk.CTkLabel(janela, text='')
login_correto.place(relx = 0.5, rely = 0.7, anchor = 'center')



janela.mainloop()