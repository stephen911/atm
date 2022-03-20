~!/usr/bin/python
import getpass
import string
import os

~ creatinga lists of users, their PINs and bank statements
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
~ while loop checks existance of the enterd username
while True:
		user = input('\nENTER USER NAME: ')
			user = user.lower()
				if user in users:
							if user == users[0]:
											n = 0
													elif user == users[1]:
																	n = 1
																			else:
																							n = 2
																									break
																									else:
																												print('----------------')
																														print('****************')
																																print('INVALID USERNAME')
																																		print('****************')
																																				print('----------------')

																																				~ comparing pin
																																				while count < 3:
																																						print('------------------')
																																							print('******************')
																																								pin = str(getpass.getpass('PLEASE ENTER PIN: '))
																																									print('******************')
																																										print('------------------')
																																											if pin.isdigit():
																																														if user == 'user1':
																																																		if pin == pins[0]:
																																																							break
																																																									else:
																																																														count += 1
																																																																		print('-----------')
																																																																						print('***********')
																																																																										print('INVALID PIN')
																																																																														print('***********')
																																																																																		print('-----------')
																																																																																						print()

																																																																																								if user == 'user2':
																																																																																												if pin == pins[1]:
																																																																																																	break
																																																																																																			else:
																																																																																																								count += 1
																																																																																																												print('-----------')
																																																																																																																print('***********')
																																																																																																																				print('INVALID PIN')
																																																																																																																								print('***********')
																																																																																																																												print('-----------')
																																																																																																																																print()

																																																																																																																																						if user == 'user3':
																																																																																																																																										if pin == pins[2]:
																																																																																																																																															break
																																																																																																																																																	else:
																																																																																																																																																						count += 1
																																																																																																																																																										print('-----------')
																																																																																																																																																														print('***********')
																																																																																																																																																																		print('INVALID PIN')
																																																																																																																																																																						print('***********')
																																																																																																																																																																										print('-----------')
																																																																																																																																																																														print()
																																																																																																																																																																															else:
																																																																																																																																																																																		print('------------------------')
																																																																																																																																																																																				print('************************')
																																																																																																																																																																																						print('PIN CONSISTS OF 4 DIGITS')
																																																																																																																																																																																								print('************************')
																																																																																																																																																																																										print('------------------------')
																																																																																																																																																																																												count += 1

																																																																																																																																																																																													~ in case of a valid pin- continuing, or exiting
																																																																																																																																																																																													if count == 3:
																																																																																																																																																																																															print('-----------------------------------')
																																																																																																																																																																																																print('***********************************')
																																																																																																																																																																																																	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
																																																																																																																																																																																																		print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
																																																																																																																																																																																																			print('***********************************')
																																																																																																																																																																																																				print('-----------------------------------')
																																																																																																																																																																																																					exit()

																																																																																																																																																																																																					print('-------------------------')
																																																																																																																																																																																																					print('*************************')
																																																																																																																																																																																																					print('LOGIN SUCCESFUL, CONTINUE')
																																																																																																																																																																																																					print('*************************')
																																																																																																																																																																																																					print('-------------------------')
																																																																																																																																																																																																					print()
																																																																																																																																																																																																					print('--------------------------')
																																																																																																																																																																																																					print('**************************')	
																																																																																																																																																																																																					print(str.capitalize(users[n]), 'welcome to ATM')
																																																																																																																																																																																																					print('**************************')
																																																																																																																																																																																																					print('----------ATM SYSTEM-----------')
																																																																																																																																																																																																					~ Main menu
																																																																																																																																																																																																					while True:
																																																																																																																																																																																																							~os.system('clear')
																																																																																																																																																																																																								print('-------------------------------')
																																																																																																																																																																																																									print('*******************************')
																																																																																																																																																																																																										response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
																																																																																																																																																																																																											print('*******************************')
																																																																																																																																																																																																												print('-------------------------------')
																																																																																																																																																																																																													valid_responses = ['s', 'w', 'l', 'p', 'q']
																																																																																																																																																																																																														response = response.lower()
																																																																																																																																																																																																															if response == 's':
																																																																																																																																																																																																																		print('---------------------------------------------')
																																																																																																																																																																																																																				print('*********************************************')
																																																																																																																																																																																																																						print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'EURO ON YOUR ACCOUNT.')
																																																																																																																																																																																																																								print('*********************************************')
																																																																																																																																																																																																																								