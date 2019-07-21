import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#object for MIMEMultipart
msg=MIMEMultipart() 

#path define
photo1=(r"E:\exam\flute-fingering-chart.jpg")     
photo2=(r"E:\exam\indian-vs-western-notes-correlation.jpg")
  
#open and read file 
jpg=MIMEApplication(open(photo1,'rb').read())    #here rb stands for read in binary(maybe...)
jpg.add_header('content-disposition','attachment',filename=photo1)
msg.attach(jpg)
jpg2=MIMEApplication(open(photo2,'rb').read())
jpg2.add_header('content-disposition','attachment',filename=photo2)
msg.attach(jpg2)

#connect to server
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()    #puts the connection into TLS mode
password = input("enter password")
server.login('pahuldeep100@gmail.com','%s'%password) #login
text = msg.as_string()
addr_to=input('enter the gmail address :')
server.sendmail('pahuldeep100@gmail.com',addr_to,text)  #sending mail
server.quit()

print("email send successfully")
