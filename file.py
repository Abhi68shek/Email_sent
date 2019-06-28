import smtplib

gmail_user = 'Your Email ID'  
gmail_password = 'YOUR Password'

sent_from = gmail_user  
to = ['the person you want to send the email']
subject = 'Important Message'  
body = 'Nice Meeting You. \n\n- 'your name''

email_text = """ \n  
To: %s  
Subject: %s

%s
""" % ( ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #465, this is port used to make a secure connection.
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')
