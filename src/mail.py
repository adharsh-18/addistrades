import smtplib
from email.message import EmailMessage
def sub(a): 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('addistradeinc@gmail.com','Jordanstockwolf99')
    server.sendmail('addistradeinc@gmail.com',a,'WELCOME TO ADDIS TRADES INCORPORATED !! \n WE WELCOME YOU TO JOIN THE HOTTEST AND MOST SAFEST STOCK BROKERAGE PLATFORM IN THE WORLD \n ADDIS TRADES INCORPORATED STRIVES TO MAKE SURE THAT YOU AS PEOPLE BE THE MOST BENIFITED \n THANK YOU \n REGARDS \n')
    server.quit()

def buy(a,b,c,d):
    msg = EmailMessage()
    msg.set_content('CONGRATULATIONS Mr/Mrs. '+a[0][1]+' ON BLOCKING '+str(d)+' STOCKS OF '+c+' THROUGH US. \n THE TOTAL BILL OF $'+b+' HAS BEEN TRANSFERRED FROM YOUR BANK ACCOUNT (ACCOUNT NO.:'+a[0][4]+') TO US. \n WE HOPE THAT YOU ARE SATISFIED WITH OUR SERVICE . \n YOUR ONLY REGRET WOULD BE NOT BUYING MORE \n THANK YOU . HAVE A NICE DAY \n REGARDS ')
    msg['Subject'] = 'STOCK HAS BEEN BLOCKED'
    msg['From'] = "addistradeinc@gmail.com"
    msg['To'] = a[0][5]
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('addistradeinc@gmail.com','Jordanstockwolf99')
    server.send_message(msg)
    server.quit()
    
def sell(a,b,c,d):
    msg = EmailMessage()
    msg.set_content('CONGRATULATIONS Mr/Mrs. '+a[0][1]+' ON SELLING '+str(d)+' STOCKS OF '+c+' THROUGH US. \n THE TOTAL BILL OF $'+str(b)+' HAS BEEN ADDED TO YOUR DEMAT WALLET (ACCOUNT NO.:'+a[0][4]+'). \n WE HOPE THAT YOU ARE SATISFIED WITH OUR SERVICE .\n THANK YOU . HAVE A NICE DAY \n REGARDS ')
    msg['Subject'] = 'STOCK SOLD'
    msg['From'] = "addistradeinc@gmail.com"
    msg['To'] = a[0][5]
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('addistradeinc@gmail.com','Jordanstockwolf99')
    server.send_message(msg)
    server.quit()
    

def password(a,b): 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('addistradeinc@gmail.com','Jordanstockwolf99')
    server.sendmail('addistradeinc@gmail.com',a[0][5],'WE HAVE PROCESSED YOUR REQUIREMENT FOR REVIVING YOUR FORGOTTEN PASSWORD. \n YOUR PASSWORD IS :\n'+str(b)+' \n THANK YOU \n REGARDS \n')
    server.quit()
