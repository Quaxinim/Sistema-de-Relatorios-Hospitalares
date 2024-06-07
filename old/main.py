import customtkinter
import tkinter as tk
from tkinter import ttk
import sqlite3
import webbrowser
import tratamento_dados

# Ctk
root = customtkinter.CTk()
# Sqlite3
connection = sqlite3.connect("../dados_usuarios.db")
cursor = connection.cursor()
# Webbroser
url = "http://127.0.0.1:8050/"


class Databank():
    # Fazendo a conexão com o banco de dados
    connection = sqlite3.connect("../dados_usuarios.db")
    cursor = connection.cursor()

    # Cria as linhas e colunas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados_usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
    )
    """)


class Application():
    def __init__(self):
        self.root = root
        self.tema()
        self.tela()
        self.tela_login()
        root.mainloop()

    def tema(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def tela(self):
        # Criação da janela
        root.geometry("500x350")
        root.wm_title("Relatorios e Dashboard Hospitalar")

    def tela_login(self):
        # Frame
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Coloca o nome no cabeçalho da janela
        label = customtkinter.CTkLabel(
            master=frame, text="Relatorios Hospitalares", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        # Colocando a caixa para escrever o usuario
        username_entry = customtkinter.CTkEntry(
            master=frame, placeholder_text="Username")
        username_entry.pack(pady=12, padx=10)

        # Colocando a caixa para escrever a senha
        password_entry = customtkinter.CTkEntry(
            master=frame, placeholder_text="Password", show="*")
        password_entry.pack(pady=12, padx=10)

        # Caixa selecionavel de lembrar senha
        checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
        checkbox.pack(pady=12, padx=10)

        def login():
            # Pega os dados digitados no campo de login
            user = username_entry.get()
            password = password_entry.get()

            # Consulta SQL para selecionar o usuário com o nome de usuário informado
            cursor.execute(
                "SELECT * FROM dados_usuarios WHERE username = ?", (user,))
            usuario = cursor.fetchone()
            print(usuario)

            # Verificação de credenciais
            if usuario is not None and password == usuario[2]:

                # Login bem-sucedido
                print("Login bem-sucedido!")
                tratamento_dados.iniciar_servidor()
                webbrowser.open(url)
                # Chamar a próxima tela ou realizar outra ação
            else:
                print("Login Falhou")

        # Botao de login
        button = customtkinter.CTkButton(
            master=frame, text="Login", command=login)
        button.pack(pady=12, padx=10)

        def tela_registro():
            # Limpa e redimendimensiona a janela
            frame.pack_forget()
            root.geometry("600x400")
            root.wm_title("Registro de usuario")

            # Criando o frame da tela de registro
            reg_frame = customtkinter.CTkFrame(master=root)
            reg_frame.pack(pady=20, padx=60, fill="both", expand=True)

            # Coloca o nome no cabeçalho da janela
            label = customtkinter.CTkLabel(
                master=reg_frame, text="Cadastre-se", font=("Roboto", 24))
            label.pack(pady=12, padx=10)

            # Função de voltar
            def back():
                reg_frame.pack_forget()
                frame.pack(pady=20, padx=60, fill="both", expand=True)

            # Botão para voltar
            voltar_button = customtkinter.CTkButton(
                master=reg_frame, text="Voltar", width=60, font=("Roboto", 10), command=back)
            voltar_button.place(x=28, y=12)

            # Primeira letra do nome
            username = customtkinter.CTkEntry(
                master=reg_frame, placeholder_text="Nome", font=("Roboto", 14))
            username.pack(pady=16, padx=30)

            # Pega o sobrenome do usuario
            surname = customtkinter.CTkEntry(
                master=reg_frame, placeholder_text="Sobrenome", font=("Roboto", 14))
            surname.pack(pady=16, padx=30)

            # Pega e confirma a senha do usuario
            pass_entry = customtkinter.CTkEntry(
                master=reg_frame, placeholder_text="Senha", show="*", font=("Roboto", 14))
            pass_entry.pack(pady=16, padx=30)

            pass_verify = customtkinter.CTkEntry(
                master=reg_frame, placeholder_text="Confirme sua senha", show="*", font=("Roboto", 14))
            pass_verify.pack(pady=16, padx=30)

            # Função que salva as informacoes escritas pelo usuario
            def save_user():
                # Pega os dados enviados pelo usuario
                usuario_crud = username.get()
                sobrenome = surname.get()
                senha = pass_entry.get()
                confirm_senha = pass_verify.get()

                # Tratamento de dados do usuario para o banco de dados
                first_letter = usuario_crud[0]
                usuario_tratado = first_letter.upper() + sobrenome.upper()

                # Tratamento de dados da senha para o banco de dados
                if senha == confirm_senha and len(senha) >= 8:
                    msg = ttk.messagebox.showinfo(
                        title="Sucesso", message="Usuario salvo com sucesso")

                    # Enviando a query para o banco de dados SQL
                    cursor.execute(
                        "INSERT INTO dados_usuarios (username, password) VALUES(? , ?)", (usuario_tratado, senha))
                    connection.commit()

                elif len(senha) < 8:
                    msg_error = ttk.messagebox.showerror(
                        title="Quantidade de caracteres", message="A quantidade de caracteres deve ser maior que 12")
                else:
                    msg_error = ttk.messagebox.showerror(
                        title="Confirmação de senha", message="As senhas não estão iguais")

            # Botão para confirmar o registro
            save_button = customtkinter.CTkButton(
                master=reg_frame, text="Salvar", command=save_user)
            save_button.pack(pady=12, padx=10)

        # Caixa de registro de usuario
        register = customtkinter.CTkButton(
            master=frame, text="Registre-se", command=tela_registro)
        register.pack(pady=12, padx=10)


Databank()
Application()
