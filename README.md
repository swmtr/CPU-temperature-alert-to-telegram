# Telegram alert when your CPU reaches a certain threshold

When you run your own Linux based machine at home and provide certain services, it might not be a bad idea to monitor it's health. One part being, the CPU temperature.

This is a simple script which will send an alert to your Telegram when the CPU rises over a certain temperature (in this example: 50 degrees Celsius)

Setup an alert sent to Telegram when your Ubuntu CPU's temperature rises over a certain threshold


## Pre-requsites

1. lm-sensors package installed

We will use the lm-sensors package, which is a common tool for monitoring hardware sensor readings, including CPU temperature. To install it, run this command:

```
sudo apt-get install lm-sensors
```

2. Telegram bot (https://core.telegram.org/bots/tutorial) and the Python Telegram library

To get the library, run this command:
```
pip install python-telegram-bot
```


## The script

Grab the Python script and modify your Telegram data in it + what your temperature threshold should be.


## Automating the notifications
  
When the script notifies you correctly of the negative el. prices, the next step is to automate it. 

Run the following command to open your crontab.

```
crontab -e
```

Add the following into it.

```
30 * * * * /usr/bin/python3 /ABSOLUTE PATH TO YOUR PYTHON FILE/cpu-temp-alert.py >> /ABSOLUTE PATH TO YOUR CRONLOG FILE 2>&1
```

Don't forget to replace the path to your python file and to the location where you want the log. 

This cron schedule will execute the specified command at the 30th minute of every hour.


# End Notes

This setup is just a hack to get notified. It is by no means perfect, but it will do the job.

If you found this guide useful, why not let it be known by [sending me a few sats](https://360swim.com/ln-donate-github) or via LN address⚡swmtr@360swim.com .
<br />
<img src="https://360swim.com/user/themes/swimquark/images/ln_git.png" width="400" />

Finally, if you are into swimming, checkout some [swimming tips](https://360swim.com/tips).






