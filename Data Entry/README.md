# Housing Search Automation

This project is a web scraping automation script built using Python and Selenium for searching and extracting property information, specifically rental prices, from online listings.

## Features

- **Web Scraping**: Extracts property information such as address, price per month, and other details from real estate listing websites.
- **Data Cleaning**: Cleans and formats the extracted data, removing unwanted symbols and text for accurate analysis.
- **Automation**: Automates the navigation through the website and clicks on various elements to gather information efficiently.

## Requirements

- Python 3.8+
- Selenium WebDriver
- Web Browser (e.g., Google Chrome or Firefox)
- WebDriver for the chosen browser (e.g., `chromedriver` for Chrome)

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/housing-search-automation.git
   cd housing-search-automation
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download and configure the WebDriver**:
   - Download the WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)).
   - Place the WebDriver in the root directory of the project or specify the path in the script.

## Usage

1. **Update the script with your target URL**:
   Modify the `url` variable in the script to point to the real estate listing website you want to scrape.

2. **Run the script**:

   ```bash
   python housing_search.py
   ```

   The script will open the browser, navigate to the specified URL, and start extracting data.

3. **Data Cleaning**:
   The script will automatically clean the extracted prices, removing unwanted symbols such as `+` and `1bd`, and output a cleaned list of rental prices.

4. **Output**:
   The script will print the extracted data in the console and optionally save it to a CSV file for further analysis.

## Customization

- Modify the `find_element` and `find_elements` selectors to match the structure of your target website.
- Update the data cleaning section if the price formats differ or if new elements need to be extracted.

## Troubleshooting

- Ensure that the WebDriver version matches the browser version.
- If elements are not found, verify the class names or XPath expressions in the HTML structure of the target website.

## Contribution

Feel free to submit issues and pull requests if you encounter any bugs or want to enhance the functionality of this project.
