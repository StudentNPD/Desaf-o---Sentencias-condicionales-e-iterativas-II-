# Actividad 3 - Fuerza bruta
# Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en
# minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras
# posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la
# contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha

from string import ascii_lowercase
import getpass


#solicita que ingrese la contraseña
contrasena = getpass.getpass(prompt="Ingresa la contraseña a adivinar: ")
#convierte la contraseña a minusculas
def fuerza_bruta(contrasena):
    intentos = 0
    contrasena_buscada = "" #almacena la contraseña
    
    for letra_contrasena in contrasena:
        for letra in ascii_lowercase:
            intentos += 1   #va poniendo en aumento el numero de intentos
            print(f"Intento {intentos}: {contrasena_buscada + letra}") #imprime las letras en los intentos
            
            if letra == letra_contrasena: #el comparador de letras
                contrasena_buscada += letra #rompe el ciclo cuando la contraseña llega su final porque no debe colocar mas letras
                break

    print(f"Contraseña encontrada: {contrasena_buscada} en {intentos} intentos")

fuerza_bruta(contrasena)



