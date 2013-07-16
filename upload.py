#
# This script will upload an email into an imap inbox.
# It will build the email from the email.html and plain.txt files into a single multi-part message.
# Make sure your imap host, username and password.
#

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import time

# config section : set your imap user, password and host here
user = "insert-your-user-here"
password = "insert-your-password-here"
host = "insert-your-host-here"

# Suggested Hosts:
# Gmail: imap.gmail.com
# Yahoo:  imap.mail.yahoo.com
# Aol: imap.aol.com

# optionally, you could point these to some other files on your computer
html_file = "email.html"
plain_file = "plain.txt"

# build up the message object
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Html email sample subject'
msg['From'] = user
msg['To'] = user

# set the plain text and html parts
plain = ""
html = ""

with open(html_file,"r") as f_html:
	html = f_html.read()
f_html.closed

with open(plain_file,"r") as f_plain:
	plain = f_plain.read()
f_plain.closed

msg.attach(MIMEText(plain, 'plain'))
msg.attach(MIMEText(html, 'html'))


# connect to imap & upload message
server = imaplib.IMAP4_SSL(host)
server.login(user,password)
server.select("Inbox")
server.append("Inbox","",imaplib.Time2Internaldate(time.time()),msg.as_string())
server.logout()

print "uploaded email"
