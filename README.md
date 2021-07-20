# WakeUp
WakeUp is a Twitter bot that greets your followers and indicates the date and local hour in Paris.

Please visit https://twitter.com/E_Dmz_Bot and https://twitter.com/E_Dmz for more.

## Prequisites
* Having write and read keys for @your_bot https://developer.twitter.com/en/portal/dashboard 

* Python 3 with python-twitter library 

* CRON (i'm running it on Ubuntu 20)

## Installation
### 1. Clone repo
```bash 
git clone https://github.com/E-Dmz/WakeUp.git
```
### 2. Manage your keys
Modify `keys_template.py` with your own keys and save as `keys.py`.

### 3. Set up a CRON job
```bash
crontab -e
# copy the following line: 
# 0 6 * * * /path/to/python3 /absolute/path/to/WakeUp/WakeUp.py
# Ctrl + S Ctrl + X
crontab -l
# this one is helpful to check on cron jobs: 
grep CRON /var/log/syslog
```

