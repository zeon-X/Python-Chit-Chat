import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Gmail credentials
gmail_user = ''
gmail_password = ''

# Email content
subject = 'Inquiry About Property Management Services for a 6-Unit Building'
body_template = '''
Dear {company_name} Team,

My name is Yesmin, and I’m in the process of closing on a 6-unit building next week. I was referred to your company by a friend in Philadelphia, and I’m interested in learning more about your property management services.

Could you please provide details on your rates and service plans?
Additionally, I have a few questions:
- Do you handle tenant screening and lease signings?
- Is there a renewal fee if the tenant stays and renews the lease?
- Do you offer in-house maintenance, or do you use external contractors?

I look forward to your response and appreciate your time.

Best regards,
Onamika Yesmin
'''

# Companies and their emails
companies = {
    "zeon management": "zeonxbd@gmail.com",
}


def send_email(company_name, recipient_email):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient_email
    msg['Subject'] = subject
    body = body_template.format(company_name=company_name)
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(gmail_user, recipient_email, text)
        server.quit()
        print(f'Email sent to {company_name}')
    except Exception as e:
        print(f'Failed to send email to {company_name}. Error: {e}')


# Loop through each company and send email
for company, email in companies.items():
    send_email(company, email)
    # time.sleep(180)
