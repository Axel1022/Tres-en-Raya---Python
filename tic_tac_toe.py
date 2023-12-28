#imports
import random
from tkinter import Button, Frame, Label, Tk

def next_turn(row, col):
    global player
    # Verifica si la celda está vacía y no hay un ganador
    if buttons[row][col]['text'] == '' and check_winner() is False:
        # Jugador actual realiza su movimiento
        if player == players[0]:
            buttons[row][col]['text'] = player
            # Verifica si hay un ganador después del movimiento
            if check_winner() is False:
                # Cambia al siguiente jugador y actualiza la etiqueta
                player = players[1]
                label.config(text=players[1] + " turn")
            elif check_winner() is True:
                label.config(text=players[0] + " wins")
            elif check_winner() == 'Empate':
                pintar_red()
                label.config(text="Empate!")
        else:
            buttons[row][col]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=players[0] + " turn")
            elif check_winner() is True:
                label.config(text=players[1] + " wins")
            elif check_winner() == 'Empate':
                pintar_red()
                label.config(text="Empate!")

def pintar_red():
    # Cambia el fondo de las celdas a rojo en caso de empate
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(bg='red')

def check_winner():
    # Verifica si hay un ganador en filas y columnas
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != '':
            buttons[row][0].config(bg= 'green')
            buttons[row][1].config(bg= 'green')
            buttons[row][2].config(bg= 'green')
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != '':
            buttons[0][col].config(bg= 'green')
            buttons[1][col].config(bg= 'green')
            buttons[2][col].config(bg= 'green')
            return True

    # Verifica si hay un ganador en las diagonales
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg= 'green')
        buttons[2][2].config(bg= 'green')
        buttons[1][1].config(bg= 'green')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg= 'green')
        buttons[2][0].config(bg= 'green')
        buttons[1][1].config(bg= 'green')
        return True

    # Verifica si hay un empate
    elif empty_spaces() is  False:
        return 'Empate'
    else:
        return False

def empty_spaces():
    # Verifica si hay celdas vacías
    count = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != '':
                count -= 1
    if count ==0:
        return False

def new_game():
    # Inicia un nuevo juego
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    # Reinicia el tablero y el color de fondo de las celdas
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(bg='white')
            buttons[row][col]['text'] = ''

# Configuración de la interfaz gráfica
window = Tk()
window.title("Tres en Raya")
players = ["x", "0"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text='Restart', font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        # Configuración de los botones del juego
        buttons[row][col] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

# Inicia el bucle principal de la interfaz gráfica
window.mainloop()

