import requests
from datetime import date


daily_cases_url = 'https://api.covid19india.org/data.json'
india_all_cases = 'http://covid-19india-api.herokuapp.com/all'
golabl_cases_url = 'http://covid-19india-api.herokuapp.com/global'


def get_all_cases(url1, url2, url3):
    # Getting cases from API 1(For cases of India)
    r = requests.get(url1)
    daily_cases = r.json()['cases_time_series']
    todays_cases = daily_cases[-1]
    cases_data = dict()
    cases_data['date'] = str(date.today())
    cases_data['dailyconfirmed'] = todays_cases['dailyconfirmed']
    cases_data['dailydeceased'] = todays_cases['dailydeceased']
    cases_data['dailyrecovered'] = todays_cases['dailyrecovered']
    cases_data['totalconfirmed'] = todays_cases['totalconfirmed']
    cases_data['totaldeceased'] = todays_cases['totaldeceased']
    cases_data['totalrecovered'] = todays_cases['totalrecovered']

    # Getting cases from API 2(For information of the cases)
    r = requests.get(url2)
    daily_cases_second = r.json()
    india_all_case = daily_cases_second[0]
    cases_data['active_cases'] = india_all_case['active_cases']
    cases_data['active_rate'] = str(india_all_case['active_rate'])+"%"
    cases_data['death_rate'] = str(india_all_case['death_rate'])+"%"
    cases_data['recovered_rate'] = str(india_all_case['recovered_rate'])+"%"

    # Getting global cases from API 3
    r = requests.get(url3)
    global_case = r.json()
    global_data = global_case['data']
    cases_data['global_confirmed_cases'] = global_data['confirmed_cases']
    cases_data['global_active_cases'] = global_data['active_cases']
    cases_data['global_active_rate'] = global_data['active_rate']
    cases_data['global_recovered_cases'] = global_data['recovered_cases']
    cases_data['global_recovered_rate'] = global_data['recovered_rate']
    cases_data['global_death_cases'] = global_data['death_cases']
    cases_data['global_death_rate'] = global_data['death_rate']

    return cases_data


if __name__ == "__main__":
    print(get_all_cases(daily_cases_url, india_all_cases, golabl_cases_url))
