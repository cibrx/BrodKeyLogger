# BrodKeyLogger
# Keylogger with Data Encryption and Broadcasting

This is a Python keylogger that captures keystrokes, saves them locally, encrypts the data, and broadcasts it over the network. It consists of two parts: `keylogger.py` for capturing keystrokes and `listen.py` for receiving and decrypting the data.

## Features

- Captures keyboard input, including special keys.
- Stores keystrokes in files organized by date and time.
- Encrypts the captured data for security.
- Broadcasts the encrypted data over the network.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Required Python packages installed. You can install them using `pip`:

    ```bash
    pip install pynput cryptography
    ```

## Usage

1. Run `keylogger.py` to start capturing keystrokes.

   ```bash
   python keylogger.py
The keystrokes will be saved in the saved/ directory.

Run listen.py on a target machine to receive and decrypt the captured data.

bash
Copy code
python listen.py
The decrypted data will be saved in the logs/ directory.
## Usage on Windows

In build folder, there is an executable `.exe` file. You can run this file to perform the relevant task.

## Configuration
You can configure the broadcasting settings in keylogger.py by modifying the broadcast_ip and port variables to match your network environment.


## Acknowledgments
This keylogger is for educational purposes only. Use it responsibly and only on systems you have permission to monitor.
Disclaimer: This software is intended for educational and ethical purposes only. The author is not responsible for any misuse of the software or any damage caused by it. Use this software responsibly and in compliance with applicable laws and regulations.

