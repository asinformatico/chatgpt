import openai
import csv
import sys
import os
import platform
from colorama import Fore, Back, init

init()

nombre_sistema = platform.system()
if nombre_sistema == "Windows":
    os.system('cls')
else:
    os.system('clear')

# En el archivo mi_api_key debe estar la Clave API que nos ha proporcionado OpenAI.
with open('mi_api_key', newline='') as key:
	claves_api = csv.reader(key)
	for clave in claves_api:
		chars = '[\']'
		clave = str(clave).translate(str.maketrans('', '', chars))
		openai.api_key = clave
		
pregunta = ''
salida = ['salir','exit','bye','adios', 'chao', 'quit']
print(Back.RED + Fore.WHITE + '\nChatGPT para Línea de Comandos by @as_informatico\n\n')
print(Back.BLACK + 'Uso:\n1- Escriba su consulta o petición y pulse Enter.\n2- Espere su respuesta.\n'
	  '3- Para finalizar el programa puede utilizar:\nexit, salir, quit, adios, bye o chao.\n\n')

while -1:
	pregunta = input(Fore.WHITE + 'Introduzca su pregunta: ')
	if pregunta in salida:
		sys.exit(Fore.RED + 'Programa finalizado por el usuario')
		
	if pregunta.strip() == '':
		print('Debe escribir algo antes de enviar...')
	else:
		respuesta = openai.Completion.create(engine='text-davinci-003', prompt=pregunta, n=1, max_tokens=4000)
		print(Fore.YELLOW + str(respuesta.choices[0].text) + '\n' + Fore.WHITE + '=' * 50 + '\n\n')
