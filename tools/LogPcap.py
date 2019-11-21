import os
import json
import time
import re
import os

def cmd(cmd):
	return os.popen(cmd).read()

def main():
	os.system('clear')
	timeout = int(input('How many seconds should a new file be created? '))

	path = os.path.expanduser('~/Desktop/pcap_logs')
	if not os.path.exists(path):
	    os.makedirs(path)

	count = 1
	while True:
		print(f'\nWriting to {path}/pcap_log_{count}')
		command = f'sudo timeout {timeout}s tcpdump -w {path}/pcap_log_{count}'
		cmd(command)
		count += 1

main()