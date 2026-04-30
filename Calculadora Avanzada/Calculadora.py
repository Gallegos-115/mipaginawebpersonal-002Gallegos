# Calculadora Avanzada #
# Mi nombre es Héctor Gallegos y hoy 'creare' una calculadora más# 
# usando los siguientes comandos 'ValueError' , 'ZeroDivisionError' , 'FileNotFoundError' #
# Esta calculadora contiene las siguientes caracteristicas :
    # 1. Operadores básicos como por ejemplo :
            # - Suma , Resta , Multiplicación y División.
           
    # 2. Operadores más avanzados :
            # - Potencía, Raíz Cuadrada y Porcentaje.

    # 3. Función de Guardado :
            # Historial de de cálculos , lectura de Archivos y Guardar resultados.

# Fin.

# Librerías #

from colorama import Fore, Style , init 
import time
import sys
import pyfiglet
init ()

# 1. Título (No entendi mucho al inicio pero logre pillarle el truco.) #

def Mostrar_Titulo():
    titulo = pyfiglet.figlet_format("CALCULADORA")
    print(Fore.YELLOW + titulo + Style.RESET_ALL)

Mostrar_Titulo ()

# 2. Una pantalla de carga : ) #

def pantalla_de_carga ():
    
        for i in range (101):
                barra = Fore.GREEN + "█" * (i // 5)
                print (Fore.CYAN + f"\rCargando : {Fore.RESET} [{barra:<20}] {i}%", end= "")
                time.sleep(0.2)

        print ("\n Sistema listo \n")

pantalla_de_carga ()


