#!/usr/bin/python

# Modulos 
import socks
import socket
import requests
from requests.exceptions import ConnectionError
import os
import time
import sys

# Colores de terminal
colores = {
        "M" :  "\033[1;31m",
        "H" :  "\033[1;32m",
        "K" :  "\033[1;33m",
        "U" :  "\033[1;34m",
        "P" :  "\033[1;35m",
        "C" :  "\033[1;36m",
        "W":  "\033[1;37m",
        "A" :  "\033[90m",

}

# Banner
class Banner:
    def __str__(self):
        return colores["P"]+"""

 ___                                      _             _____
|  _`\                                   ( )_          (_   _)
| (_) )   __     _ _  _   _    __    ___ | ,_)  ___      | |   _    _ __
| ,  /  /'__`\ /'_` )( ) ( ) /'__`\/',__)| |  /',__)     | | /'_`\ ( '__)
| |\ \ (  ___/( (_) || (_) |(  ___/\__, \| |_ \__, \     | |( (_) )| |
(_) (_)`\____)`\__, |`\___/'`\____)(____/`\__)(____/     (_)`\___/'(_)
                  | |
                  (_)
        """
x = Banner()
print(x)

# Imprime error
class Error:
    pass
    def __init__(self,tor):
        self.tor = tor
    def close(self):
        return "Asegúrate que tú servicio {} este corriendo".format(self.tor)

y = Error("Tor")

# Petición de URL
url = str(input(colores["K"]+"Ingrese una URL: "))

# Conexión por el proxy Tor
def Tor():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
	socket.socket = socks.socksocket

# Función main
def main():
        Tor() # Llamada al proxy de Tor
        print(y.close())
        time.sleep(1)
        r = requests.get(url)
        try:
            for header in r.headers.keys():
	            print(header + " : " + r.headers[header]) # Envío de cabeceras
        # Excepciones
        except ConnectionError:
            print(y.close())
            sys.exit(0)
        except AttributeError:
            pass
        except KeyboardInterrupt:
            sys.exit(1)
        finally:
            # Envío de respuestas por el proxy de Tor con requests 
            response = requests.get(url) 
            response = requests.post(url)
            print("El servidor dio una respuesta:\n")
            time.sleep(1)
            print(response.status_code)
            print("")
            print("Cabeceras:\n")
            time.sleep(1)
            print(response.headers)
            print("")
            print("Solicitud de cabeceras:\n")
            time.sleep(1)
            print(response.request.headers)
            print("")
            print("Texto de respuesta:\n")
            time.sleep(1)
            print(response.text)
            print("")
            print("Contenido de respuesta:\n")
            time.sleep(1)
            print(response.content)
            print("")

if __name__ == '__main__':
    main()
