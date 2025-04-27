import customtkinter as ctk

from database import insert_date

def mostrar_login():
    #mostra na tela de login 
    input_email.place(relx=0.5, rely=0.2, anchor='center')
    input_senha.place(relx= 0.5, rely=0.3, anchor='center')
    checkbox.place(relx=0.5, rely=0.4, anchor='center')
    entrar.place(relx=0.5, rely=0.5, anchor='center')
    cadastro.place(relx=0.5, rely=0.6, anchor='center')
    login_correto.place(relx=0.5, rely=0.7, anchor='center')

#oculta os widget na tela de cadastro
    input_telefone.place_forget()
    criar_cadastro.place_forget()
    input_email_cadastro.place_forget()
    input_senha_cadastro.place_forget()
    voltar.place_forget()
    
def mostrar_valores():
    #oculta os widget na tela de login
    input_senha.place_forget()
    checkbox.place_forget()
    entrar.place_forget()
    cadastro.place_forget()
    login_correto.place_forget()

    #mostra na tela de cadastro
    input_email_cadastro.place(relx=0.5, rely=0.2, anchor='center')
    input_telefone.place(relx=0.5, rely=0.3, anchor='center')
    input_senha_cadastro.place(relx=0.5, rely=0.4, anchor='center')
    criar_cadastro.place(relx=0.5, rely=0.5, anchor='center')
    voltar.place(relx=0.5, rely=0.6, anchor='center')
def obter_valores():
    senha = input_senha.get()
    email = input_email.get()
#aqui pega todos os valores digitados pra enviar ao banco de dados
    if not senha or not email:
        messagebox = ctk.CTkLabel(janela, placeholder_text='Insira todos os campos.', justify = 'center')
        messagebox.place(relx = 0.5, rely = 0.7, anchor='center')
    else:
        insert_date(senha, email)

def valores_cadastro():
    email_cadastro = input_email_cadastro.get()
    senha_cadastro = input_senha_cadastro.get()
    telefone = input_telefone.get()
    if not email_cadastro or not senha_cadastro or not telefone:
        messagebox = ctk.CTkLabel(janela, text='insira todos os campos', justify='center')
        messagebox.place(relx=0.5, rely=0.7, anchor='center')
    else:
        insert_date(email_cadastro, senha_cadastro, telefone)
    
    #aqui verifica se todos os campos foram preenchidos pra não dar erro depois no banco de dados.
    

#aqui cria a janela né
ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.title('Sistema de login')
janela.geometry('600x600')

#tela de login 
input_email = ctk.CTkEntry(janela, placeholder_text='Digite seu E-mail', justify = 'center')
input_senha = ctk.CTkEntry(janela, placeholder_text='Digite sua senha', justify = 'center', show='*')
checkbox = ctk.CTkCheckBox(janela, text = 'Lembrar login')
entrar = ctk.CTkButton(janela, text='Entrar', command=obter_valores)
cadastro = ctk.CTkButton(janela, text='Primeiro acesso', command= mostrar_valores)
login_correto = ctk.CTkLabel(janela, text='')

#tela de cadastro
input_email_cadastro = ctk.CTkEntry(janela, placeholder_text='Digite seu E-mail', justify = 'center')
input_senha_cadastro = ctk.CTkEntry(janela, placeholder_text='Digite sua nova senha', justify='center')
input_telefone = ctk.CTkEntry(janela, placeholder_text='Digite seu telefone', justify = 'center')
criar_cadastro = ctk.CTkButton(janela, text='Criar cadastro', command = valores_cadastro)
voltar = ctk.CTkButton(janela, text='Voltar', command=mostrar_login)

mostrar_login()

janela.mainloop()