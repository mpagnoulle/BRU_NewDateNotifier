# BRU_NDN - Brussels City Hall Appointement New Date Notifier

BRU_NDN is a Python script that automates the process of checking for new appointment dates from a specific Qmatic web calendar. It is designed to work with the Qmatic web booking system used by the city of Brussels. If a new date becomes available that is earlier than a specified target date, the script sends an email notification to a designated recipient.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- Necessary Python packages installed: `requests`, `smtplib`, `ssl`, `os`, `schedule`, `time`, `email`.

## Configuration

1. Update the `calendar_url` variable with the URL of the Qmatic web booking calendar that you want to monitor.

2. Set the `target_date` variable to the desired target date for your appointment.

3. Fill in the email-related variables:
   - `receiver_email`: Email address of the recipient who will receive notifications.
   - `smtp_email`: Your SMTP email address.
   - `smtp_server`: SMTP server for sending emails.
   - `smtp_port`: SMTP server port (default: 465).
   - `smtp_password`: SMTP password. If not provided, the script will prompt you to enter it.

## Usage

1. Open a terminal and navigate to the directory containing the script.

2. Run the script using the following command:

        python3 script_name.py

Replace `script_name.py` with the actual name of the script file.

3. The script will start checking for new dates approximately every 10 minutes.

4. If a new date earlier than the target date is found, the script will send an email notification to the recipient specified in the configuration.

5. The earliest checked date will be updated, and the script will continue to monitor for new dates.

## Notes

- The script uses the `schedule` library to run tasks at specified intervals.
- Logs are stored in the `BRU_NDN.log` file, including any errors encountered during execution.

## Disclaimer

This script is provided as-is and without any warranty. Use it responsibly and ensure it complies with any terms of use of the web calendar service you are monitoring.

## License

This project is licensed under the [MIT License](LICENSE).
