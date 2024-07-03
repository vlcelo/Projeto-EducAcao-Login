import tkinter as tk
from tkinter import messagebox

def login():
    email = email_entry.get()
    password = password_entry.get()
    messagebox.showinfo("Login", f"Email: {email}\nSenha: {password}")

def abrir_matricula(event):
    root.withdraw()  # Esconde a janela de login
    exec(open("matricula.py").read())  # Abre a janela de matrícula

# Criar a janela principal
root = tk.Tk()
root.title("Login")
root.geometry("400x500")
root.configure(bg='white')

# Caixa de texto para o logotipo
logo_text = tk.Text(root, height=1, width=20, bg='white', bd=0, font=("Arial", 24, "bold"))
logo_text.tag_configure("black", foreground="black")
logo_text.tag_configure("#FF6E14", foreground="#FF6E14")
logo_text.insert(tk.END, "Educa", "black")
logo_text.insert(tk.END, "Ação", "#FF6E14")
logo_text.tag_configure("center", justify='center')
logo_text.tag_add("center", "1.0", "end")
logo_text.pack(pady=20)
logo_text.configure(state="disabled")  # Desabilita edição

# Caixa ao redor dos campos principais
login_box = tk.Frame(root, bg='white', highlightbackground="#FF6E14", highlightcolor="#FF6E14", highlightthickness=2, padx=20, pady=20)
login_box.pack(pady=20)

# Título "Entrar"
titulo_label = tk.Label(login_box, text="Entrar", font=("Arial", 16, "bold"), fg="#FF6E14", bg="white")
titulo_label.pack()

# Formulário de login
login_frame = tk.Frame(login_box, bg='white')
login_frame.pack(pady=10)

# Caixa de email
tk.Label(login_frame, text="Email:", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=10, padx=10, sticky='e')
email_entry = tk.Entry(login_frame, width=30, bd=2)
email_entry.grid(row=0, column=1, pady=10)

# Caixa de senha
tk.Label(login_frame, text="Senha:", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=10, padx=10, sticky='e')
password_entry = tk.Entry(login_frame, width=30, bd=2, show="*")
password_entry.grid(row=1, column=1, pady=10)

# Botão de entrar
login_button = tk.Button(login_frame, text="Entrar", font=("Arial", 12), bg="#FF6E14", fg="white", width=20, command=login)
login_button.grid(row=2, columnspan=2, pady=20)

# Link para cadastro
register_label = tk.Label(root, text="Não tenho matrícula", fg="#FF6E14", bg="white", cursor="hand2", font=("Arial", 12, "underline"))
register_label.pack(pady=10)
register_label.bind("<Button-1>", abrir_matricula)  # Associa o evento de clique à função abrir_matricula

# Iniciar o loop da aplicação
root.mainloop()
