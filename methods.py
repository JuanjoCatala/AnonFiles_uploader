import os
import sys
from colorama import Fore, Style

# Clean terminal

def clean():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")



def code_check(diccionary, request):

#--------------------- API exceptions ------------------------------------

	if diccionary["status"] == "false":  #Evaluates if there's any error

		error = diccionary["error"]  #We save error data section of json diccionary

		clean()
		print(Fore.RED + Style.BRIGHT + "Ups!, something has gone bad :(" + Style.RESET_ALL)
		print(" ")
		print(Fore.GREEN + Style.BRIGHT +"Error code: " + Style.RESET_ALL + error["code"])
		print(Fore.GREEN + Style.BRIGHT +"Error type: " + Style.RESET_ALL + error["type"])
		print(Fore.GREEN + Style.BRIGHT +"Error info: " + Style.RESET_ALL + error["message"])
		print(" ")



#---------------------- HTTP exceptions -------------------------------

	
	if request.status_code == 400:
		clean()
		print(Fore.RED + Style.BRIGHT + "Client error (400)" + Style.RESET_ALL)
		print(" ")

	if request.status_code == 403:
		clean()
		print(Fore.RED + Style.BRIGHT + "Server refused connection (403)" + Style.RESET_ALL)
		print(" ")
	if request.status_code == 404:
		clean()
		print(Fore.RED + Style.BRIGHT + "Not found (404)" + Style.RESET_ALL)
		print(" ")