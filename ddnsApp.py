
import subprocess, requests, logging, shlex

API_SECRET = "YOUR_DIGITAL_OCEAN_API_KEY" 

def getCurrentIP():
  cmd='dig @resolver1.opendns.com ANY -4 myip.opendns.com +short'
  proc=subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE)
  out,err=proc.communicate()
  currentIPv4 = out.decode('UTF-8').strip('\n')
  return currentIPv4

def validateAndUpdateIPLocally(currentIP):
        with open('private_info.txt','r') as inputfile:
                lines = inputfile.readlines()
                if lines:
                        lineCounter = 0
                        for line in lines:
                                lineCounter = lineCounter + 1
                                if lineCounter < 2:
                                        if currentIP == line:
                                                break
                                        else:
                                                fileUpdate = open("private_info.txt", 'w')
                                                fileUpdate.write(currentIP)
                                                url = "https://api.digitalocean.com/v2/domains/satyamkapoor.com/records/66321298"
                                                headers = {'Content-Type':'application/json','Authorization': 'Bearer ' + API_SECRET}
                                                payload = {"data": currentIP}
                                                r = requests.put(url, headers=headers, json = payload)
                                                logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
                                                logging.info('Text:'+r.text+" status code "+ str(r.status_code) )


currentIP = getCurrentIP()
validateAndUpdateIPLocally(currentIP)
