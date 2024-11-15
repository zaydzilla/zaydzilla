import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
# Function to send email
def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    try:
        # Email setup
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
# Function to check the price
def check_price():
    url = "https://doorway-api.knockrentals.com/v1/property/2019943/units"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        data = response.json()
        # Navigate to the 'units' key in the JSON response
        units = data.get("units_data", {}).get("units", [])
        # Check each unit for the desired displayPrice
        for unit in units:
            if unit.get("displayPrice") == "2475":
                print("Match found! Sending email...")
                # Email details
                send_email(
                    subject="Apartment Available at $2675",
                    body="An apartment with a display price of $2675 is now available.",
                    to_email="testzaitsev@gmail.com", # Replace with your email
                    from_email="testzaitsev@gmail.com", # Replace with sender email
                    smtp_server="in-v3.mailjet.com", # Replace with your SMTP server
                    smtp_port=587,
                    login="d68ef74d8a8539b32c565120cc66156d", # Replace with sender email
                    password="a60c03a354737bc915b2cdf97eb13d6e"  # Replace with sender email's password
                )
                return
        print("No match found.")
    except Exception as e:
        print(f"Error fetching data: {e}")
# Run the script every 3 hours
while True:
    check_price()
    sleep(3 * 60 * 60)  # Sleep for 3 hours