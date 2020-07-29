from flask import Flask
from stats_extractor import get_all_cases
import smtplib
from email.message import EmailMessage
from plaintext import plain_text

app = Flask(__name__)

with open('./login_details.txt') as f:
    email, password = f.read().split()

msg = EmailMessage()
msg['Subject'] = 'Daily updates of the Covid-19 cases'
msg["From"] = f'Covid-19 stats <{email}>'
msg['To'] = 'srikar1awesome@gmail.com'


@app.route('/')
def home():
    daily_cases_url = 'https://api.covid19india.org/data.json'
    india_all_cases = 'http://covid-19india-api.herokuapp.com/all'
    golabl_cases_url = 'http://covid-19india-api.herokuapp.com/global'

    cases_data = get_all_cases(
        daily_cases_url, india_all_cases, golabl_cases_url)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as stmp:
        text = plain_text(cases_data)
        msg.set_content(text)
        stmp.login(email, password)

        stmp.send_message(msg)

    return "<h1>Done<h1>"


if __name__ == "__main__":
    app.run(debug=True)
