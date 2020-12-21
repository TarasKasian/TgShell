# TgShell
Simple command line via chat with telegram bot.

### How to run

- Replace 'bot_api_token' placeholder in main.py file with your telegram bot api token.
- Install dependencies:

  `$ pip install pyTelegramBotAPI`

  `$ pip install pyautogui`

- Run main.py with python interpreter version 3.8 or higher:

  `$ python main.py`

- Now you can send commands to your bot.

### :exclamation: Be careful :exclamation:
Anyone, who can accidentally find your bot by name in telegram, will be able to run commands on your machine. 
To prevent such vulnerability need to provide user authorization mechanism.

### TODO :dart:

- User authorization mechanism
- Logging
- Test commands on different operation systems
- Ability to get and put files
