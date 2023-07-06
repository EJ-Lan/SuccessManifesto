import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Myself'
email['to'] = 'dummy152146@gmail.com' # Dummy Email
email['subject'] = 'Success Manifesto'

email.set_content('test text')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummy152146@gmail.com', 'orcldiftzpkdkocu')
    smtp.send_message(email)