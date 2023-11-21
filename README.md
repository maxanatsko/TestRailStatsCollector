# TestRail Stats Collector

This repository contains a set of Python scripts designed to collect and process data from TestRail, an automated testing platform. The scripts fetch various types of data such as users, projects, statuses, and more, and save them into JSON files. Additionally, it supports sending notifications through Telegram and logging.

## Features

- Fetch data from TestRail API.
- Write data to JSON files.
- Send updates via Telegram.
- Logging of operations and errors.

## Setup

### Requirements

- Python 3.x
- `requests` library
- `telegram` library (for Telegram notifications)

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/TestRail-Stats-Collector.git
cd TestRail-Stats-Collector
```
Install the required Python packages:
```python
pip install -r requirements.txt
```


## Configuration
Create a `config.ini` file in the root directory with the following structure:
```ini
[Dev]
log_level = INFO

[Results]
directory_path = /path/to/your/directory

[Auth]
username = your_username
api_key = your_api_key

[Server]
testrail_url = http://your.testrail.url/

[Telegram]
bot_token = your_telegram_bot_token
chat_id = your_chat_id

[TestRail Filters]
project_name = Your Project Name
```
Fill in the details according to your environment and credentials.

## Usage
Run the main script:
```python
python trap_requests.py
```

Optional command-line arguments:
`-l` or `--log`: Set the logging level (e.g., INFO, WARN, DEBUG).
