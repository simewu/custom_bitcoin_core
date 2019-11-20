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
	line += "# VERSION Diff,"
	line += "VERSION ClksSum Diff,"
	line += "VERSION ClksAvg Diff,"
	line += "VERSION ClksAvg,"
	line += "VERSION ClksMax,"
	line += "VERSION BytsSum Diff,"
	line += "VERSION BytsAvg Diff,"
	line += "VERSION BytsAvg,"
	line += "VERSION BytsMax,"
	line += "# VERACK,"
	line += "# VERACK Diff,"
	line += "VERACK ClksSum Diff,"
	line += "VERACK ClksAvg Diff,"
	line += "VERACK ClksAvg,"
	line += "VERACK ClksMax,"
	line += "VERACK BytsSum Diff,"
	line += "VERACK BytsAvg Diff,"
	line += "VERACK BytsAvg,"
	line += "VERACK BytsMax,"
	line += "# ADDR,"
	line += "# ADDR Diff,"
	line += "ADDR ClksSum Diff,"
	line += "ADDR ClksAvg Diff,"
	line += "ADDR ClksAvg,"
	line += "ADDR ClksMax,"
	line += "ADDR BytsSum Diff,"
	line += "ADDR BytsAvg Diff,"
	line += "ADDR BytsAvg,"
	line += "ADDR BytsMax,"
	line += "# INV,"
	line += "# INV Diff,"
	line += "INV ClksSum Diff,"
	line += "INV ClksAvg Diff,"
	line += "INV ClksAvg,"
	line += "INV ClksMax,"
	line += "INV BytsSum Diff,"
	line += "INV BytsAvg Diff,"
	line += "INV BytsAvg,"
	line += "INV BytsMax,"
	line += "# GETDATA,"
	line += "# GETDATA Diff,"
	line += "GETDATA ClksSum Diff,"
	line += "GETDATA ClksAvg Diff,"
	line += "GETDATA ClksAvg,"
	line += "GETDATA ClksMax,"
	line += "GETDATA BytsSum Diff,"
	line += "GETDATA BytsAvg Diff,"
	line += "GETDATA BytsAvg,"
	line += "GETDATA BytsMax,"
	line += "# MERKLEBLOCK,"
	line += "# MERKLEBLOCK Diff,"
	line += "MERKLEBLOCK ClksSum Diff,"
	line += "MERKLEBLOCK ClksAvg Diff,"
	line += "MERKLEBLOCK ClksAvg,"
	line += "MERKLEBLOCK ClksMax,"
	line += "MERKLEBLOCK BytsSum Diff,"
	line += "MERKLEBLOCK BytsAvg Diff,"
	line += "MERKLEBLOCK BytsAvg,"
	line += "MERKLEBLOCK BytsMax,"
	line += "# GETBLOCKS,"
	line += "# GETBLOCKS Diff,"
	line += "GETBLOCKS ClksSum Diff,"
	line += "GETBLOCKS ClksAvg Diff,"
	line += "GETBLOCKS ClksAvg,"
	line += "GETBLOCKS ClksMax,"
	line += "GETBLOCKS BytsSum Diff,"
	line += "GETBLOCKS BytsAvg Diff,"
	line += "GETBLOCKS BytsAvg,"
	line += "GETBLOCKS BytsMax,"
	line += "# GETHEADERS,"
	line += "# GETHEADERS Diff,"
	line += "GETHEADERS ClksSum Diff,"
	line += "GETHEADERS ClksAvg Diff,"
	line += "GETHEADERS ClksAvg,"
	line += "GETHEADERS ClksMax,"
	line += "GETHEADERS BytsSum Diff,"
	line += "GETHEADERS BytsAvg Diff,"
	line += "GETHEADERS BytsAvg,"
	line += "GETHEADERS BytsMax,"
	line += "# TX,"
	line += "# TX Diff,"
	line += "TX ClksSum Diff,"
	line += "TX ClksAvg Diff,"
	line += "TX ClksAvg,"
	line += "TX ClksMax,"
	line += "TX BytsSum Diff,"
	line += "TX BytsAvg Diff,"
	line += "TX BytsAvg,"
	line += "TX BytsMax,"
	line += "# HEADERS,"
	line += "# HEADERS Diff,"
	line += "HEADERS ClksSum Diff,"
	line += "HEADERS ClksAvg Diff,"
	line += "HEADERS ClksAvg,"
	line += "HEADERS ClksMax,"
	line += "HEADERS BytsSum Diff,"
	line += "HEADERS BytsAvg Diff,"
	line += "HEADERS BytsAvg,"
	line += "HEADERS BytsMax,"
	line += "# BLOCK,"
	line += "# BLOCK Diff,"
	line += "BLOCK ClksSum Diff,"
	line += "BLOCK ClksAvg Diff,"
	line += "BLOCK ClksAvg,"
	line += "BLOCK ClksMax,"
	line += "BLOCK BytsSum Diff,"
	line += "BLOCK BytsAvg Diff,"
	line += "BLOCK BytsAvg,"
	line += "BLOCK BytsMax,"
	line += "# GETADDR,"
	line += "# GETADDR Diff,"
	line += "GETADDR ClksSum Diff,"
	line += "GETADDR ClksAvg Diff,"
	line += "GETADDR ClksAvg,"
	line += "GETADDR ClksMax,"
	line += "GETADDR BytsSum Diff,"
	line += "GETADDR BytsAvg Diff,"
	line += "GETADDR BytsAvg,"
	line += "GETADDR BytsMax,"
	line += "# MEMPOOL,"
	line += "# MEMPOOL Diff,"
	line += "MEMPOOL ClksSum Diff,"
	line += "MEMPOOL ClksAvg Diff,"
	line += "MEMPOOL ClksAvg,"
	line += "MEMPOOL ClksMax,"
	line += "MEMPOOL BytsSum Diff,"
	line += "MEMPOOL BytsAvg Diff,"
	line += "MEMPOOL BytsAvg,"
	line += "MEMPOOL BytsMax,"
	line += "# PING,"
	line += "# PING Diff,"
	line += "PING ClksSum Diff,"
	line += "PING ClksAvg Diff,"
	line += "PING ClksAvg,"
	line += "PING ClksMax,"
	line += "PING BytsSum Diff,"
	line += "PING BytsAvg Diff,"
	line += "PING BytsAvg,"
	line += "PING BytsMax,"
	line += "# PONG,"
	line += "# PONG Diff,"
	line += "PONG ClksSum Diff,"
	line += "PONG ClksAvg Diff,"
	line += "PONG ClksAvg,"
	line += "PONG ClksMax,"
	line += "PONG BytsSum Diff,"
	line += "PONG BytsAvg Diff,"
	line += "PONG BytsAvg,"
	line += "PONG BytsMax,"
	line += "# NOTFOUND,"
	line += "# NOTFOUND Diff,"
	line += "NOTFOUND ClksSum Diff,"
	line += "NOTFOUND ClksAvg Diff,"
	line += "NOTFOUND ClksAvg,"
	line += "NOTFOUND ClksMax,"
	line += "NOTFOUND BytsSum Diff,"
	line += "NOTFOUND BytsAvg Diff,"
	line += "NOTFOUND BytsAvg,"
	line += "NOTFOUND BytsMax,"
	line += "# FILTERLOAD,"
	line += "# FILTERLOAD Diff,"
	line += "FILTERLOAD ClksSum Diff,"
	line += "FILTERLOAD ClksAvg Diff,"
	line += "FILTERLOAD ClksAvg,"
	line += "FILTERLOAD ClksMax,"
	line += "FILTERLOAD BytsSum Diff,"
	line += "FILTERLOAD BytsAvg Diff,"
	line += "FILTERLOAD BytsAvg,"
	line += "FILTERLOAD BytsMax,"
	line += "# FILTERADD,"
	line += "# FILTERADD Diff,"
	line += "FILTERADD ClksSum Diff,"
	line += "FILTERADD ClksAvg Diff,"
	line += "FILTERADD ClksAvg,"
	line += "FILTERADD ClksMax,"
	line += "FILTERADD BytsSum Diff,"
	line += "FILTERADD BytsAvg Diff,"
	line += "FILTERADD BytsAvg,"
	line += "FILTERADD BytsMax,"
	line += "# FILTERCLEAR,"
	line += "# FILTERCLEAR Diff,"
	line += "FILTERCLEAR ClksSum Diff,"
	line += "FILTERCLEAR ClksAvg Diff,"
	line += "FILTERCLEAR ClksAvg,"
	line += "FILTERCLEAR ClksMax,"
	line += "FILTERCLEAR BytsSum Diff,"
	line += "FILTERCLEAR BytsAvg Diff,"
	line += "FILTERCLEAR BytsAvg,"
	line += "FILTERCLEAR BytsMax,"
	line += "# SENDHEADERS,"
	line += "# SENDHEADERS Diff,"
	line += "SENDHEADERS ClksSum Diff,"
	line += "SENDHEADERS ClksAvg Diff,"
	line += "SENDHEADERS ClksAvg,"
	line += "SENDHEADERS ClksMax,"
	line += "SENDHEADERS BytsSum Diff,"
	line += "SENDHEADERS BytsAvg Diff,"
	line += "SENDHEADERS BytsAvg,"
	line += "SENDHEADERS BytsMax,"
	line += "# FEEFILTER,"
	line += "# FEEFILTER Diff,"
	line += "FEEFILTER ClksSum Diff,"
	line += "FEEFILTER ClksAvg Diff,"
	line += "FEEFILTER ClksAvg,"
	line += "FEEFILTER ClksMax,"
	line += "FEEFILTER BytsSum Diff,"
	line += "FEEFILTER BytsAvg Diff,"
	line += "FEEFILTER BytsAvg,"
	line += "FEEFILTER BytsMax,"
	line += "# SENDCMPCT,"
	line += "# SENDCMPCT Diff,"
	line += "SENDCMPCT ClksSum Diff,"
	line += "SENDCMPCT ClksAvg Diff,"
	line += "SENDCMPCT ClksAvg,"
	line += "SENDCMPCT ClksMax,"
	line += "SENDCMPCT BytsSum Diff,"
	line += "SENDCMPCT BytsAvg Diff,"
	line += "SENDCMPCT BytsAvg,"
	line += "SENDCMPCT BytsMax,"
	line += "# CMPCTBLOCK,"
	line += "# CMPCTBLOCK Diff,"
	line += "CMPCTBLOCK ClksSum Diff,"
	line += "CMPCTBLOCK ClksAvg Diff,"
	line += "CMPCTBLOCK ClksAvg,"
	line += "CMPCTBLOCK ClksMax,"
	line += "CMPCTBLOCK BytsSum Diff,"
	line += "CMPCTBLOCK BytsAvg Diff,"
	line += "CMPCTBLOCK BytsAvg,"
	line += "CMPCTBLOCK BytsMax,"
	line += "# GETBLOCKTXN,"
	line += "# GETBLOCKTXN Diff,"
	line += "GETBLOCKTXN ClksSum Diff,"
	line += "GETBLOCKTXN ClksAvg Diff,"
	line += "GETBLOCKTXN ClksAvg,"
	line += "GETBLOCKTXN ClksMax,"
	line += "GETBLOCKTXN BytsSum Diff,"
	line += "GETBLOCKTXN BytsAvg Diff,"
	line += "GETBLOCKTXN BytsAvg,"
	line += "GETBLOCKTXN BytsMax,"
	line += "# BLOCKTXN,"
	line += "# BLOCKTXN Diff,"
	line += "BLOCKTXN ClksSum Diff,"
	line += "BLOCKTXN ClksAvg Diff,"
	line += "BLOCKTXN ClksAvg,"
	line += "BLOCKTXN ClksMax,"
	line += "BLOCKTXN BytsSum Diff,"
	line += "BLOCKTXN BytsAvg Diff,"
	line += "BLOCKTXN BytsAvg,"
	line += "BLOCKTXN BytsMax,"
	line += "# REJECT,"
	line += "# REJECT Diff,"
	line += "REJECT ClksSum Diff,"
	line += "REJECT ClksAvg Diff,"
	line += "REJECT ClksAvg,"
	line += "REJECT ClksMax,"
	line += "REJECT BytsSum Diff,"
	line += "REJECT BytsAvg Diff,"
	line += "REJECT BytsAvg,"
	line += "REJECT BytsMax,"
	line += "# [UNDOCUMENTED],"
	line += "# [UNDOCUMENTED] Diff,"
	line += "[UNDOCUMENTED] ClksSum Diff,"
	line += "[UNDOCUMENTED] ClksAvg Diff,"
	line += "[UNDOCUMENTED] ClksAvg,"
	line += "[UNDOCUMENTED] ClksMax,"
	line += "[UNDOCUMENTED] BytsSum Diff,"
	line += "[UNDOCUMENTED] BytsAvg Diff,"
	line += "[UNDOCUMENTED] BytsAvg,"
	line += "[UNDOCUMENTED] BytsMax,"
	return line

prevNumMsgs = {}
prevClocksSum = {}
prevBytesSum = {}
def parseMessage(message, string):
	line = ''
	numMsgs = re.findall(r"([0-9\.]+) msgs", string)[0]
	matches = re.findall(r"\[[0-9\., ]+\]", string)
	if len(matches) != 2:
		return None
	match1 = json.loads(matches[0])
	match2 = json.loads(matches[1])

	numMsgsDiff = int(numMsgs)
	if message in prevNumMsgs:
		numMsgsDiff = int(numMsgs) - int(prevNumMsgs[message])

	clocksSumDiff = int(match1[0])
	clocksAvgDiff = clocksSumDiff
	if numMsgsDiff != 0 and message in prevClocksSum:
		clocksAvgDiff = (int(clocksSumDiff) - int(prevClocksSum[message])) / numMsgsDiff

	bytesSumDiff = int(match2[0])
	bytesAvgDiff = bytesSumDiff
	if numMsgsDiff != 0 and message in prevBytesSum:
		bytesAvgDiff = (int(bytesSumDiff) - int(prevBytesSum[message])) / numMsgsDiff

	line += str(numMsgs) + ','		# Num
	line += str(numMsgsDiff) + ','	# Num Diff

	line += str(clocksSumDiff) + ','
	line += str(clocksAvgDiff) + ','

	line += str(match1[1]) + ','	# ClksAvg
	line += str(match1[2]) + ','	# ClksMax

	line += str(bytesSumDiff) + ','
	line += str(bytesAvgDiff) + ','

	line += str(match2[0]) + ','	# BytsSum
	line += str(match2[1]) + ','	# BytsAvg
	line += str(match2[2])			# BytsMax

	line += "# VERSION,"
	line += "# VERSION Diff,"

	line += "VERSION ClksSum Diff,"
	line += "VERSION ClksAvg Diff,"
	line += "VERSION ClksAvg,"
	line += "VERSION ClksMax,"
	line += "VERSION BytsSum Diff,"
	line += "VERSION BytsAvg Diff,"
	line += "VERSION BytsAvg,"
	line += "VERSION BytsMax,"

	prevNumMsgs[message] = numMsgs
	prevClocksSum[message] = clocksSumDiff
	prevBytesSum[message] = bytesSumDiff
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
	line += parseMessage("VERSION", messages["VERSION"]) + ","
	line += parseMessage("VERACK", messages["VERACK"]) + ","
	line += parseMessage("ADDR", messages["ADDR"]) + ","
	line += parseMessage("INV", messages["INV"]) + ","
	line += parseMessage("GETDATA", messages["GETDATA"]) + ","
	line += parseMessage("MERKLEBLOCK", messages["MERKLEBLOCK"]) + ","
	line += parseMessage("GETBLOCKS", messages["GETBLOCKS"]) + ","
	line += parseMessage("GETHEADERS", messages["GETHEADERS"]) + ","
	line += parseMessage("TX", messages["TX"]) + ","
	line += parseMessage("HEADERS", messages["HEADERS"]) + ","
	line += parseMessage("BLOCK", messages["BLOCK"]) + ","
	line += parseMessage("GETADDR", messages["GETADDR"]) + ","
	line += parseMessage("MEMPOOL", messages["MEMPOOL"]) + ","
	line += parseMessage("PING", messages["PING"]) + ","
	line += parseMessage("PONG", messages["PONG"]) + ","
	line += parseMessage("NOTFOUND", messages["NOTFOUND"]) + ","
	line += parseMessage("FILTERLOAD", messages["FILTERLOAD"]) + ","
	line += parseMessage("FILTERADD", messages["FILTERADD"]) + ","
	line += parseMessage("FILTERCLEAR", messages["FILTERCLEAR"]) + ","
	line += parseMessage("SENDHEADERS", messages["SENDHEADERS"]) + ","
	line += parseMessage("FEEFILTER", messages["FEEFILTER"]) + ","
	line += parseMessage("SENDCMPCT", messages["SENDCMPCT"]) + ","
	line += parseMessage("CMPCTBLOCK", messages["CMPCTBLOCK"]) + ","
	line += parseMessage("GETBLOCKTXN", messages["GETBLOCKTXN"]) + ","
	line += parseMessage("BLOCKTXN", messages["BLOCKTXN"]) + ","
	line += parseMessage("REJECT", messages["REJECT"]) + ","
	line += parseMessage("[UNDOCUMENTED]", messages["[UNDOCUMENTED]"]) + ","
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
