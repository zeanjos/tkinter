import customtkinter as ctk

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
    
    def obter_valores():
        usuario = input_usuario.get()
        senha = input_senha.get()
        email = input_email.get()
        telefone = input_telefone()
        if not usuario or not senha or not email or not telefone:
            messagebox = ctk.CTkEntry(janela, placeholder_text='Insira todos os campos.', justify = 'center')
            messagebox.place(relx = 0.5, rely = 0.9, anchor = 'center')
        else:
            insert_date(usuario, senha, email, telefone)

    input_email = ctk.CTkEntry(janela, placeholder_text='Digite seu E-mail', justify = 'center')
    input_email.place(relx = 0.5, rely = 0.4, anchor = 'center')

    input_telefone = ctk.CTkEntry(janela, placeholder_text='Digite seu telefone', justify = 'center')
    input_telefone.place(relx = 0.5, rely = 0.5, anchor = 'center')
    

    criar_cadastro = ctk.CTkButton(janela, text='Criar cadastro', command = obter_valores)
    criar_cadastro.place(relx = 0.5, rely = 0.6, anchor = 'center')

ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.title('Sistema de login')
janela.geometry('600x600')


input_usuario = ctk.CTkEntry(janela, placeholder_text='Digite seu usuario', justify='center')
input_usuario.place(relx = 0.5, rely = 0.2, anchor = 'center')



input_senha = ctk.CTkEntry(janela, placeholder_text='Digite sua senha', justify = 'center', show='*')
input_senha.place(relx = 0.5, rely = 0.3, anchor = 'center')



checkbox = ctk.CTkCheckBox(janela, text = 'Lembrar login')
checkbox.place(relx = 0.5, rely = 0.6, anchor = 'center')


botao = ctk.CTkButton(janela, text='Entrar', command=botao_callback)
botao.place(relx = 0.5, rely = 0.4, anchor = 'center')


cadastro = ctk.CTkButton(janela, text='Primeiro acesso', command= registro)
cadastro.place(relx = 0.5, rely = 0.5, anchor = 'center')

login_correto = ctk.CTkLabel(janela, text='Login correto.')
login_correto.place(relx = 0.5, rely = 0.7, anchor = 'center')



janela.mainloop()