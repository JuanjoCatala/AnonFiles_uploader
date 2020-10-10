import os
import sys
import time
import argparse
import requests, json
import methods
import datetime
from colorama import Fore, Style 

methods.clean()

# Veryfing folder

if os.path.isdir("upload"):
	time.sleep(0.1)
else:
	os.mkdir("upload")
	methods.clean()
	print(Fore.BLUE + Style.BRIGHT + "folder 'upload' created, move your files to be uploaded there and restart the script" + Style.RESET_ALL)
	print("")
	sys.exit()


try: 
	
	# Saving paths

	path = os.getcwd()
	path_upload = path + "/upload"

	# Setting arguments 

	parser = argparse.ArgumentParser(description= "Upload files to anonfiles.com")

	parser.add_argument('-f', '--filename', metavar='', type=str, required=True, help="input filename (in upload, in script's folder)")
	parser.add_argument('-p', '--proxy', metavar='', type=str, required=False, help='do requests with http/https proxy (proxy:port)')
	parser.add_argument('-t', '--tor', metavar='', type=bool, required=False, help='set to True to use tor')
	parser.add_argument('-o', '--output', metavar='', type=str, required=False, help='path to save all info related to file uploaded as a txt')

	arg = parser.parse_args()

	# Changing path

	os.chdir(path_upload)

	# read file to send

	file_send = open(arg.filename, "rb")

	#Performing requests 

	done_with_proxy = False
	done_with_tor = False
	
# --------------------------------------------------------------------------------------------------------------
	if arg.tor and arg.proxy != None:   #No valid

		methods.clean()
		print(Fore.RED + Style.BRIGHT + "You can't use tor proxy and proxy at the same time" + Style.RESET_ALL)
		sys.exit()
# --------------------------------------------------------------------------------------------------------------

	if arg.tor and arg.proxy == None:   # tor request

		proxy = {
				'http' : "socks5://127.0.0.1:9050",
				'https' : "socks5://127.0.0.1:9050"
			}
			
		methods.clean()
		print(Fore.RED + Style.BRIGHT + "Request will be done with tor" + Style.RESET_ALL)
		time.sleep(2)
		methods.clean()
		print(Fore.BLUE + Style.BRIGHT + "Sending Data... this could take a while" + Style.RESET_ALL)
		request = requests.post('https://api.anonfiles.com/upload', proxies=proxy, files={"file":file_send})
		done_with_tor = True
		
# --------------------------------------------------------------------------------------------------------------

	if arg.proxy != None: #proxy request

		proxy = {
				'http' : "http://" + arg.proxy,
				'https' : "https://" + arg.proxy
			}
		print(Fore.RED + Style.BRIGHT + "Request will be done with proxy" + Style.RESET_ALL)
		time.sleep(2)
		methods.clean()
		print(Fore.BLUE + Style.BRIGHT + "Sending Data... this could take a while" + Style.RESET_ALL)
		request = requests.post('https://api.anonfiles.com/upload', proxies=proxy, files={"file":file_send})
		done_with_proxy = True
# --------------------------------------------------------------------------------------------------------------
	if arg.tor != True and arg.proxy == None: #normal request

		print(Fore.BLUE + Style.BRIGHT + "Sending Data... this could take a while" + Style.RESET_ALL)
		request = requests.post('https://api.anonfiles.com/upload', files={"file":file_send})
# --------------------------------------------------------------------------------------------------------------



	#Saving Json 

	str_json_recived = json.dumps(request.json())
	diccionary = json.loads(str_json_recived)


	# We verify the http codes

	methods.code_check(diccionary, request)

	# save date and hour

	time = datetime.datetime.now()

	# printing all file info

	print(" ")

	data = diccionary["data"]
	file = data ["file"]
	metadata = file["metadata"]
	size = metadata["size"]
	url = file["url"]

	methods.clean()

	time = datetime.datetime.now()

	print(" ")
	print(Fore.BLUE + Style.BRIGHT + "Upload date: " + Style.RESET_ALL + str(time))
	print(" ")


	if done_with_tor:   #if tor request we add this header
		print(" ")
		print(Fore.RED + Style.BRIGHT + "--[!] Uploaded with tor [!]--" + Style.RESET_ALL)
		print(" ")
	if done_with_proxy: #if proxy request we add this header
		print(" ")
		print(Fore.RED + Style.BRIGHT + "--[!] Uploaded with proxy (" + arg.proxy + ") [!]--" + Style.RESET_ALL)
		print(" ")


	print(" ")
	print(Fore.GREEN + Style.BRIGHT + "[*] URL: " + Style.RESET_ALL)
	print(" ")
	print(url["full"])
		
	print(" ")
	print(Fore.GREEN + Style.BRIGHT + "[*] File info:" + Style.RESET_ALL)
	print(" ")
	print(Fore.BLUE + Style.BRIGHT + "Name: " + Style.RESET_ALL + metadata["name"] + Style.RESET_ALL)
	print(Fore.BLUE + Style.BRIGHT + "Size: " + Style.RESET_ALL + size["readable"] + Style.RESET_ALL)
	print(Fore.BLUE + Style.BRIGHT + "Anonfiles id: " + Style.RESET_ALL + metadata["id"])
	print(" ")

	
	# if output

	if arg.output != None:

		# Checking last letter of path

		length = len(arg.output)

		if arg.output[length-1] != "/":

			arg.output = arg.output + "/"

		# writting info

		file_output = open(arg.output + arg.filename + "_output_" + ".txt", "a")
		file_output.write("\n" + "--------------------------------------------------------------------")
		file_output.write("\n" + str(time))
		if done_with_tor:
			file_output.write("\n" + " ")
			file_output.write("\n" +"--[!] Uploaded with tor [!]--")
			file_output.write("\n" + " ")
		if done_with_proxy:
			file_output.write("\n" + " ")
			file_output.write("\n" + "--[!] Uploaded with proxy (" + arg.proxy + ") [!]--" )
			file_output.write("\n" + " ")
		file_output.write("\n" + " ")
		file_output.write("\n" + "[*] URL: ")
		file_output.write("\n" +" ")
		file_output.write("\n" + url["full"])
		file_output.write("\n" + " ")
		file_output.write("\n" + "[*] File info:")
		file_output.write("\n" + " ")
		file_output.write("\n" +"Name: " + metadata["name"])
		file_output.write("\n" +"Size: " + size["readable"])
		file_output.write("\n" +"Anonfiles id: " + metadata["id"])
		file_output.write("\n" + "--------------------------------------------------------------------")
		file_output.write("\n" + " ")

		file_output.close()
		print(Fore.GREEN + Style.BRIGHT + "File saved with succes into: " + Style.RESET_ALL + arg.output + Fore.GREEN + Style.BRIGHT + " as " + Style.RESET_ALL + arg.filename + "_output_" + ".txt")
		print(" ")


except FileNotFoundError:
	methods.clean()
	print(Fore.RED + Style.BRIGHT + "Sorry, file not found. Make sure it's in upload folder" + Style.RESET_ALL)
	print(" ")

except requests.exceptions.ConnectionError:
	methods.clean()
	print(Fore.RED + Style.BRIGHT + "Can't connect to server (check your internet/proxy)" + Style.RESET_ALL)
	print(" ")

except KeyboardInterrupt:
	methods.clean()
	print(Fore.GREEN + Style.BRIGHT + "Have a nice day :)" + Style.RESET_ALL)

except json.decoder.JSONDecodeError:
	print(Fore.RED + Style.BRIGHT + "Error processing json (try again)" + Style.RESET_ALL)
