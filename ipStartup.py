# socket library is required for this
import socket
import smtplib, ssl
import fcntl
import struct
import time

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
            )[20:24])
    except:
        return "undefined"

# send the email
def sendEmail():
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
        try:
            server.sendmail(sender_email, "peters.taylor@gmail.com", get_ip_address(b'wlan0'))
        except:
            server.sendmail(sender_email, "peters.taylor@gmail.com", get_ip_address(b'eth0'))
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

# get the ip address
time.sleep(30)
#wlan = get_ip_address(b'wlan0') #Function call
#eth = get_ip_address(b'eth0')
#output = "Wireless: " + wlan + " | "
#output = output + "Ethernet: " + eth
#print(output)
sendEmail()
