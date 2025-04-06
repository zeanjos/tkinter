import customtkinter as ctk
import DataBase
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

    label_email = ctk.CTkLabel(janela, text = 'E-mail', justify = 'center')
    label_email.place(relx = 0.5, rely = 0.5, anchor = 'center')


    input_email = ctk.CTkEntry(janela, placeholder_text='Digite seu E-mail', justify = 'center')
    input_email.place(relx = 0.5, rely = 0.6, anchor = 'center')
    pegar_email = input_email.get()

    label_telefone = ctk.CTkLabel(janela, text = 'Telefone de contato', justify = 'center')
    label_telefone.place(relx = 0.5, rely = 0.7, anchor = 'center')

    input_telefone = ctk.CTkEntry(janela, placeholder_text='Digite seu telefone', justify = 'center')
    input_telefone.place(relx = 0.5, rely = 0.8, anchor = 'center')
    pegar_telefone = input_telefone.get()

ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.title('Sistema de login')
janela.geometry('600x600')


label_usuario = ctk.CTkLabel(janela, text='Usuario:', justify='center')
label_usuario.place(relx = 0.5, rely = 0.1, anchor = 'center')


input_usuario = ctk.CTkEntry(janela, placeholder_text='Digite seu usuario')
input_usuario.place(relx = 0.5, rely = 0.2, anchor = 'center')
pegar_usuario = input_usuario.get()

label_usuario1 = ctk.CTkLabel(janela, text='Senha:')
label_usuario1.place(relx = 0.5, rely = 0.3, anchor = 'center')

input_senha = ctk.CTkEntry(janela, placeholder_text='Digite sua senha', justify = 'center', show='*')
input_senha.place(relx = 0.5, rely = 0.4, anchor = 'center')
pegar_senha = input_senha.get()


checkbox = ctk.CTkCheckBox(janela, text = 'Lembrar login')
checkbox.place(relx = 0.5, rely = 0.5, anchor = 'center')



botao = ctk.CTkButton(janela, text='Entrar', command=botao_callback)
botao.place(relx = 0.5, rely = 0.6, anchor = 'center')



cadastro = ctk.CTkButton(janela, text='Criar cadastro', command= registro)
cadastro.place(relx = 0.5, rely = 0.7, anchor = 'center')

login_correto = ctk.CTkLabel(janela, text='')
login_correto.place(relx = 0.5, rely = 0.8, anchor = 'center')

janela.mainloop()

