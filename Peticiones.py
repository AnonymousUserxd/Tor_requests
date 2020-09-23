# Modulos 
import socks
import socket
import requests
from requests.exceptions import ConnectionError
import os
import time
import sys

# Petición de URL
url = str(input("Ingrese una URL: "))

# Conexión por el proxy Tor
def Tor():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
	socket.socket = socks.socksocket

# Función main
def main():
        Tor() # Llamada al proxy de Tor
        r = requests.get(url)
        try:
            for header in r.headers.keys():
	            print(header + " : " + r.headers[header]) # Envío de cabeceras
        # Excepciones
        except ConnectionError:
            print("Revisa que tú servicio Tor este corriendo")
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
