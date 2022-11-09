import smtplib
import time
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

#change the sending email, recieving email and password
def sendEmail(message):
    mailserver = smtplib.SMTP('smtp.office365.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login('sending email here', 'sending email password here')
    mailserver.sendmail('sending email here','receiving email here',message)
    mailserver.quit()
    pass

def checkURL(site,phrase):
    print("Running")
    while True:
        try:
            url = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(url).read()
            soup = BeautifulSoup(response)

            if phrase not in soup.text:
                sendEmail('Subject:Stock Detected\n\n' + site)
                print("Stock Detected")
            else:
                print("Out of Stock")
        except Exception as e:
            print("error")
        time.sleep(30)
    pass

#the url to check
url = 'https://www.memoryexpress.com/Products/MX00122931'
#the phrase to look for (if not found it will send email)
phrase = "Out of Stock"
checkURL(url,phrase)