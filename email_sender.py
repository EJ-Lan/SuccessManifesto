import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import datetime


# Check if it's time to send the yearly email
def should_send_yearly_email():
    # Replace 'yyyy-mm-dd' with the date of the last email sent
    last_email_date = datetime.date.fromisoformat('2020-01-01')
    current_date = datetime.date.today()
    # Set the interval for yearly emails (365 days)
    interval = datetime.timedelta(days=365)
    return current_date >= last_email_date + interval


# Send the yearly email
def send_yearly_email():
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Myself'
    email['to'] = 'dummy152146@gmail.com'  # Dummy Email
    email['subject'] = 'Success Manifesto'

    email.set_content(html.substitute({'name': 'Your Name'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('dummy152146@gmail.com', 'orcldiftzpkdkocu')
        smtp.send_message(email)


# Check if it's time to send the yearly email
if should_send_yearly_email():
    send_yearly_email()
