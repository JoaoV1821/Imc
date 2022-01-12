import PySimpleGUI as sg # Importa a biblioteca de interface gráfica
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED # Importa os métodos da classe "PySimpleGUI"
from Imc import * # Imporata a classe Imc

class Sistema_imc: # Definição do sistema Imc
    @staticmethod
    def janela_principal(): # Janela principal
        layout = [
           [sg.Text('Peso(Kg):', justification='left'), sg.Input(key='peso', size=(20, 20))],
           [sg.Text('Altura(m):', justification='left'), sg.Input(key='altura', size=(20, 20))],
           [sg.Button('Enviar'), sg.Button('Sair')]
        ]

        return sg.Window('IMC', layout) # retorno da janela com layout pré-definido
    
    def window_init(self): # Método que administra as informações da janela
        window = self.janela_principal() # atribui a janela à uma variável

        while True: # loping da janela
            event, values = window.read() # leitura da janela

            if event == WINDOW_CLOSED or event == 'Sair': # Verifica se a janela foi fechada
                break

            if event == 'Enviar':
                try:
                    imc = Imc(values['altura'].strip(), values['peso'].strip()) # Atribui os valores ao construtor
                except Exception as E: # Captura as exceções
                    sg.popup(E) # Pop-up com a mensagem de erro
                else:
                    sg.popup(f'Seu IMC é {imc.imc}Kg/m²\nClassificação: {imc.classificacao}') # Pop-up com a saída dos dados

        window.close() # Fecha a janela

if __name__ == '__main__':
    sistema = Sistema_imc()
    sistema.window_init()