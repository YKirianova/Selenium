
# LinkedIn Job Application 

This script automates job applications on LinkedIn using the `selenium` package. It is designed to handle basic job applications that do not require additional fields or questions beyond contact information. Use this script responsibly and understand LinkedIn’s policies and terms of use before using automation tools.

## Prerequisites

Before using this script, make sure you have the following:

1. **Python 3.x** installed on your machine.
2. **Google Chrome** and the appropriate version of the `chromedriver` installed and accessible in your PATH. You can download `chromedriver` [here](https://sites.google.com/chromium.org/driver/).
3. Required Python packages installed:
    - `selenium`
  
    You can install `selenium` using:

    pip install selenium

## Setup

1. Clone the repository or copy the code into your Python environment.

2. Open the script and replace the following placeholder variables with your personal details:

    ```python
    ACCOUNT_EMAIL = YOUR_EMAIL
    ACCOUNT_PASSWORD = YOUR_PASSWORD
    PHONE = YOUR_PHONE_NUMBER
    ```

   - `YOUR_EMAIL`: Replace with your LinkedIn account email.
   - `YOUR_PASSWORD`: Replace with your LinkedIn account password.
   - `YOUR_PHONE_NUMBER`: Replace with your phone number for the job applications.

## How to Run

1. Launch the script in your Python environment:

    python linkedin_job_application.py

2. The script will open a new Chrome window and navigate to the LinkedIn job search page.

3. It will automatically log in using the provided credentials.

4. If a CAPTCHA is encountered, **you need to solve it manually**. The script will pause and ask you to press "Enter" once you have completed the CAPTCHA.

5. The script will iterate through job listings, attempting to apply to each one based on the pre-set information.

## Script Flow

1. **Navigate to LinkedIn Job Search**: Opens the specified job search URL.
   
2. **Login**: Automates the login process using your email and password.

3. **Job Listings**: Collects all job listings on the page.

4. **Apply for Jobs**: Clicks on each job listing and attempts to apply:
   - If the application form is simple and only asks for basic information (like phone number), the bot will fill it out and submit.
   - If the application is complex (additional fields, attachments, or questions), the bot will skip it.

5. **Completion**: Once all applications are processed, the bot will close the browser and end the session.

## Important Notes

- This script is a basic implementation and may not handle all types of LinkedIn job applications, particularly complex ones.
- LinkedIn may detect automation activities. Use this script with caution and consider the potential risks, such as account suspension.
- Always make sure your `chromedriver` version matches your Chrome browser version to avoid compatibility issues.
- Ensure that your login credentials and sensitive information are handled securely and never hard-coded in a publicly accessible environment.

## Customization

To modify the job search parameters, change the `driver.get()` URL in the script:

```python
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4039125300&f_AL=true&f_E=1%2C2&keywords=junior%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
```

- Adjust the `keywords` parameter to change the job titles you want to search for.
- Modify other URL parameters to refine your job search, such as location, experience level, or company.

## Disclaimer

This script is provided as-is, and I am not responsible for any misuse or violations of LinkedIn's terms of service. Use at your own risk.


