# Email_sent
This project is based on how to connect to gmail using Python standard lib and send email from it
import smtplib

gmail_user = 'Your email user'  
gmail_password = 'Your Password'

sent_from = gmail_user  
to = ['To Whom you want to send']
subject = 'Important Message'  
body = 'Nice Meeting You. \n\n- Your name'

email_text = """ \n  
To: %s  
Subject: %s

%s
""" % ( ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')
