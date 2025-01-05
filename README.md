# Instagram Automation Bot

## Overview

This project automates the process of blocking and unblocking users on Instagram. Using Selenium and Python, the bot allows users to log in to their Instagram account, find a specific user, and either block or unblock them based on user input. It leverages the browser automation capabilities of Selenium to simulate user actions on Instagram.

The system is organized into several modules that each handle specific tasks, such as opening the browser, logging into Instagram, finding users, and performing block/unblock actions.

## Features

- **Browser Automation**: Opens Chrome browser and navigates to Instagram using Selenium WebDriver.
- **Instagram Login**: Automates logging into Instagram with a username and password.
- **Find User**: Searches for a specific Instagram user based on their username.
- **Block User**: Blocks a user by interacting with the Instagram interface.
- **Unblock User**: Unblocks a previously blocked user by simulating the necessary steps on Instagram.
- **Logging**: Tracks each step of the process with detailed logs for debugging and transparency.

## Requirements

- **Python 3.8+**: Make sure Python 3.8 or later is installed on your computer.
- **Selenium**: A Python library to control a web browser.
- **webdriver-manager**: A tool to automatically manage browser drivers (e.g., ChromeDriver).
- **Logging**: Python's built-in logging library for debugging.
  
Install the necessary dependencies by running:

```bash
pip install selenium webdriver-manager
```

## Running the Bot

1. Clone or download the repository.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. To use the bot, run the `manage.py` script:

   ```bash
   python manage.py
   ```

4. The bot will prompt you for your Instagram username, password, the username of the target account, and the action (either "block" or "unblock").

   - Example:
     ```bash
     Enter your Instagram username: your_username
     Enter your Instagram password: your_password
     Enter the username to find: target_username
     Enter for block or unblock operation (example: block): block
     ```

## Modules

### 1. **BrowserBot** (`browser_bot/opening_browser.py`)

   - Initializes the Chrome browser and navigates to the Instagram website.

### 2. **InstagramBot** (`instagram.instagram_login.py`)

   - Logs into Instagram using the provided credentials (username and password).

### 3. **FindUser** (`instagram.find_user.py`)

   - Searches for the Instagram profile of the specified user.

### 4. **InstagramBlocking** (`instagram.blocking_process.py`)

   - Handles the blocking process of the specified user on Instagram.

### 5. **ToUnblock** (`instagram.to_unblock.py`)

   - Handles the unblocking process of the specified user on Instagram.

### 6. **Logging** (`logging_info.logging_config.py`)

   - Configures logging for tracking all bot actions.

## Example Workflow

1. The bot opens the Chrome browser and navigates to Instagram.
2. Logs into the account using the provided credentials.
3. Searches for the specified user.
4. Depending on the user's input, either blocks or unblocks the user.

## Troubleshooting

- If you encounter issues, check the `logging_info/logging.log` file for detailed logs.
- Ensure that you have installed all the required dependencies.
- Make sure you are using a compatible version of Python and Chrome.
