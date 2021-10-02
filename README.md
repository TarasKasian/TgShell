# TgShell

Simple command prompt via chat with telegram bot.

## 1. First Steps

### Getting the source code

> $ git clone https://github.com/gvieralopez/TgShell.git

ℹ️ **Info:**| After completing this pull request you can clone from the original project: https://github.com/TarasKasian/TgShell.git
:---: | :---


### Install software dependencies

> $ pip install -r requirements.txt


## 2. Setting up

The main configuration file is `settings.py`, but it is not included by default. Simply make a copy of `settings_example.py` and rename it to `settings.py`. 

### Configuring your bot credentials

Make sure to add your bot token in the `BOT_TOKEN` variable of your `settings.py`. If you don't have a token, you can ask for one in Telegram via @BotFather.

### Configuring your user identifier

In order to allow only the desired users to access the remote computer via bot, you have to declare those users manually by 
introducing their unique telegram identifier in the list of allowed users named `ADMIN_LIST` inside the `settings.py` file. 
If you don't know how to get your telegram unique identifier, just run the bot with the default configuration once and it 
will reply with a message like:

> Insufficient Permissions (Your id: 1234567)

Then you can use that id to update the `ADMIN_LIST` inside the `settings.py` file. 


## 3. Running the script

Simply run:

> $ python main.py


⚠️ **Warning:**| Now you can send commands to your bot. But anyone, who can access your telegram account will be able to run commands on your machine. 
:---: | :---


## 4. TODO :dart:

- Logging
- Test commands on different operation systems
- Ability to get and put files
