# Covid-19 daily stats report
The program will send a mail to a list of recievers when the url of the hosted program is requested.

### Package requirement:
* Flask
* Requests

## The mail consists of:
### Country: India
1) Last 24 hours
    * Confirmed cases
    * Recoveries
    * Deaths
2) Summary
    * Total cases
    * Active cases
    * Active cases rate
    * Total recoveries
    * Recovery rate
    * Total deaths
    * Death rate
### Country: Global
1) Total confirmed cases: 17,189,755
2) Total active cases: 5,818,358
3) Active rate: 33.85%
4) Total recoveries: 670,256
5) Recovery rate: 3.9%
6) Total deaths: 10,701,141
7) Death rate: 62.25%

## How it works?
1) Put the list of recievers mail-id in `Formatted/email_list.txt`.
2) Enter the login details of the sender in `./login_details.txt`.
3) Host the website either locally (for testing) or on a server.
4) Hit the url of the hosted program using cron daily.

# Sample picture of the mail
![A screenshot of the mail](https://i.imgur.com/1NkwYxK.png)