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

    def mostrar_tela_home(user):
        velocidade = ft.Ref[ft.Slider]()
        conteudo = ft.Column()

        def on_nav_change(e):
            atualizar_conteudo_visivel()

        def run_clicked(e):
            print(f"Velocidade selecionada: {velocidade.current.value}")

        def atualizar_conteudo_visivel():
            conteudo.controls.clear()
            idx = nav_bar.selected_index
            if idx == 0:
                conteudo.controls.append(ft.Text("Você está logado com sucesso!"))
            elif idx == 2:
                conteudo.controls.append(ft.Text(f"Perfil do usuário: {user}"))
            elif idx == 1:
                conteudo.controls.extend([
                    ft.Text("Velocidade:"),
                    ft.Slider(ref=velocidade, min=0, max=100, divisions=10, value=0),
                    ft.ElevatedButton("Run", on_click=run_clicked)
                ])
            conteudo.update()

        nav_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
                ft.NavigationBarDestination(icon=ft.Icons.SPEED, label="Speed"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ],
            on_change=on_nav_change
        )

        # Monta a view com o conteúdo
        page.views.clear()
        page.views.append(
            ft.View(
                "/home",
                controls=[
                    ft.AppBar(title=ft.Text("Bem-vindo, " + user)),
                    conteudo,
                    nav_bar
                ]
            )
        )
        page.update()
        atualizar_conteudo_visivel()  # <- SÓ AQUI ESTÁ SEGURO


    def login(e):
        user = user_login.value
        senha = senha_login.value
        if user in usuarios and usuarios[user] == senha:
            mostrar_tela_home(user)
        else:
            msg_login.value = "Email ou senha inválidos."
            msg_login.update()

    def cadastrar(e):
        user = email_cadastro.value
        senha = senha_cadastro.value
        if user in usuarios:
            msg_cadastro.value = "Usuário já existe."
        else:
            usuarios[user] = senha
            msg_cadastro.value = "Cadastro realizado com sucesso!"
        msg_cadastro.update()

    # View Login
    user_login = ft.TextField(label="Usuário")
    senha_login = ft.TextField(label="Senha", password=True)
    msg_login = ft.Text(value="", color=ft.Colors.RED)
    view_login = ft.View(
        "/login",
        [
            ft.Text("Login", size=30),
            user_login,
            senha_login,
            ft.ElevatedButton("Entrar", on_click=login),
            msg_login,
            ft.TextButton("Cadastrar", on_click=lambda _: mostrar_tela_cadastro())
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # View Cadastro
    email_cadastro = ft.TextField(label="Usuário")
    senha_cadastro = ft.TextField(label="Senha", password=True)
    msg_cadastro = ft.Text(value="", color=ft.Colors.GREEN)
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

