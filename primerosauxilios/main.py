def main():
    print("Guía de primeros auxilios.")

    while True:
        print("\n¿La persona responde a estímulos? (sí/no)")
        respuesta = input().strip().lower()

        if respuesta == "sí":
            print("Valorar la necesidad de llevarlo al hospital más cercano.")
        elif respuesta == "no":
            abrir la vía aérea()

def abrir_vía_aérea():
    print("\nAbrir la vía aérea.")
    print("¿La persona respira? (sí/no)")
    respuesta = input().strip().lower()

    if respuesta == "sí":
        print("Permitirle posición de suficiente ventilación.")
    elif respuesta == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia.")
        signos_de_vida()
    else:
        print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")

def signos_de_vida():
    print("\n¿La persona tiene signos de vida? (sí/no)")
    respuesta = input().strip().lower()

    if respuesta == "sí":
        print("Reevaluar a la espera de la ambulancia.")
    elif respuesta == "no":
        print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
        llego_ambulancia()
    else:
        print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")

def llego_ambulancia():
    while True:
        print("\n¿Llegó la ambulancia? (sí/no)")
        respuesta = input().strip().lower()

        if respuesta == "sí":
            print("Fin.")
            break
        elif respuesta == "no":
            print("¿La persona tiene signos de vida? (sí/no)")
            respuesta_signos = input().strip().lower()

            if respuesta_signos == "sí":
                print("Reevaluar a la espera de la ambulancia.")
            elif respuesta_signos == "no":
                print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
            else:
                print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")
        else:
            print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")

    main()
