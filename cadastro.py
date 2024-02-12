import PySimpleGUI as sg


def main():
    layout = [
        [sg.Text('Usuário:'), sg.InputText(key='usuario')],
        [sg.Text('Email:'), sg.InputText(key='email')],
        [sg.Text('Senha:'), sg.InputText(key='senha', password_char='*')],
        [sg.Button('Cadastrar'), sg.Button('Cancelar')]
    ]

    window = sg.Window('Cadastro de Usuário', layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancelar'):
            break
        elif event == 'Cadastrar':
            usuario = values['usuario']
            email = values['email']
            senha = values['senha']
            
            with open("users.txt", "a") as arquivo: 
                arquivo.write(f'Usuario: {usuario}\nEmail: {email}\nSenha: {senha}' + "\n")

        
    window.close()

if __name__ == '__main__':
    main()
