import smtplib
import re
import getpass
# import time
# Go this url https://myaccount.google.com/apppasswords
# sankjgcwowqlgczi
# Write gmail name to find port number
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()

def emailinput():
    sender_email=input("Enter Sender Email: ")
    print(sender_email)
    if re.findall('[\w]{2,20}@[\w]{2,20}.[A-Za-z]',sender_email):
        pass
    else:
        print("Please Enter a Valid Email")
        # time.sleep(3)
        exit()
    password=getpass.getpass(prompt="Enter a Password Associted with this Email: ")
    return sender_email,password

sender_email,password=emailinput()

try:
    conn.login(sender_email,password=password)
    print("Login SuccessFull")
    reciver_email=input("Enter Reciver Email: ")
    subject=input("Enter your Subject: ")
    msg=input("Enter your Message: ")
    conn.sendmail(sender_email,reciver_email,(f"Subject: {subject} \n\n {msg}"))
    print("Email Sent Succesfully!")
    conn.quit()
except:
    print("Invalid Username or Email")