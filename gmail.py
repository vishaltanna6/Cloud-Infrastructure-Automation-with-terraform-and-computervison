import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

filename = "img.jpg"

fromaddr = "vishal.test.bot@gmail.com"
toaddr = "vishaltanna6@gmail.com"


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ALERT! ALERT! ALERT!"

body = "Trespassers Detected !"

msg.attach(MIMEText(body, 'plain'))

attachment = open("img.jpg", "rb")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())


encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "logout121")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
