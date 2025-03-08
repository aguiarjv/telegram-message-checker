# Telegram Message Checker

The idea of this project is to check the messages you are receiving on Telegram from any source and forward some specific messages to yourself. It is very useful when you have a lot groups and you
don't have time to check all the messages but you want to filter some of them in real time.

## Prerequisites

- Python 3.8+
- Git
- Virtualenv
- Docker

## Installation and Usage

### Steps

1. Create Telegram API ID and Hash

   - Go to the [Telegram Website](https://my.telegram.org/auth) and enter the phone number you are going to use.

   - Click under API Development tools.

   - Fill in your application details. There is no need to enter any URL.

   - Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!

   - Save your API ID and Hash.

2. Create a bot using BotFather and save your Bot Token. There is a [tutorial here](https://core.telegram.org/bots/tutorial).

3. Clone this repository:

   ```bash
   git clone https://github.com/aguiarjv/telegram-message-checker
   ```

4. Create a .env file with the following fields:

   ```
   TELEGRAM_API_ID=
   TELEGRAM_API_HASH=
   TELEGRAM_BOT_TOKEN=
   SEARCH_WORDS=
   ```

5. Update the fields in your .env file. The "SEARCH_WORDS" field is where you put the different words or terms that you wish to check for. These terms should be comma (,) separated.

6. Build the project using Docker:

   ```bash
   docker compose build
   ```

7. Run the app and you will be prompted to enter your phone number. Then you have to enter a code that you will receive from Telegram. After that a .session file will be created.

   ```bash
   docker compose run app
   ```

8. After the session file is created you can shutdown this container and set up a new one:

   ```bash
   docker compose up -d
   ```
