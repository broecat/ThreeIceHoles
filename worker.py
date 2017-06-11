import probeTurn
import texting
import grades
import requests
import json
import urllib
from time import sleep

while True:
    
    users = requests.get('http://localhost:56951/ApiUrlThatPythonUses/Users?token=TkSWDXfF0jrcXv9ai0aB')
    #users = urllib.urlopen('http://localhost:56951/ApiUrlThatPythonUses/Users?token=TkSWDXfF0jrcXv9ai0aB')
    temp = str(users.content).replace('\r\n','')
    temp = temp.replace('&quot;','"')
    users = json.loads(temp)
    #print users['Users']
    for i in users['Users']:
       
        oldPortal = requests.Session()
        newPortal = requests.Session()

        url = "http://home.uprm.edu/ckstart.php"
        values = {'username': i['Username']+"@upr.edu",
            'password': i['Password']}
        oldPortal.post(url, data=values)

        url = 'https://portal.upr.edu/rum/portal.php'
        values = {'username': i['Username']+"@upr.edu",
                'password': i['Password'],
                'a':'rea_login_do'}
        newPortal.post(url, data=values)

        i['Probate']=probeTurn.checkProbation(oldPortal,i['Email'])
        i['Matriculate']=probeTurn.checkTurn(oldPortal,i['Email'])
        i['Grades']=grades.getgrades(newPortal,i['Email'],i['Grades'])


        headers = {'content-type': 'application/json'}


        requests.post('http://localhost:56951/ApiUrlThatPythonUses/UpdateUser',data=json.dumps(i),headers = headers)
    sleep(600)

