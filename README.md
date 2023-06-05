# HKU Gym Bot

## Basic Overview
A python script that can help you fill and submit the HKU gym booking form. This script can also be scheduled using cron jobs so that you do not need to fret over getting your desired gym slot `:muscle:`.

## Demonstration of Gym Bot


https://github.com/jicsontoh/HKU-Gym-Bot/assets/64951628/85c7fb8b-8808-4c41-80aa-467bbcf03960



## How to install
1. Clone this repo
```
$ git clone https://github.com/jicsontoh/HKU-Gym-Bot.git
```

2. Create and set up your env variables in a .env file
```
EMAIL=
NAME=
STUDENT_NUM=
```

## How to use
- The script runs with the following command syntax
```
$ python hku_gym_bot.py [CENTRE] [DATE] [TIMESLOT]
```
[CENTRE] can be replaced by any of the following centre abbreviations

| Abbreviation | Represents               |
|--------------|--------------------------|
| CSE          | CSE Active               |
| B-Active     | HKU B-Active             |
| SHSC         | Stanley Ho Sports Centre |


[DATE] should follow this format strictly: YYYY/MM/DD


[TIMESLOT] is based on the various centres

| Centre                   | Timeslots                                 |
|--------------------------|-------------------------------------------|
| CSE Active               | 1245-1415 <br/> 1715-1845                 |
| HKU B-Active             | 1700-1830 <br/> 1845-2015 <br/> 2030-2200 |
| Stanley Ho Sports Centre | 1745-1915 <br/> 1930-2100                 |



## Known issues
- The booking form has a reCAPTCHA element that detects bots such as Selenium (the API we're using) and this script occasionally may not work as desired.
To overcome this, you may need to use a VPN or rotate proxies.
