#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import right, width
import DataBaser

#Criar nossa janela
janela = Tk()
janela.title("Controle de acesso MD")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.iconbitmap(default="Icons/icone.ico")
## Janela transparente
janela.attributes("-alpha", 0.9)
## Janela transparente

#======= Imagem ======
logo = PhotoImage(file="Icons/logo.png")

#======== widgets ===============
LeftFrame = Frame(janela, width=200, height=300, bg="white", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#User
UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg="midnightblue", fg="white")
UserLabel.place(x=5, y=96)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

#Password
PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="WHITE")
PassLabel.place(x=5, y=145)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)


    ###PUXA OS DADOS DO BANCO, E CONFERE###
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso confirmado. Seja Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Senha ou Usuário incorreto.")

#botoes
LoginButton = ttk.Button(RightFrame, text="Entrar", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    ##  REMOVE WIDGETS DE LOGIN
    LoginButton.place(x=99999)
    RegisterButton.place(x=99999)
    ##  INSERE WIDGETS DE CADASTRO
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=150, y=18)

    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=150, y=64)

    ##PEGA OS DADOS E SALVA NO BANCO DE DADOS##
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Erro de Registro", message="Preencha todo os campos!")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """,(Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso!")

    Register = ttk.Button(RightFrame, text="Registrar", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        #removendo widgets de cadastro
        NomeLabel.place(x=999999)
        NomeEntry.place(x=999999)
        EmailLabel.place(x=99999)
        EmailEntry.place(x=99999)
        Register.place(x=99999)
        Back.place(x=9999999)

        ## TRAZENDO OS BOTOES ANTIGOS
        LoginButton.place(x=100, y=225)
        RegisterButton.place(x=125, y= 260)


    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Cadastro", width=20, command=Register)
RegisterButton.place(x=125, y= 260) 

janela.mainloop()
