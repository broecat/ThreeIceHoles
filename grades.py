import re
import json
import texting

# s = requests.Session()
# url = 'https://portal.upr.edu/rum/portal.php'
# values = {'username': '#email#',
#           'password': '#password#',
#           'a':'rea_login_do'}
          
# r1=s.post(url, data=values)
#print(r1.text)
def getgrades(session,email,grade):
    r2 = session.get('https://portal.upr.edu/rum/students/grade/index.php')
    JSON = re.compile('var ui_table_def_([a-zA-Z0-9]*) = ({.*?});', re.DOTALL)
    matches = JSON.search(r2.text)
    #print(matches.group(2))

    d = json.loads(matches.group(2))
    count =0
    msg = ""
    for i in d['items']:
        msg = msg + i['course_code'].replace("&nbsp;","")+" "+i['grade']+"\n"
        if(i['grade'].isalpha()):
            count=count+1
        #print(i['course_code'].replace("&nbsp;","")+" "+i['grade'])
    if(count!=grade):
        texting.sendemail(email,msg)
    return count