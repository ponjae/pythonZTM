import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Pontus Jaensson'
email['to'] = 'ponjae11@gmail.com'
email['subject'] = 'You won 100,000,000$!'
email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('punnej@gmail.com', '****')  # Password goes here later
    smtp.send_message(email)
    print('All good boss!')
