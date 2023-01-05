from email.message import EmailMessage
from smtplib         import SMTP_SSL
import ssl

# Purpose:  Create and return a connection to an smtp server 
# In:       Username,  username for the email account which will be seding the emails
# In:       Passwords, password for the email account which will be seding the emails
# Out:      SMTP_SSL object from smtplib library
# Note:     If returned, the connection will be logged in to the account, if this fails, the function will exit 
def getConnection(username, password):
    c = ssl.create_default_context()

    s = SMTP_SSL('smtp.gmail.com', 465, context=c)
    s.set_debuglevel(0)
    try:
        s.login(username, password)
        return(s)
    except:
        print("Failed to log into email")
        exit()

# Purpose:  Compose an email to be sent to the gift giver
# In:       GiversName,     name of the gift giver for the email text body
# In:       RevieversName,  name of the gift reciever for the email text body
# Out:      EmailMessage object from the email library
def composeEmail(giversName, recieversName):
    msg = EmailMessage()
    msg['Subject'] = f'Your Secret Santa'
    msg['From'] = "Santa"
    msg.set_content(f'Hello {giversName},\nYou are giving a gift to {recieversName} this year!! Keep it a secret.\n-Santa')
    return msg

# Purpose:  Send an email to each participant notifying them of who they are giving to 
# In:       Array of tuples with information on the giver and reviever [((giverName, giverEmail), recieverName), ... ]
def sendEmails(giftPairs):
    conn = getConnection(input("Enter Username: "), input("Enter Password: "))
    for giver, reciever in giftPairs:
        sendEmail(giver[1], composeEmail(giver[0], reciever), conn)
    quitServer(conn)

# Purpose:  Send an email to a recipient letting them know who they have for secret santa
# In:       Email,  Email address of the giver
# In:       Msg,    EmailMessage object from the email library
# In:       Conn,   SMTP_SSL object from smtplib library
def sendEmail(email, msg, conn):
    try:
        conn.sendmail(msg['From'], email, msg.as_string())
        print(f'Sent to {email}')
    except Exception as error:
        print (f'Unable to send e-mail: {error}')

# Purpose:  Close the connection to the server
# In:       SMTP_SSL object from smtplib library  
def quitServer(conn):
    conn.quit()
