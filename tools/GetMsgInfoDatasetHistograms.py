import os
import csv

# Generates the probability of each message type occuring

def main():
	os.system('clear')
	file = open(os.path.expanduser(f'~/Desktop/GetMsgInfoDatasetProbabilities.csv'), 'w+')
	file.write(getHeader())
	for fileName in os.listdir('GetMsgInfoDatasets'):
		if fileName.endswith(".csv"):
			file.write(parseFile(fileName, f'GetMsgInfoDatasets/{fileName}'))
	print('Successfully generated "GetMsgInfoDatasetProbabilities.csv" on the Desktop.')

def parseFile(fileName, path):
	print(f'Parsing "{fileName}"...')
	histogram = probability = {
		'VERSION': 0,
		'VERACK': 0,
		'ADDR': 0,
		'INV': 0,
		'GETDATA': 0,
		'MERKLEBLOCK': 0,
		'GETBLOCKS': 0,
		'GETHEADERS': 0,
		'TX': 0,
		'HEADERS': 0,
		'BLOCK': 0,
		'GETADDR': 0,
		'MEMPOOL': 0,
		'PING': 0,
		'PONG': 0,
		'NOTFOUND': 0,
		'FILTERLOAD': 0,
		'FILTERADD': 0,
		'FILTERCLEAR': 0,
		'SENDHEADERS': 0,
		'FEEFILTER': 0,
		'SENDCMPCT': 0,
		'CMPCTBLOCK': 0,
		'GETBLOCKTXN': 0,
		'BLOCKTXN': 0,
		'REJECT': 0,
	}
	with open(path) as file:
		reader = csv.reader(file, delimiter=',')
		lineCount = 0
		for row in reader:
			if lineCount != 0: # Skip the header
				histogram['VERSION'] += max(0, int(row[4]))
				histogram['VERACK'] += max(0, int(row[14]))
				histogram['ADDR'] += max(0, int(row[24]))
				histogram['INV'] += max(0, int(row[34]))
				histogram['GETDATA'] += max(0, int(row[44]))
				histogram['MERKLEBLOCK'] += max(0, int(row[54]))
				histogram['GETBLOCKS'] += max(0, int(row[64]))
				histogram['GETHEADERS'] += max(0, int(row[74]))
				histogram['TX'] += max(0, int(row[84]))
				histogram['HEADERS'] += max(0, int(row[94]))
				histogram['BLOCK'] += max(0, int(row[104]))
				histogram['GETADDR'] += max(0, int(row[114]))
				histogram['MEMPOOL'] += max(0, int(row[124]))
				histogram['PING'] += max(0, int(row[134]))
				histogram['PONG'] += max(0, int(row[144]))
				histogram['NOTFOUND'] += max(0, int(row[154]))
				histogram['FILTERLOAD'] += max(0, int(row[164]))
				histogram['FILTERADD'] += max(0, int(row[174]))
				histogram['FILTERCLEAR'] += max(0, int(row[184]))
				histogram['SENDHEADERS'] += max(0, int(row[194]))
				histogram['FEEFILTER'] += max(0, int(row[204]))
				histogram['SENDCMPCT'] += max(0, int(row[214]))
				histogram['CMPCTBLOCK'] += max(0, int(row[224]))
				histogram['GETBLOCKTXN'] += max(0, int(row[234]))
				histogram['BLOCKTXN'] += max(0, int(row[244]))
				histogram['REJECT'] += max(0, int(row[254]))

				
			lineCount += 1
	totalMessages = 0
	for messageType in histogram:
		totalMessages += histogram[messageType]

	line = ''
	line += fileName + ','
	line += str(lineCount) + ','
	for messageType in histogram:
		line += '"' + str(histogram[messageType] / totalMessages) + '",'
	line += str(totalMessages) + ','
	for messageType in histogram:
		line += '"' + str(histogram[messageType]) + '",'
	line += '\n'
	return line

def getHeader():
	line = ''
	line += '"File name",'
	line += '"Num rows",'
	line += '"P(VERSION)",'
	line += '"P(VERACK)",'
	line += '"P(ADDR)",'
	line += '"P(INV)",'
	line += '"P(GETDATA)",'
	line += '"P(MERKLEBLOCK)",'
	line += '"P(GETBLOCKS)",'
	line += '"P(GETHEADERS)",'
	line += '"P(TX)",'
	line += '"P(HEADERS)",'
	line += '"P(BLOCK)",'
	line += '"P(GETADDR)",'
	line += '"P(MEMPOOL)",'
	line += '"P(PING)",'
	line += '"P(PONG)",'
	line += '"P(NOTFOUND)",'
	line += '"P(FILTERLOAD)",'
	line += '"P(FILTERADD)",'
	line += '"P(FILTERCLEAR)",'
	line += '"P(SENDHEADERS)",'
	line += '"P(FEEFILTER)",'
	line += '"P(SENDCMPCT)",'
	line += '"P(CMPCTBLOCK)",'
	line += '"P(GETBLOCKTXN)",'
	line += '"P(BLOCKTXN)",'
	line += '"P(REJECT)",'
	line += '"Total num messages",'
	line += '"Num VERSION",'
	line += '"Num VERACK",'
	line += '"Num ADDR",'
	line += '"Num INV",'
	line += '"Num GETDATA",'
	line += '"Num MERKLEBLOCK",'
	line += '"Num GETBLOCKS",'
	line += '"Num GETHEADERS",'
	line += '"Num TX",'
	line += '"Num HEADERS",'
	line += '"Num BLOCK",'
	line += '"Num GETADDR",'
	line += '"Num MEMPOOL",'
	line += '"Num PING",'
	line += '"Num PONG",'
	line += '"Num NOTFOUND",'
	line += '"Num FILTERLOAD",'
	line += '"Num FILTERADD",'
	line += '"Num FILTERCLEAR",'
	line += '"Num SENDHEADERS",'
	line += '"Num FEEFILTER",'
	line += '"Num SENDCMPCT",'
	line += '"Num CMPCTBLOCK",'
	line += '"Num GETBLOCKTXN",'
	line += '"Num BLOCKTXN",'
	line += '"Num REJECT",'
	line += '\n'
	return line

main()