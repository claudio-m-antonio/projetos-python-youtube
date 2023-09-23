import PySimpleGUI as sg
import math
from calculadora import calcular

fonte_grande = ('Helvetica', 24)

layout = [
    [sg.Input(size=(18, 1), justification='right', font=fonte_grande, key='-DISPLAY-')],
    [
        sg.Button('C', font=fonte_grande, size=(4, 2)),
        sg.Button('1', font=fonte_grande, size=(4, 2)),
        sg.Button('2', font=fonte_grande, size=(4, 2)),
        sg.Button('3', font=fonte_grande, size=(4, 2)),
        sg.Button('4', font=fonte_grande, size=(4, 2))
    ],
    [
        sg.Button('5', font=fonte_grande, size=(4, 2)),
        sg.Button('6', font=fonte_grande, size=(4, 2)),
        sg.Button('7', font=fonte_grande, size=(4, 2)),
        sg.Button('8', font=fonte_grande, size=(4, 2)),
        sg.Button('9', font=fonte_grande, size=(4, 2))
    ],
    [
        sg.Button('0', font=fonte_grande, size=(4, 2)),
        sg.Button('+', font=fonte_grande, size=(4, 2)),
        sg.Button('-', font=fonte_grande, size=(4, 2)),
        sg.Button('×', font=fonte_grande, size=(4, 2)),  # × representa a multiplicação
        sg.Button('/', font=fonte_grande, size=(4, 2))
    ],
    [
        sg.Button('x²', font=fonte_grande, size=(4, 2)),
        sg.Button('√', font=fonte_grande, size=(4, 2)),
        sg.Button('=', font=fonte_grande, size=(4, 2))
    ]
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
        expressao = str(resultado) if resultado != 'Erro' else ''

    elif event == 'x²':
        # Verifique se há um número antes de calcular x²
        if expressao and expressao[-1].isdigit():
            expressao = calcular(expressao)
            expressao = str(float(expressao) ** 2)
        else:
            expressao = ''
    elif event == '√':
        # Verifique se há um número antes de calcular a raiz quadrada
        if expressao and expressao[-1].isdigit():
            resultado = calcular(expressao)
            if resultado != 'Erro' and float(resultado) >= 0:
                expressao = str(math.sqrt(float(resultado)))
            else:
                expressao = 'Erro'
        else:
            expressao = ''
    elif event == '×':  # Lógica de multiplicação
        expressao += '*'
    else:
        expressao += event

    window['-DISPLAY-'].update(expressao)

window.close()
