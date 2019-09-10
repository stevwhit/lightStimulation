# socket library is required for this
import socket
import smtplib, ssl

# Function to display hostname and
# IP address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except:
        print("Unable to get Hostname and IP")

# send the email
def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "lightstimulation@gmail.com"
    # todo: find a more secure way to store the password
    password = "seniordesign"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, "peters.taylor@gmail.com", message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

# get the ip address
ipAddress = get_Host_name_IP() #Function call
sendEmail(ipAddress)
