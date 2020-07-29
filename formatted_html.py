def html_format(cases_data):

    formatted = f"""<!DOCTYPE html>
<html lang="en">

    <body
        style="max-width:600px;margin:30px auto;font-size:18px;font-family:Georgia,Times,serif;color:#333333;margin-bottom:1em;">
        <div>
            <h1 style="text-align: center;margin-bottom: 3rem;font-weight:bold;text-decoration:underline;color:#4ba04e">
                Covid-19😷 Updates
            </h1>
            <h2 style="color:#222831;"> Country: India</h2>
            <div>
                <h4 style="font-size: 22px; color: #494949;">Last 24 hours⌚:</h4>
                <p><span style="color: #3e474b;">Confirmed cases in last 24
                        hours:</span> <span style="color: #3b6978;">{int(cases_data['dailyconfirmed']):,}</span>
                </p>
                <p><span style="color: #222831;">Recoveries in last 24 hours:</span><span style="color: #3b6978;">
                        {int(cases_data['dailyrecovered']):,}</span></p>
                <p><span style="color: #222831;"> Deaths in last 24 hours:</span>
                    <span style="color: #3b6978;">{int(cases_data['dailydeceased']):,}</span>
                </p>
                <br>
                <h4 style="font-size: 22px; color: #494949;">Total:</h4>
                <p> <span style="color: #222831;">Total cases:</span> <span
                        style="color: #3b6978;">{int(cases_data['totalconfirmed']):,}</span></p>
                <p> <span style="color: #222831;">Active cases:</span> <span
                        style="color: #3b6978;">{int(cases_data['active_cases']):,}</span></p>
                <p> <span style="color: #222831;">Active cases rate:</span> <span
                        style="color: #3b6978;">{cases_data['active_rate']}</span></p>
                <p> <span style="color: #222831;">Total recoveries:</span> <span
                        style="color: #3b6978;">{int(cases_data['totalrecovered']):,}</span></p>
                <p> <span style="color: #222831;">Recovery rate:</span> <span
                        style="color: #3b6978;">{cases_data['recovered_rate']}</span></p>
                <p> <span style="color: #222831;">Total deaths:</span> <span
                        style="color: #3b6978;">{int(cases_data['totaldeceased']):,}</span></p>
                <p> <span style="color: #222831;">Death rate:</span> <span
                        style="color: #3b6978;">{cases_data['death_rate']}</span></p>
            </div>
            <br>
            <p><span style="color: #222831;">For more details visit:</span> <a href="https://www.covid19india.org/"
                    target="_blank">https://www.covid19india.org/</a></p>
            <br>
            <div>
                <h2 style="color:#222831;">Country: Global</h2>
                <p style="margin-bottom: 1.7rem;">Total confirmed cases:</span><span style="color: #3b6978;">
                        {int(cases_data['global_confirmed_cases']):,}</span>
                </p>
                <p><span style="color: #222831;">Total active cases:</span>
                    <span style="color: #3b6978;">{int(cases_data['global_active_cases']):,}</span>
                </p>
                <p> <span style="color: #222831;">Active rate:</span> <span
                        style="color: #3b6978;">{cases_data['global_active_rate']}</span>
                </p>
                <p> <span style="color: #222831;">Total recoveries:</span>
                    <span style="color: #3b6978;">{int(cases_data['global_recovered_cases']):,}</span>
                </p>
                <p> <span style="color: #222831;">Recovery rate:</span>
                    <span style="color: #3b6978;">{cases_data['global_recovered_rate']}</span></p>
                <p> <span style="color: #222831;">Total deaths:</span>
                    <span style="color: #3b6978;">{int(cases_data['global_death_cases']):,}</span></p>
                <p> <span style="color: #222831;">Death rate:</span> <span
                        style="color: #3b6978;">{cases_data['global_death_rate']}</span></p>
            </div>
        </div>
    </body>

</html>"""

    return formatted
