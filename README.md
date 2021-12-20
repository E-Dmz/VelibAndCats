# VelibAndCats
![Example](Example.png)
- **VelibAndCats** is a script that sends through Twitter Direct Message with **infos about Vélib'** docking points (*stations*) along with **a cat fact**.
- It uses the [Cat Facts API](https://catfact.ninja/), the [Velib Metropole API](https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole), the [python-twitter library](https://python-twitter.readthedocs.io) and a `cron` task running on a NAS server.
- Depending on the time (morning vs. evening):
  - in the morning the state of *home stations* is displayed first, then a *cat fact*, then the state of *day/work stations*
  - in the evening that order is reversed
- can be personnalized by adding users and their lists of stations of interest
- can be run as a scheduled task on a NAS

## Requires
* Write and read keys for @your_bot https://developer.twitter.com/en/portal/dashboard
* Python 3 with python-twitter library
* `cron` or NAS

## Installation
### 1. Clone repo
```bash
git clone https://github.com/E-Dmz/VelibAndCats.git
```
### 2. Manage your keys
Modify `keys_template.py` with your own keys and save it as `keys.py`.

### 3. Test and personnalize
- modify and test in the .ipynb (*please do change the ids*)
- update the .py script: run `jupyter nbconvert --to script VelibAndCats.ipynb`
- run `python path/to/VelibAndCats.py <username>`

### 4. Set up a CRON job / a NAS scheduled task
```bash
crontab -e
## copy the following line:
# 0 6 * * * python3 path/to/WakeUp/WakeUp.py
## Ctrl + S Ctrl + X
crontab -l
# this one is helpful to check on cron jobs:
grep CRON /var/log/syslog
```
