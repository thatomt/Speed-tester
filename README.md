# Speed-Tester

A simple and efficient command-line tool to measure your internet connection speed using Python.

## Overview

Speed-Tester is a Python-based CLI application that checks your internet connection performance by measuring:

- Download speed
- Upload speed
- Ping (latency)

It runs directly from the terminal and provides quick, readable results.

## Features

- Measures download speed in Mbps
- Measures upload speed in Mbps
- Displays network latency (ping)
- Selects the best available test server
- Simple terminal-based output
- Fast execution with minimal setup

## Requirements

- Python 3
- An active internet connection
- `speedtest-cli` Python package

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/thatomt/Speed-Tester.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Speed-Tester
   ```

3. Install the required package:

   ```bash
   pip install speedtest-cli
   ```

## Usage

Run the application from your terminal:

```bash
python internet_speed_tester.py
```

## Testing

The project includes a test file for checking the application's functionality.

Run the tests using:

```bash
python -m unittest test_internet_speed_tester.py
```

The application will test your internet connection and display your download speed, upload speed and ping.

## Example Output

```text
Testing speed...

Download: 45.67 Mbps
Upload: 12.34 Mbps
Ping: 18.5 ms

Test Completed!
```

*Note: The values above are examples. Actual results depend on your internet connection.*

## Project Structure

```text
Speed-Tester/
│
├── internet_speed_tester.py
├── test_internet_speed_tester.py
└── README.md
```
