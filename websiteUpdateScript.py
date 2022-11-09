import smtplib
import time
import hashlib
from urllib.request import urlopen, Request

#change the sending email, recieving email and password
def sendEmail(message):
    mailserver = smtplib.SMTP('smtp.office365.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login('sending email here', 'sending email password here')
    mailserver.sendmail('sending email here','receiving email here',message)
    mailserver.quit()
    pass


# setting the URL you want to monitor
def checkURL(site):
    url = Request(site, headers={'User-Agent': 'Mozilla/5.0'})

    # to perform a GET request and load the
    # content of the website and store it in a var
    response = urlopen(url).read()

    # to create the initial hash
    currentHash = hashlib.sha224(response).hexdigest()
    print("running")
    time.sleep(10)
    while True:
        try:
            # perform the get request and store it in a var
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(30)

            # perform the get request
            response = urlopen(url).read()

            # create a new hash
            newHash = hashlib.sha224(response).hexdigest()

            # check if new hash is same as the previous hash
            if newHash == currentHash:
                continue

            # if something changed in the hashes
            else:
                # notify
                print("Change Detected")

                #send email
                sendEmail('Subject:Change Detected\n\n' + site)

                # again read the website
                response = urlopen(url).read()

                # create a hash
                currentHash = hashlib.sha224(response).hexdigest()

                # wait for 30 seconds
                time.sleep(30)
                continue

        # To handle exceptions
        except Exception as e:
            print("error")

#url to check
url = 'your url'
checkURL(url)