import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


def progressBar(count, total, status=''):  # graphical display of the running script
    bar_len = 6
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()  

###################################CONFIG################################
HOST = "smtp."                          # host email
SUBJECT = ""                            # message subject
FROM = ""                               # specify the exact email address from which you send

userName = ''                           # user name from your email
passWord = ''                           # password from your email
fileText = 'msg.txt'                    # the name of the text file from which the message body is taken
fileMail = 'e_mail.txt'                 # the name of the text file from which the email list is taken
###########################################################################

def openFile(nameFile):
    f = open(nameFile, 'r')
    contentFile = f.read()
    f.close()
    return contentFile

def sendMail():    
    s_email = openFile(fileMail).split() # convective string to slice
    server = smtplib.SMTP_SSL(HOST, 465)
    server.login(userName, passWord)

    total = len(s_email)
    count = 0
  
    for i in s_email:
        msg = MIMEMultipart()
        msg['From'] = FROM
        msg['Subject'] = SUBJECT
        msg['To'] = str(i)
        msg.attach(MIMEText(openFile(fileText), 'plain'))
        server.send_message(msg)
        
        count += 1
        progressBar(count, total, str(count))

    server.quit()

sendMail()
print("The script worked")