import PySimpleGUI as sg
from Ventana import Ventana

class InicioSesion(Ventana):

    def build(self):
        layout = [
            [sg.Text('Gestion de datos de Axie Infinity',font=('Patua One'), justification='center')],
            [sg.Text('Usuario', font=('Patua One')), sg.Input(k='-user-')],
            [sg.Button('Ingresar', k='-OK-')]
        ]

        window = sg.Window('Inicio sesión', layout=layout)
        return window

    def loop(self):
        window = self.build() #-> devuelve la ventana que se construyo
        while True:
            event, values = window.read()
            if (event == sg.WINDOW_CLOSED):
                break
            if (event == '-OK-'):
                pass