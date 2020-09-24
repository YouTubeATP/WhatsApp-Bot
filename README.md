# WhatsApp-Bot
This is a private WhatsApp Bot which I use to entertain friends and automate things.

Dependencies include my own version of WebWhatsAPI available at:
https://github.com/YouTubeATP/WebWhatsapp-Wrapper

## In order to let the bot run, you need to set up a few environment variables:

### `NUMBER`
Assign the phone number of the account in which you want the bot to run in, without spaces or punctuation marks to this variable. Note this is required.
For example: `NUMBER = 13151234567`

### `CLIENT_ID`
Put the Client ID of your Imgur Application here. Note this is required. It powers the function which the bot uploads the QR Code to imgur for you to scan it.

### `DETAILS`
This is just for censoring out details for the `mask` command. You don't need to set it but it may return an error.

Put all of those variables in a file called `.env` in the folder root.

## To run the bot, cd to the project directory and run `python main.py`.
