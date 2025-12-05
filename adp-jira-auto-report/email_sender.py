import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

# Import credentials from config
try:
    from config import (
        SENDGRID_API_KEY, SENDER_EMAIL, RECIPIENT_EMAIL,
        MAILTRAP_USERNAME, MAILTRAP_PASSWORD, 
        MAILTRAP_SERVER, MAILTRAP_PORT
    )
except ImportError:
    print("❌ ERROR: config.py not found!")
    print("📝 Please copy config.example.py to config.py and add your credentials")
    print("   cp config.example.py config.py")
    sys.exit(1)

def send_jira_report_email(use_production=False):
    """
    Send automated JIRA report email
    
    Args:
        use_production (bool): If True, uses SendGrid (production). If False, uses Mailtrap (testing)
    """
    recipient_email = RECIPIENT_EMAIL
    
    # Email content
    subject = f"JIRA Automated Report - {datetime.now().strftime('%Y-%m-%d')}"
    
    if use_production:
        return send_via_sendgrid(recipient_email, subject)
    else:
        return send_via_mailtrap(recipient_email, subject)

def send_via_sendgrid(recipient_email, subject):
    """Send email using SendGrid (Production)"""
    print("🚀 Using SendGrid (PRODUCTION) - counts against your 100/day limit")
    
    # SendGrid configuration from config.py
    api_key = SENDGRID_API_KEY
    sender_email = SENDER_EMAIL
    
    html_content = f"""
    <html>
    <body>
        <h2>JIRA Automated Report</h2>
        <p>Hello,</p>
        
        <p>This is your automated JIRA report for <strong>{datetime.now().strftime('%B %d, %Y')}</strong>.</p>
        
        <h3>Report Summary:</h3>
        <ul>
            <li>Total tickets processed: [To be implemented]</li>
            <li>Open tickets: [To be implemented]</li>
            <li>Closed tickets: [To be implemented]</li>
            <li>High priority tickets: [To be implemented]</li>
        </ul>
        
        <p>This is a REAL email from the automated JIRA reporting system.</p>
        
        <p>Best regards,<br>
        ADP JIRA Auto Report System</p>
    </body>
    </html>
    """
    
    try:
        message = Mail(
            from_email=sender_email,
            to_emails=recipient_email,
            subject=subject,
            html_content=html_content
        )
        
        sg = SendGridAPIClient(api_key=api_key)
        response = sg.send(message)
        
        print(f"✅ Email sent successfully via SendGrid!")
        print(f"Status Code: {response.status_code}")
        return True
        
    except Exception as e:
        print(f"❌ SendGrid error: {str(e)}")
        return False

def send_via_mailtrap(recipient_email, subject):
    """Send email using Mailtrap (Testing)"""
    print("🧪 Using Mailtrap (TESTING) - email captured, not delivered")
    
    # Mailtrap configuration from config.py
    smtp_server = MAILTRAP_SERVER
    smtp_port = MAILTRAP_PORT
    username = MAILTRAP_USERNAME
    password = MAILTRAP_PASSWORD
    sender_email = "test@example.com"
    
    # Create HTML email
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    
    html_content = f"""
    <html>
    <body>
        <h2>JIRA Automated Report (TEST)</h2>
        <p>Hello,</p>
        
        <p>This is your automated JIRA report for <strong>{datetime.now().strftime('%B %d, %Y')}</strong>.</p>
        
        <h3>Report Summary:</h3>
        <ul>
            <li>Total tickets processed: [To be implemented]</li>
            <li>Open tickets: [To be implemented]</li>
            <li>Closed tickets: [To be implemented]</li>
            <li>High priority tickets: [To be implemented]</li>
        </ul>
        
        <p>This is a TEST email from the automated JIRA reporting system.</p>
        <p><em>Check your Mailtrap inbox to see this email.</em></p>
        
        <p>Best regards,<br>
        ADP JIRA Auto Report System</p>
    </body>
    </html>
    """
    
    html_part = MIMEText(html_content, "html")
    message.attach(html_part)
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"✅ Email sent successfully via Mailtrap!")
        print(f"📧 Check your Mailtrap inbox at mailtrap.io")
        return True
        
    except Exception as e:
        print(f"❌ Mailtrap error: {str(e)}")
        return False

if __name__ == "__main__":
    # Choose your mode:
    # False = Mailtrap (testing, unlimited, emails captured in web interface)
    # True = SendGrid (production, 100/day limit, real email delivery)
    
    use_production = False  # Change to True when ready for real emails
    
    print(f"Email Mode: {'PRODUCTION (SendGrid)' if use_production else 'TESTING (Mailtrap)'}")
    send_jira_report_email(use_production=use_production)