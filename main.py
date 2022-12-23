import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email(report, recipient, subject, sender, password):
    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    # Open the report file
    with open(report, "rb") as f:
        # Create a MIMEBase object for the report
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={report}")
        msg.attach(part)

    # Create an SMTP server object
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)

    # Send the email
    server.sendmail(sender, recipient, msg.as_string())

    # Close the server
    server.quit()


# Test the emailer
send_email("report.pdf", "recipient@example.com", "Report", "sender@example.com", "password")

