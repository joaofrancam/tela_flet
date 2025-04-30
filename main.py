import flet as ft

# Simulação de banco de dados em memória
usuarios = {}

def main(page: ft.Page):
    page.title = "App com Login e Cadastro"
    page.window_width = 400
    page.window_height = 600

    def mostrar_tela_login():
        page.views.clear()
        page.views.append(view_login)
        page.update()

    def mostrar_tela_cadastro():
        page.views.clear()
        page.views.append(view_cadastro)
        page.update()

    def mostrar_tela_home(email):
        nav_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.HOME, label="Início"),
                ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Perfil"),
            ],
            on_change=lambda e: print(f"Selecionado: {e.control.selected_index}"),
        )

        page.views.clear()
        page.views.append(
            ft.View(
                "/home",
                controls=[
                    ft.AppBar(title=ft.Text("Bem-vindo, " + email)),
                    ft.Text("Você está logado com sucesso!"),
                    nav_bar
                ]
            )
        )
        page.update()


    def login(e):
        email = email_login.value
        senha = senha_login.value
        if email in usuarios and usuarios[email] == senha:
            mostrar_tela_home(email)
        else:
            msg_login.value = "Email ou senha inválidos."
            msg_login.update()

    def cadastrar(e):
        email = email_cadastro.value
        senha = senha_cadastro.value
        if email in usuarios:
            msg_cadastro.value = "Usuário já existe."
        else:
            usuarios[email] = senha
            msg_cadastro.value = "Cadastro realizado com sucesso!"
        msg_cadastro.update()

    # View Login
    email_login = ft.TextField(label="Email")
    senha_login = ft.TextField(label="Senha", password=True)
    msg_login = ft.Text(value="", color=ft.colors.RED)
    view_login = ft.View(
        "/login",
        [
            ft.Text("Login", size=30),
            email_login,
            senha_login,
            ft.ElevatedButton("Entrar", on_click=login),
            msg_login,
            ft.TextButton("Cadastrar", on_click=lambda _: mostrar_tela_cadastro())
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # View Cadastro
    email_cadastro = ft.TextField(label="Email")
    senha_cadastro = ft.TextField(label="Senha", password=True)
    msg_cadastro = ft.Text(value="", color=ft.colors.GREEN)
    view_cadastro = ft.View(
        "/cadastro",
        [
            ft.Text("Cadastro", size=30),
            email_cadastro,
            senha_cadastro,
            ft.ElevatedButton("Cadastrar", on_click=cadastrar),
            msg_cadastro,
            ft.TextButton("Voltar ao Login", on_click=lambda _: mostrar_tela_login())
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    mostrar_tela_login()

ft.app(target=main)
