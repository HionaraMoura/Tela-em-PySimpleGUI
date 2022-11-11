from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Darkpurple1') 
Layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario',size=(20,1))] ,
    [sg.Text ('Senha'),sg.Input(key='senha',password_char ='*',size=(20,1))],
    [sg.Checkbox ('Salvar o login?')],
    [sg.Button ('Entrar')]
] 
#Janela
Janela = sg.Window ('Tela de login', Layout)
#Ler os eventos 
while True:
    eventos,valores = Janela.read() 
    if eventos == sg.WINDOW_CLOSED:
        break    
    if eventos == 'Entrar':
    
      if valores ['usuario'] == 'Hionara' and valores['senha'] == '1234':
        print('Bem-vindo ao Meu Primeiro Projeto!')