from flask import Flask
from stats_extractor import get_all_cases
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

with open('./login_details.txt') as f:
    email, password = f.read().split()

msg = EmailMessage()
msg['Subject'] = 'Daily updates of the Covid-19 cases'
msg["From"] = f'Covid-19 stats <{email}>'
msg['To'] = 'srikar1awesome@gmail.com'


def plain_text(cases_data):
    msg = f"""
    Daily updates for Covid-19 cases:
        Country: India
            Last 24 hours:
            Confirmed cases in last 24 hours:   {int(cases_data['dailyconfirmed']):,}
            Recoveries in last 24 hours:    {int(cases_data['dailyrecovered']):,}
            Deaths in last 24 hours:    {int(cases_data['dailydeceased']):,}

            Total:
            Total cases:    {int(cases_data['totalconfirmed']):,}
            Active cases:   {int(cases_data['active_cases']):,}
            Active cases rate:   {cases_data['active_rate']}
            Total recoveries:   {int(cases_data['totalrecovered']):,}
            Recovery rate:   {cases_data['recovered_rate']}
            Total deaths:   {int(cases_data['totaldeceased']):,}
            Death rate:     {cases_data['death_rate']}

            For more details visit: https://www.covid19india.org/

        Country: Global
            Total confirmed cases:   {int(cases_data['global_confirmed_cases']):,}
            
            Total active cases:     {int(cases_data['global_active_cases']):,}
            Active rate:    {cases_data['global_active_rate']}
            Total recoveries:   {int(cases_data['global_recovered_cases']):,}
            Recovery rate:   {cases_data['global_recovered_rate']}
            Total deaths:   {int(cases_data['global_death_cases']):,}
            Death rate:     {cases_data['global_death_rate']}
    """

    return msg


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
