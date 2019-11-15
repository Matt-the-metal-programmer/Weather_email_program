

def Send_email(data):
    import smtplib
    import time
    import datetime

    today = datetime.date.today()
    today = datetime.date.today()
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo()
    email.starttls()
    email.login("matwjunk@gmail.com","qcwcwivnoltergry")
    message = "Subject: Weather for "+ str(today) + "\n\n" + "Good morning:\nHere is your weather for today: \n" + data + "\n Have a great day!!!"

    email.sendmail("matwjunk@gmail.com","matwoodson@gmail.com",message)
    time.sleep(.5)
    email.quit()
