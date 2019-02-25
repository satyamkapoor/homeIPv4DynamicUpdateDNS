import subprocess, requests, logging


API_SECRET = "XXXXXXXXXXXXXX" 

#updateDomainARecord(currentIP)


def getCurrentIP():
	p = subprocess.Popen('dig @resolver1.opendns.com ANY -4 myip.opendns.com +short', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	for line in p.stdout.readlines():
    		currentIP = line[::-1].decode('UTF-8').strip('\n')
	return currentIP

def validateAndUpdateIPLocally(currentIP):
	with open('resources/private_info.txt','r') as inputfile:
		lines = inputfile.readlines()
		if lines:
			lineCounter = 0
			for line in lines:
				lineCounter = lineCounter + 1
				print("lincCouneter")
				if lineCounter < 2:
					if currentIP == line:
						break
					else:
						fileUpdate = open("resources/private_info.txt", 'w')
						fileUpdate.write(currentIP)
						url = "https://api.digitalocean.com/v2/domains/satyamkapoor.com/records/66321298"
						headers = {'Content-Type':'application/json','Authorization': 'Bearer ' + API_SECRET}
						payload = {"data": currentIP}
						r = requests.put(url, headers=headers, json = payload)
						logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
						logging.info('Text:'+r.text+" status code "+ str(r.status_code) )
						

currentIP = getCurrentIP()
validateAndUpdateIPLocally(currentIP)

