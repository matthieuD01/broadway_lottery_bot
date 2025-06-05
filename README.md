# Broadway Lottery Bot

This repository contains a simple automation script that enters the online lotteries for several Broadway shows through [Broadway Direct](https://lottery.broadwaydirect.com/).

The bot launches Chrome, navigates to each show's lottery page and fills in the entry form using Selenium.

## Requirements

- Python 3
- Google Chrome
- [ChromeDriver](https://chromedriver.chromium.org/) (matching your Chrome version)
- Python packages listed in `requirements.txt` (see below)

## Installation

1. Clone this repository.
2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variable:

```
CHROMEDRIVER_PATH=/path/to/chromedriver
```

## Usage

Simply run:

```bash
python main.py
```

The script will open a Chrome window and submit entries for each show listed in `shows_bway_direct` in `broadway_bot.py`.

## Customization

Edit the `shows_bway_direct` dictionary in `main.py` (or `broadway_bot.py`) to change which shows are entered and how many tickets are requested. The keys are the show identifiers used by Broadway Direct and the values are the desired ticket quantities.


### requirements.txt

The required Python packages are listed below:

```
selenium
undetected-chromedriver
python-dotenv
```
