import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# smtp_server =
# smtp_port =
# email_address =
# password =
# to =

wiadomosc = MIMEMultipart()
wiadomosc['From'] = email_address
wiadomosc["To"] = to
wiadomosc['Subject'] = "Dodatkowe życzenia"

tresc = "Wszystkiego najlepszego z okazji urodzin!"
wiadomosc.attach(MIMEText(tresc, 'plain'))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, password)
        server.sendmail(email_address, to, wiadomosc.as_string())
        print("E-mail został wysłany")
except Exception as e:
    print(f"Bład: {e}")