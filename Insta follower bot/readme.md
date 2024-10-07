
### README

# Instagram Follower Bot

This project is an Instagram bot that helps you automatically follow followers of a specified Instagram account using Selenium. It can be used to gain followers by targeting accounts with similar content.

## Features

- Automatically logs into your Instagram account.
- Navigates to the target account and retrieves the list of followers.
- Follows the retrieved followers of the specified account.

## Prerequisites

1. **Python 3.x** installed on your system.
2. **Google Chrome** browser installed.
3. **ChromeDriver** that matches your Chrome browser version. You can download it [here](https://sites.google.com/chromium.org/driver/).
4. Install the required Python packages:

   
    pip install selenium
   

## Setup

1. Clone or download the repository.
2. Open the `main.py` file and set your Instagram credentials and target account:

    ```python
    SIMILAR_ACCOUNT = "target_account"
    USERNAME = "your_username"
    PASSWORD = "your_password"
    ```

3. Save your changes.

## How to Run

Execute the `main.py` file:


python main.py


The bot will open a new Chrome window, log into your Instagram account, and start following users from the specified target account.

## Important Notes

- Instagram may detect automation activities, which could result in a temporary or permanent account suspension. Use this bot responsibly.
- Update the CSS selectors and XPaths in the code as Instagram's UI and structure may change over time.
- This bot is intended for educational purposes only.

## License

This project is licensed under the MIT License.
