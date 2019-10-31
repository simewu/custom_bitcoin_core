import os
import json
import time
import re

directory = '~/Desktop/custom_bitcoin_core' # Virtual machine shared folder
if os.path.exists('/media/sf_Bitcoin/'):
	directory = '/media/sf_Bitcoin/' # Virtual machine shared folder

def bitcoin(cmd):
	#return os.popen('\'C:\\Program Files\\Bitcoin\\daemon\\bitcoin-cli\' -rpcuser=simewu -rpcpassword=kZIdeN4HjZ3fp9Lge4iezt0eJrbjSi8kuSuOHeUkEUbQVdf09JZXAAGwF3R5R2qQkPgoLloW91yTFuufo7CYxM2VPT7A5lYeTrodcLWWzMMwIrOKu7ZNiwkrKOQ95KGW8kIuL1slRVFXoFpGsXXTIA55V3iUYLckn8rj8MZHBpmdGQjLxakotkj83ZlSRx1aOJ4BFxdvDNz0WHk1i2OPgXL4nsd56Ph991eKNbXVJHtzqCXUbtDELVf4shFJXame -rpcport=8332 ' + cmd).read()
	return os.popen(directory + '/bitcoin/src/bitcoin-cli -datadir=/media/sim/BITCOIN/ ' + cmd).read()


def console(width):
	os.system('clear')
	print('-' * width)
	print('Bitcoin Console'.center(width))
	print('-' * width)
	count = 1
	commands = {}
	while True:
		numTimes = 1
		cmd = input(str(count).ljust(4) + '>   ')
		cmds = re.split(r'\s*\*\s*(?=[0-9]+$)', cmd)
		if len(cmds) == 2: # Add command multiplier
			cmd = cmds[0]
			numTimes = int(cmds[1])

		if len(cmd) == 0:
			cmd = count - 1
		elif re.match(r'[0-9]+', cmd):
			cmd = int(cmd)
		if(cmd in commands):
			cmd = commands[cmd]
			print('    >   ' + cmd)
		else:
			cmd = str(cmd)
			commands[count] = cmd
			count += 1
		print()

		for i in range(numTimes - 1):
			bitcoin(cmd)
		print('   ' + bitcoin(cmd))
		print('-' * width)

console(80)