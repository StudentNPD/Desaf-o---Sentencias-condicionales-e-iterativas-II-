from string import ascii_lowercase

#solicita que ingrese la contraseña
contrasena = input("Ingresa la contraseña a adivinar: ")
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