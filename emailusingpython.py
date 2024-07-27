import smtplib as s #importing smtplib module

#import server and port number of gmail
ob = s.SMTP('smtp.gmail.com',587) #import server and port number of gmail
# connecting to servers
ob.ehlo()
ob.starttls()

#login to SMTP server with parameters of sender's gmail account and the App password created
#for example:
ob.login('sender@gmail.com', 'password generated') 

#mention the subject and body of the message you want to send
subject = "Testing mail via python"
body = "The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon."

#It will specify the format of the message that needs to be send through the mail
message = "subject:{}\n\n{}".format(subject, body)

#add the list of gmail accounts to whom you want to send the particular message via mail
#for example :
listAdd = ["receiver1@gmail.com", "receiver2@gmail.com", "receiver3@gmail.com"]

#sendmail() takes three parameters: sender email, list of receivers, message
ob.sendmail("sender@gmail.com",listAdd,message)

#display the message in the terminal for the successfull execution of the program
print("Send Successfully")
#disconnecting from the SMTP server to release resources and terminate the session cleanly
ob.quit()