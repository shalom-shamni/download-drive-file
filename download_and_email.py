import os
import requests
import smtplib
from email.message import EmailMessage

def main():
    FILE_ID = '1JqMBUUcd3zDMbgKkbdm2s8Qj0nAcJ0fZ'
    URL = f'https://drive.google.com/uc?export=download&id={FILE_ID}'
    response = requests.get(URL)
    filename = 'drive_file.pdf'
    
    # שמירת הקובץ
    with open(filename, 'wb') as f:
        f.write(response.content)

    # שליחת מייל
    EMAIL = os.environ['EMAIL']
    APP_PASS = os.environ['APP_PASS']

    msg = EmailMessage()
    msg['Subject'] = 'הקובץ מ-Google Drive'
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg.set_content('מצורף הקובץ מהדרייב.')
    msg.add_attachment(response.content, maintype='application', subtype='pdf', filename=filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, APP_PASS)
        smtp.send_message(msg)
    print("✅ הקובץ נשלח למייל.")

if __name__ == '__main__':
    main()
