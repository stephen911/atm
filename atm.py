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
																								