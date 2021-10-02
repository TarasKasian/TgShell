# TgShell

Simple command prompt via chat with telegram bot.

## Setting up

### Getting the source code

> $ git clone https://github.com/gvieralopez/TgShell.git

> **ℹ️: Info:** 
> After completing this pull request you can clone from the original project: https://github.com/TarasKasian/TgShell.git


### Install software dependencies

> $ pip install -r requirements.txt


### Configuring your bot credentials

The main configuration file is `settings.py`, but it is not included by default. Simply make a copy of `settings_example.py` and rename it to `settings.py`. 

Make sure to add your bot token in the BOT_TOKEN variables of your `settings.py`. If you don't have a token, you can ask for one in Telegram via @BotFather.


## Running the script

Simply run:

> $ python main.py


> **⚠ WARNING: Please, be careful**  
> Now you can send commands to your bot. But anyone, who can accidentally find your bot by name in telegram, will be able to run commands on your machine. 
> To prevent such vulnerability need to provide user authorization mechanism.


## TODO :dart:

- User authorization mechanism
- Logging
- Test commands on different operation systems
- Ability to get and put files
