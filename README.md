
# Secret Santa Telegram Bot

This Telegram bot was created to facilitate the popular "Secret Santa" game with an added feature: ensuring that certain people do not draw each other, as pre-agreed by the participants. This unique functionality wasn't available in existing applications, so I decided to create a custom solution for our group of friends.

## About the Project

The "Secret Santa" game is a fun tradition where participants anonymously exchange gifts. However, our group had a specific requirement: some people couldn't be paired with certain others. Existing tools couldn't meet this need, so I developed this Telegram bot to handle the custom pairing logic while preserving the fun and surprise of the game.

## Features

- **Custom Pairing Logic:** Ensures that specified participants do not draw certain other participants.
- **Easy Setup:** Simple commands to start the game and manage participants.
- **Anonymity:** Keeps the identity of each person's Secret Santa hidden until the reveal.
- **Notification:** Automatically notifies each participant with their assigned person to gift.

## Installation

To set up and run the Secret Santa Telegram Bot, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/andriivmnd/secret-santa-bot.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd secret-santa-bot
   ```
3. **Create the configuration file**:
   - Create a `config.py` file in the root directory with the following content:
     ```python
     # config.py
     TOKEN = "your_telegram_bot_token"  # Your Telegram bot token
     ```
   - Obtain your Telegram bot token by creating a bot through [BotFather](https://t.me/botfather) on Telegram.

4. **Install dependencies**:
   - Set up a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
     ```
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the bot**:
   - Start the bot with:
     ```bash
     python bot.py
     ```
   - The bot will be active and ready to manage your Secret Santa game.

## Usage

1. **Start the Bot**:
   - Add the bot to a group chat where you want to run the Secret Santa game.
   - Use the `/start` command to initialize the game.

2. **Add Participants**:
   - Each participant should send a message to the bot to join the game.

3. **Set Pairing Restrictions**:
   - As the game organizer, you can define pairing restrictions by listing participants who should not draw each other.

4. **Assign Secret Santas**:
   - Once all participants are added, use the `/assign` command to perform the secret pairing based on the defined restrictions.

5. **Notification**:
   - The bot will privately message each participant with the name of the person they should buy a gift for.

## Notes

- **Security:** Ensure that the bot token is kept secure and not shared publicly.
- **Customization:** The bot can be customized to include additional features such as deadline reminders or wishlists.

## Future Improvements

- **Group Size Flexibility:** Handle larger groups or multiple Secret Santa events within the same bot.
- **User Interface:** Develop a more user-friendly interface, possibly with buttons and menus for easier interaction.
- **Language Support:** Add support for multiple languages to make the bot accessible to a wider audience.

## Conclusion

This Secret Santa Telegram bot was developed to address a specific need within our group of friends, making the game more enjoyable and tailored to our requirements. I hope it proves useful for your Secret Santa events as well. If you have any suggestions or questions, feel free to contact me.
