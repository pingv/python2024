# ADP JIRA Auto Report

This project contains an automated JIRA reporting system that sends email reports.

## Setup

1. Update the SMTP configuration in `email_sender.py`:
   - `smtp_server`: Your SMTP server
   - `smtp_port`: SMTP port (usually 587 for TLS)
   - `sender_email`: Your sender email address
   - `sender_password`: Your email app password

2. Install required dependencies:
   ```bash
   pip install smtplib email
   ```

## Usage

Run the email sender:
```bash
python email_sender.py
```

## Configuration

Update the recipient email address in the code and configure your SMTP settings before running.
