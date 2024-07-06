import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    email = email_entry.get()
    student = student_var.get()
    professor = professor_var.get()
    education_level = education_var.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    messagebox.showinfo("Cadastro", f"Nome: {name}\nEmail: {email}\nEstudante: {student}\nProfessor: {professor}\nEscolaridade: {education_level}\nSenha: {password}")

def abrir_login(event):
    root.withdraw()  # Esconde a janela de matrícula
    exec(open("entrar.py", encoding="utf-8").read())  # Abre a janela de login

def update_options(*args):
    if professor_var.get():
        student_var.set(False)
        education_label.config(text="Selecione sua área de atuação:")
        education_var.set('')  # Limpa a seleção atual
        education_menu['menu'].delete(0, 'end')
        new_options = ["Ciências Humanas", "Ciências da Natureza", "Linguagens", "Matemática"]
        for option in new_options:
            education_menu['menu'].add_command(label=option, command=tk._setit(education_var, option))
    elif student_var.get():
        professor_var.set(False)
        education_label.config(text="Selecione sua escolaridade:")
        education_var.set('')  # Limpa a seleção atual
        education_menu['menu'].delete(0, 'end')
        new_options = ["Ensino Fundamental - 1o ano", "Ensino Fundamental - 2o ano", "Ensino Fundamental - 3o ano", "Ensino Fundamental - 4o ano",
                        "Ensino Fundamental - 5o ano", "Ensino Fundamental - 6o ano", "Ensino Fundamental - 7o ano", "Ensino Fundamental - 8o ano",
                        "Ensino Fundamental - 9o ano", "Ensino Médio - 1o ano", "Ensino Médio - 2o ano", "Ensino Médio - 3o ano", 
                        "Ensino Superior", "Pós-Graduação", "Não tenho escolaridade"]
        for option in new_options:
            education_menu['menu'].add_command(label=option, command=tk._setit(education_var, option))

# Criar a janela principal
root = tk.Tk()
root.title("Matrícula")
root.geometry("400x700")
root.configure(bg='white')

# Definir estilos comuns
font_style = ("Arial", 12)
button_style = ("Arial", 12, "bold")

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
register_box = tk.Frame(root, bg='white', highlightbackground="#FF6E14", highlightcolor="orange", highlightthickness=2, padx=20, pady=20)
register_box.pack(pady=20)

# Título "Matrícula"
titulo_label = tk.Label(register_box, text="Matrícula", font=button_style, fg="#FF6E14", bg="white")
titulo_label.pack()

# Formulário de cadastro
register_frame = tk.Frame(register_box, bg='white')
register_frame.pack(pady=10)

# Caixa de nome completo
tk.Label(register_frame, text="Nome completo:", font=font_style, bg="white").grid(row=0, column=0, pady=10, padx=10, sticky='w')
name_entry = tk.Entry(register_frame, width=30, bd=2, font=font_style)
name_entry.grid(row=0, column=1, pady=10, sticky='w')

# Caixa de email
tk.Label(register_frame, text="Email:", font=font_style, bg="white").grid(row=1, column=0, pady=10, padx=10, sticky='w')
email_entry = tk.Entry(register_frame, width=30, bd=2, font=font_style)
email_entry.grid(row=1, column=1, pady=10, sticky='w')

# Checkboxes
student_var = tk.BooleanVar()
professor_var = tk.BooleanVar()
student_var.trace('w', update_options)  # Monitorar mudanças
professor_var.trace('w', update_options)  # Monitorar mudanças

tk.Checkbutton(register_frame, text="Sou estudante", variable=student_var, bg="white").grid(row=2, column=0, pady=10, padx=10, sticky='w')
tk.Checkbutton(register_frame, text="Sou professor", variable=professor_var, bg="white").grid(row=2, column=1, pady=10, padx=10, sticky='w')

# Menu de seleção de escolaridade/área de atuação
education_label = tk.Label(register_frame, text="Selecione:", font=font_style, bg="white")
education_label.grid(row=3, column=0, pady=10, padx=10, sticky='w')

education_var = tk.StringVar()
education_menu = tk.OptionMenu(register_frame, education_var, "Selecione se você é aluno ou professor")
education_menu.grid(row=3, column=1, pady=10, sticky='w')

# Caixa de senha
tk.Label(register_frame, text="Senha:", font=font_style, bg="white").grid(row=4, column=0, pady=10, padx=10, sticky='w')
password_entry = tk.Entry(register_frame, width=30, bd=2, show="*", font=font_style)
password_entry.grid(row=4, column=1, pady=10, sticky='w')

# Caixa de confirmação de senha
tk.Label(register_frame, text="Confirmar senha:", font=font_style, bg="white").grid(row=5, column=0, pady=10, padx=10, sticky='w')
confirm_password_entry = tk.Entry(register_frame, width=30, bd=2, show="*", font=font_style)
confirm_password_entry.grid(row=5, column=1, pady=10, sticky='w')

# Botão de matricular
register_button = tk.Button(register_frame, text="Matricular", font=button_style, bg="#FF6E14", fg="white", width=20, command=register)
register_button.grid(row=6, columnspan=2, pady=20)

# Link para login
login_label = tk.Label(root, text="Já tenho matrícula", fg="#FF6E14", bg="white", cursor="hand2", font=font_style)
login_label.pack(pady=10)
login_label.bind("<Button-1>", abrir_login)  # Associa o evento de clique à função abrir_login

# Iniciar o loop da aplicação
root.mainloop()
