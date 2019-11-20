import os
import re
import json
import datetime
from threading import Timer

numSecondsPerSample = 1

#def getmyIP():
#	return os.popen("curl \"http://myexternalip.com/raw\"").read() + ":8333"

def bitcoin(cmd):
	return os.popen("./../bitcoin/src/bitcoin-cli -rpcuser=simewu -rpcpassword=kZIdeN4HjZ3fp9Lge4iezt0eJrbjSi8kuSuOHeUkEUbQVdf09JZXAAGwF3R5R2qQkPgoLloW91yTFuufo7CYxM2VPT7A5lYeTrodcLWWzMMwIrOKu7ZNiwkrKOQ95KGW8kIuL1slRVFXoFpGsXXTIA55V3iUYLckn8rj8MZHBpmdGQjLxakotkj83ZlSRx1aOJ4BFxdvDNz0WHk1i2OPgXL4nsd56Ph991eKNbXVJHtzqCXUbtDELVf4shFJXame -rpcport=8332 " + cmd).read()

def fetchHeader():
	line = "Timestamp,"
	line += "Timestamp (Seconds),"
	line += "NumPeers,"
	line += "InactivePeers,"
	line += "AvgPingTime,"
	line += "TotalBanScore,"
	line += "Connections,"
	line += "ClocksPerSec,"

	line += "# VERSION,"
	line += "VERSIONClksAvg,"
	line += "VERSIONClksMax,"
	line += "VERSIONBytsAvg,"
	line += "VERSIONBytsMax,"
	line += "# VERACK,"
	line += "VERACKClksAvg,"
	line += "VERACKClksMax,"
	line += "VERACKBytsAvg,"
	line += "VERACKBytsMax,"
	line += "# ADDR,"
	line += "ADDRClksAvg,"
	line += "ADDRClksMax,"
	line += "ADDRBytsAvg,"
	line += "ADDRBytsMax,"
	line += "# INV,"
	line += "INVClksAvg,"
	line += "INVClksMax,"
	line += "INVBytsAvg,"
	line += "INVBytsMax,"
	line += "# GETDATA,"
	line += "GETDATAClksAvg,"
	line += "GETDATAClksMax,"
	line += "GETDATABytsAvg,"
	line += "GETDATABytsMax,"
	line += "# MERKLEBLOCK,"
	line += "MERKLEBLOCKClksAvg,"
	line += "MERKLEBLOCKClksMax,"
	line += "MERKLEBLOCKBytsAvg,"
	line += "MERKLEBLOCKBytsMax,"
	line += "# GETBLOCKS,"
	line += "GETBLOCKSClksAvg,"
	line += "GETBLOCKSClksMax,"
	line += "GETBLOCKSBytsAvg,"
	line += "GETBLOCKSBytsMax,"
	line += "# GETHEADERS,"
	line += "GETHEADERSClksAvg,"
	line += "GETHEADERSClksMax,"
	line += "GETHEADERSBytsAvg,"
	line += "GETHEADERSBytsMax,"
	line += "# TX,"
	line += "TXClksAvg,"
	line += "TXClksMax,"
	line += "TXBytsAvg,"
	line += "TXBytsMax,"
	line += "# HEADERS,"
	line += "HEADERSClksAvg,"
	line += "HEADERSClksMax,"
	line += "HEADERSBytsAvg,"
	line += "HEADERSBytsMax,"
	line += "# BLOCK,"
	line += "BLOCKClksAvg,"
	line += "BLOCKClksMax,"
	line += "BLOCKBytsAvg,"
	line += "BLOCKBytsMax,"
	line += "# GETADDR,"
	line += "GETADDRClksAvg,"
	line += "GETADDRClksMax,"
	line += "GETADDRBytsAvg,"
	line += "GETADDRBytsMax,"
	line += "# MEMPOOL,"
	line += "MEMPOOLClksAvg,"
	line += "MEMPOOLClksMax,"
	line += "MEMPOOLBytsAvg,"
	line += "MEMPOOLBytsMax,"
	line += "# PING,"
	line += "PINGClksAvg,"
	line += "PINGClksMax,"
	line += "PINGBytsAvg,"
	line += "PINGBytsMax,"
	line += "# PONG,"
	line += "PONGClksAvg,"
	line += "PONGClksMax,"
	line += "PONGBytsAvg,"
	line += "PONGBytsMax,"
	line += "# NOTFOUND,"
	line += "NOTFOUNDClksAvg,"
	line += "NOTFOUNDClksMax,"
	line += "NOTFOUNDBytsAvg,"
	line += "NOTFOUNDBytsMax,"
	line += "# FILTERLOAD,"
	line += "FILTERLOADClksAvg,"
	line += "FILTERLOADClksMax,"
	line += "FILTERLOADBytsAvg,"
	line += "FILTERLOADBytsMax,"
	line += "# FILTERADD,"
	line += "FILTERADDClksAvg,"
	line += "FILTERADDClksMax,"
	line += "FILTERADDBytsAvg,"
	line += "FILTERADDBytsMax,"
	line += "# FILTERCLEAR,"
	line += "FILTERCLEARClksAvg,"
	line += "FILTERCLEARClksMax,"
	line += "FILTERCLEARBytsAvg,"
	line += "FILTERCLEARBytsMax,"
	line += "# SENDHEADERS,"
	line += "SENDHEADERSClksAvg,"
	line += "SENDHEADERSClksMax,"
	line += "SENDHEADERSBytsAvg,"
	line += "SENDHEADERSBytsMax,"
	line += "# FEEFILTER,"
	line += "FEEFILTERClksAvg,"
	line += "FEEFILTERClksMax,"
	line += "FEEFILTERBytsAvg,"
	line += "FEEFILTERBytsMax,"
	line += "# SENDCMPCT,"
	line += "SENDCMPCTClksAvg,"
	line += "SENDCMPCTClksMax,"
	line += "SENDCMPCTBytsAvg,"
	line += "SENDCMPCTBytsMax,"
	line += "# CMPCTBLOCK,"
	line += "CMPCTBLOCKClksAvg,"
	line += "CMPCTBLOCKClksMax,"
	line += "CMPCTBLOCKBytsAvg,"
	line += "CMPCTBLOCKBytsMax,"
	line += "# GETBLOCKTXN,"
	line += "GETBLOCKTXNClksAvg,"
	line += "GETBLOCKTXNClksMax,"
	line += "GETBLOCKTXNBytsAvg,"
	line += "GETBLOCKTXNBytsMax,"
	line += "# BLOCKTXN,"
	line += "BLOCKTXNClksAvg,"
	line += "BLOCKTXNClksMax,"
	line += "BLOCKTXNBytsAvg,"
	line += "BLOCKTXNBytsMax,"
	line += "# REJECT,"
	line += "REJECTClksAvg,"
	line += "REJECTClksMax,"
	line += "REJECTBytsAvg,"
	line += "REJECTBytsMax,"
	line += "# [UNDOCUMENTED],"
	line += "[UNDOCUMENTED]ClksAvg,"
	line += "[UNDOCUMENTED]ClksMax,"
	line += "[UNDOCUMENTED]BytsAvg,"
	line += "[UNDOCUMENTED]BytsMax,"
	return line

def parseMessage(string):
	line = ''
	numMsgs = re.findall(r"([0-9\.]+) msgs", string)[0]
	matches = re.findall(r"\[[0-9\., ]+\]", string)
	if len(matches) != 2:
		return None
	match1 = json.loads(matches[0])
	match2 = json.loads(matches[1])

	line += str(numMsgs) + ','		# Num
	line += str(match1[0]) + ','	# ClksAvg
	line += str(match1[1]) + ','	# ClksMax
	line += str(match2[0]) + ','	# BytsAvg
	line += str(match2[1])			# BytsMax
	return line


def fetch():
	now = datetime.datetime.now()
	line = str(now) + ","
	line += str((now - datetime.datetime(1970, 1, 1)).total_seconds()) + ","
	messages = json.loads(bitcoin("getmsginfo"))
	peerinfo = json.loads(bitcoin("getpeerinfo"))
	numPeers = len(peerinfo)
	addresses = ''
	totalBanScore = 0
	totalPingTime = 0
	numPingTimes = 0
	noResponsePings = 0
	for peer in peerinfo:
		if addresses != '':
			addresses += ' '
		try:
			addresses += peer["addr"]
			totalBanScore += peer["banscore"]
		except:
			pass
		try:
			totalPingTime += peer["pingtime"]
			numPingTimes += 1
		except:
			noResponsePings += 1


	if numPingTimes != 0:
		avgPingTime = totalPingTime / numPingTimes
	else:
		avgPingTime = "N/A"
	line += str(numPeers) + ","
	line += str(noResponsePings) + ","
	line += str(avgPingTime) + ","
	line += str(totalBanScore) + ","
	line += addresses + ","

	line += str(messages["CLOCKS PER SECOND"]) + ","
	line += parseMessage(messages["VERSION"]) + ","
	line += parseMessage(messages["VERACK"]) + ","
	line += parseMessage(messages["ADDR"]) + ","
	line += parseMessage(messages["INV"]) + ","
	line += parseMessage(messages["GETDATA"]) + ","
	line += parseMessage(messages["MERKLEBLOCK"]) + ","
	line += parseMessage(messages["GETBLOCKS"]) + ","
	line += parseMessage(messages["GETHEADERS"]) + ","
	line += parseMessage(messages["TX"]) + ","
	line += parseMessage(messages["HEADERS"]) + ","
	line += parseMessage(messages["BLOCK"]) + ","
	line += parseMessage(messages["GETADDR"]) + ","
	line += parseMessage(messages["MEMPOOL"]) + ","
	line += parseMessage(messages["PING"]) + ","
	line += parseMessage(messages["PONG"]) + ","
	line += parseMessage(messages["NOTFOUND"]) + ","
	line += parseMessage(messages["FILTERLOAD"]) + ","
	line += parseMessage(messages["FILTERADD"]) + ","
	line += parseMessage(messages["FILTERCLEAR"]) + ","
	line += parseMessage(messages["SENDHEADERS"]) + ","
	line += parseMessage(messages["FEEFILTER"]) + ","
	line += parseMessage(messages["SENDCMPCT"]) + ","
	line += parseMessage(messages["CMPCTBLOCK"]) + ","
	line += parseMessage(messages["GETBLOCKTXN"]) + ","
	line += parseMessage(messages["BLOCKTXN"]) + ","
	line += parseMessage(messages["REJECT"]) + ","
	line += parseMessage(messages["[UNDOCUMENTED]"]) + ","
	return line

def log(file, targetDateTime, count = 1):
	file.write(fetch() + "\n")
	print("Line " + str(count))
	file.flush()
	#if count >= 3600:
	#	file.close()
	#	return
	count += 1
	targetDateTime = targetDateTime + datetime.timedelta(seconds = numSecondsPerSample)
	delay = getDelay(targetDateTime)
	Timer(delay, log, [file, targetDateTime, count]).start()

def getDelay(time):
	return (time - datetime.datetime.now()).total_seconds()

time = input("Enter what time it should begin (example: \"2:45pm\", \"\" for right now): ")
file = open(os.path.expanduser("~/Desktop/GetMsgInfoLog.csv"), "w+")

if time == "":
	targetDateTime = datetime.datetime.now()
	delay = 0
else:
	targetDateTime = datetime.datetime.strptime(datetime.datetime.now().strftime('%d-%m-%Y') + " " + time, '%d-%m-%Y %I:%M%p')
	delay = getDelay(targetDateTime)

file.write(fetchHeader() + "\n")
Timer(delay, log, [file, targetDateTime, 1]).start()

if(delay > 60):
	print("Time left: " + str(delay / 60) + " minutes.")
else:
	print("Time left: " + str(delay) + " seconds.")