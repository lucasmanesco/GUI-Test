import PySimpleGUI as psg

layout = [
    [psg.Text('Largura', size=(15,1)), psg.Input()],  # row 1
    [psg.Text('Comprimento', size=(15,1)), psg.Input()],  # row 2
    [psg.Text('Altura', size=(15,1)), psg.Input()],  # row 3
    [psg.Text('kb = 1.5', size=(15,1))],  # row 4
    [psg.OK()],  # row 5
]

window = psg.Window('Form', layout, size=(715,150))

while True:
    
    event, entries = window.read()
    
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    
    print(event, entries)
    
    dimensions = []
    for val in entries.values():
        try:
            val = float(val)
        except ValueError:
            print('Digite as informações corretamente.')
        dimensions.append(val)
    
    l, c, a = dimensions
    vol = a * l * c                                                         ## CALCULO VOLUME DO TRECHO
    sup = 2.00 * ((c * l) + (c * a) + (l * a))                              ## CALCULO SUPERFICIE DO TRECHO
    mas = 1.5 * ((0.75 * vol) + (0.20 * sup))                                ## CALCULO MASSA CO2

    if mas_total <= 10:
    print('Utilizar Cilindro de CO² de 10kg\n')
    else:
    if mas_total >= 10 and mas_total <=20:
        print('Utilizar Cilindro de CO² de 20kg\n')
    else:
        print('Utilizar Cilindro de CO² de 30kg\n')

    print(vol, sup, mas)

window.close()

