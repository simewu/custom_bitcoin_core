import os
import json
import time
import re

datadir = '/media/sim/BITCOIN/' # Virtual machine shared folder
if os.path.exists('/media/sf_Bitcoin'):
	datadir = '/media/sf_Bitcoin' # Virtual machine shared folder
elif os.path.exists('../blocks'):
	datadir = '..' # Super computer shared folder

def bitcoin(cmd):
	#return os.popen('\'C:\\Program Files\\Bitcoin\\daemon\\bitcoin-cli\' -rpcuser=cybersec -rpcpassword=kZIdeN4HjZ3fp9Lge4iezt0eJrbjSi8kuSuOHeUkEUbQVdf09JZXAAGwF3R5R2qQkPgoLloW91yTFuufo7CYxM2VPT7A5lYeTrodcLWWzMMwIrOKu7ZNiwkrKOQ95KGW8kIuL1slRVFXoFpGsXXTIA55V3iUYLckn8rj8MZHBpmdGQjLxakotkj83ZlSRx1aOJ4BFxdvDNz0WHk1i2OPgXL4nsd56Ph991eKNbXVJHtzqCXUbtDELVf4shFJXame -rpcport=8332 ' + cmd).read()
	return os.popen(f'bitcoin/src/bitcoin-cli -datadir={datadir} {cmd}').read()


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
		elif cmd.endswith('*'): # Infinite loop
			cmd = str(cmd[:-1])
			print(cmd)
			while True:
				bitcoin(cmd)
			return
		else:
			cmd = str(cmd)
			commands[count] = cmd
			count += 1
		print()

		timeStart = time.perf_counter()
		for i in range(numTimes - 1):
			bitcoin(cmd)
		output = bitcoin(cmd)
		timeEnd = time.perf_counter()

		print(output)
		print(f'That took {str(timeEnd - timeStart)} seconds (external console).')
		print('-' * width)

console(80)
