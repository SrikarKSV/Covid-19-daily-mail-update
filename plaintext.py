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
