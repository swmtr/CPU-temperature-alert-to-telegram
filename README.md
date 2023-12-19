# Telegram alert when your CPU reaches a certain threshold

When you run your own Linux based machine (ex: Ubuntu Mini PC or Raspberry Pi) at home and provide certain services, it might not be a bad idea to monitor it's health. One part being, the CPU temperature.

This is a simple script which will send an alert to your Telegram when the CPU rises over a certain temperature (in this example: 50 degrees Celsius)

Setup an alert sent to Telegram when your Ubuntu CPU's temperature rises over a certain threshold


## Pre-requsites

1. lm-sensors package installed (if you have Raspberry Pi, you can skip this)

We will use the lm-sensors package, which is a common tool for monitoring hardware sensor readings, including CPU temperature. To install it, run this command:

```
sudo apt-get install lm-sensors
```

2. Python Telegram library

For Raspberry Pi setup, see the end of this section.

To get the library, run this command:
```
pip install python-telegram-bot
```

For Raspberry Pi, if you try to install via pip, you will get an error. You will need to create a virtual environment first and then install the bot. Run the following commands:
```
python3 -m venv venv
source venv/bin/activate
pip install python-telegram-bot
```

3. Telegram bot (https://core.telegram.org/bots/tutorial) - this is where you will get bot token and chat id


## The script

Grab the Python script and modify your Telegram data in it + what your temperature threshold should be.

For Raspberry Pi:
- each time you want to run the .py script, you will need to activate the virtual environment
```
source venv/bin/activate
```


## Automating the notifications
  
When the script notifies you correctly of the temperature rise, the next step is to automate it. 

Run the following command to open your crontab.

```
crontab -e
```

Add the following into it.

```
30 * * * * /usr/bin/python3 /ABSOLUTE PATH TO YOUR PYTHON FILE/cpu-temp-alert.py >> /ABSOLUTE PATH TO YOUR CRONLOG FILE 2>&1
```

For Raspberry Pi:

```
30 * * * *  /home/<USERNAME>/venv/bin/python3 /ABSOLUTE PATH TO YOUR PYTHON FILE/check-pi-cpu-temp.py >> /ABSOLUTE PATH TO YOUR CRONLOG FILE  2>&1
```

Don't forget to replace the path to your python file and to the location where you want the log. 

This cron schedule will execute the specified command at the 30th minute of every hour.


# End Notes

This setup is just a hack to get notified. It is by no means perfect, but it will do the job.

If you found this guide useful, why not let it be known by [sending me a few sats](https://360swim.com/ln-donate-github) or via LN address⚡swmtr@360swim.com .
<br />
<img src="https://360swim.com/user/themes/swimquark/images/ln_git.png" width="400" />

Finally, if you are into swimming, checkout some [swimming tips](https://360swim.com/tips).






