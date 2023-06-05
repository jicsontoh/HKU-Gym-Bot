# HKU Gym Bot

## Basic Overview
A python script that can help you fill and submit the HKU gym booking form. This script can also be scheduled using cron jobs so that you do not need to fret over getting your desired gym slot.

## Demonstration of how to use


https://github.com/jicsontoh/HKU-Gym-Bot/assets/64951628/419b181d-29fd-4876-913f-de4d0430a213


## How to install
1. Clone this repo
```
git clone https://github.com/jicsontoh/HKU-Gym-Bot.git
```

2. Set up your env variables in .env file
```
EMAIL=
NAME=
STUDENT_NUM=
```

## How to use
- The script runs with the following command syntax
```
python hku_gym_bot.py [CENTRE] [DATE YYYY/MM/DD] [TIMESLOT]
```


## Known issues
- The booking form has a reCAPTCHA element that detects bots such as Selenium(the API we're using) and this script may not work as desired occasionally.
