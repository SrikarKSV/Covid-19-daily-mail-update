from flask import Flask
from stats_extractor import get_all_cases
import smtplib
from email.message import EmailMessage
from plaintext import plain_text
from formatted_html import html_format

app = Flask(__name__)

with open('./login_details.txt') as f:
    email, password = f.read().split()


emails = []
with open("./email_list.txt", newline='\n') as f:
    for x in f:
        emails.append(x)

msg = EmailMessage()
msg['Subject'] = 'Daily updates of the Covid-19 cases'
msg["From"] = f'Covid-19 stats <{email}>'
msg['To'] = ", ".join(emails)


def error_occured(error):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as stmp:
        msgs = EmailMessage()
        msgs['Subject'] = 'Alert📢 something wrong happened'
        msgs['From'] = f'Covid-19 stats <{email}>'
        msgs['To'] = 'srikar1awesome@gmail.com'
        msg.set_content(f"The error:{error}")
        stmp.login(email, password)
        stmp.send_message(msg)


@app.route('/', methods=["GET", "POST"])
def home():
    daily_cases_url = 'https://api.covid19india.org/data.json'
    india_all_cases = 'http://covid-19india-api.herokuapp.com/all'
    golabl_cases_url = 'http://covid-19india-api.herokuapp.com/global'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as stmp:
        try:
            cases_data = get_all_cases(
                daily_cases_url, india_all_cases, golabl_cases_url)
            text = plain_text(cases_data)
            msg.set_content(text)
            msg.add_alternative(html_format(cases_data), subtype="html")
        except Exception as e:
            error_occured(e)
            text = "We are sorry dear consumer due to some technical difficulties we are not able to deliver your updates today."
            msg.set_content(text)

        stmp.login(email, password)

        stmp.send_message(msg)

    return "<h1 style='font-style:italic;color: #3e474b; text-align:center;'>Done<h1>"


if __name__ == "__main__":
    app.run(debug=True)
