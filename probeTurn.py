import re
import requests
import texting
import sys, getopt
from bs4 import BeautifulSoup

def checkProbation (session,email):
	matricula = session.get("https://home.uprm.edu/matricula/index.php")
	soup = BeautifulSoup(matricula.text, "html.parser")
	mtr_info = soup.find_all("div", {"class": "inf_box"})
	probation = mtr_info[1]
	if probation.find("Probation") > -1:
        	texting.sendemail(email,"You in probation fool!")
		return 1
	return 0
def checkTurn (session,email):
	matricula = session.get("https://home.uprm.edu/matricula/index.php")
    	soup = BeautifulSoup(matricula.text, "html.parser")
    	mtr_info = soup.find_all("div", {"class": "inf_box"})
	turn = mtr_info[2]
	if turn.find("was") != -1:
        	texting.sendemail(email,turn.text)
		return 1
	return 0

#url = "http://home.uprm.edu/ckstart.php"
#values = {'username': 'jaimetted.olivieri',
#        'password': 'Jaimetted123'}

#session = requests.session()
#session.post(url, data=values)
#matricula = session.get("https://home.uprm.edu/matricula/index.php")

#soup = BeautifulSoup(matricula.text, "html.parser")
#mtr_info = soup.find_all("div", {"class": "inf_box"})

#probation = mtr_info[1]
#turn = mtr_info[2]

#if probation.find("Probation") > -1:
 #       print "I will send a text"

#if turn.find("was") == -1:
 #       print "I will send a text"

#print probation
#print turn.text


