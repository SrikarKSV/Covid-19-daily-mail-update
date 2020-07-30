from flask import Flask
from stats_extractor import get_all_cases
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Formatted_text.formatted_html import html_format
from Formatted_text.plaintext import plain_text

app = Flask(__name__)

# Getting the login detils
with open('./login_details.txt') as f:
    email, password = f.read().split()
    print(email, password)

# Getting the list of recivers emails
emails = []
with open("./Formatted_text/email_list.txt", newline='\n') as f:
    for x in f:
        emails.append(x)


msg = MIMEMultipart('alternative')
msg['Subject'] = 'Daily updates of the Covid-19 cases'
msg["From"] = f'Covid-19 stats <{email}>'
msg['To'] = ", ".join(emails)


@app.route('/', methods=["GET", "POST"])
def home():
    # Links of the API
    daily_cases_url = 'https://api.covid19india.org/data.json'
    india_all_cases = 'http://covid-19india-api.herokuapp.com/all'
    golabl_cases_url = 'http://covid-19india-api.herokuapp.com/global'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as stmp:
        try:
            # Getting the data from the API
            cases_data = get_all_cases(
                daily_cases_url, india_all_cases, golabl_cases_url)
        except Exception as e:
            return f"Alert:{e}"

        # Formatting the data into plain text
        text = plain_text(cases_data)
        txt_part = MIMEText(text, 'plain')
        msg.attach(txt_part)

        # Formatting the data into html
        html = html_format(cases_data)
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

        # Logging in
        stmp.login(email, password)

        stmp.send_message(msg)

    return "<h1 style='font-style:italic;color: #3e474b; text-align:center;'>Done<h1>"
