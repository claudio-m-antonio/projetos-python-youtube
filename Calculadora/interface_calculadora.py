import PySimpleGUI as sg
from calculadora import calcular

fonte_grande = ('Helvetica', 24)

layout = [
    [sg.Input(size=(18, 1), justification='right', font=fonte_grande, key='-DISPLAY-')],
    [sg.Button('C', font=fonte_grande, size=(4, 2)), sg.Button('1', font=fonte_grande, size=(4, 2)), sg.Button('2', font=fonte_grande, size=(4, 2)), sg.Button('3', font=fonte_grande, size=(4, 2)), sg.Button('4', font=fonte_grande, size=(4, 2))],
    [sg.Button('5', font=fonte_grande, size=(4, 2)), sg.Button('6', font=fonte_grande, size=(4, 2)), sg.Button('7', font=fonte_grande, size=(4, 2)), sg.Button('8', font=fonte_grande, size=(4, 2)), sg.Button('9', font=fonte_grande, size=(4, 2))],
    [sg.Button('0', font=fonte_grande, size=(4, 2)), sg.Button('+', font=fonte_grande, size=(4, 2)), sg.Button('-', font=fonte_grande, size=(4, 2)), sg.Button('*', font=fonte_grande, size=(4, 2)), sg.Button('/', font=fonte_grande, size=(4, 2))],
    [sg.Button('^', font=fonte_grande, size=(4, 2)), sg.Button('√', font=fonte_grande, size=(4, 2)), sg.Button('=', font=fonte_grande, size=(4, 2))]  # Usando os símbolos para Potência e Raiz
]

window = sg.Window('Calculadora', layout, return_keyboard_events=True)
expressao = ''

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'C':
        expressao = ''
    elif event == '=':
        resultado = calcular(expressao)
        expressao = resultado if resultado != 'Erro' else ''
    elif event == '^':
        expressao += '**'
    elif event == '√':
        expressao = f'sqrt({expressao})' if expressao else ''
    else:
        expressao += event

    window['-DISPLAY-'].update(expressao)

window.close()
