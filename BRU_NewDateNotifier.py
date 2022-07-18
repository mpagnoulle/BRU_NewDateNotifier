#!/usr/bin/python3

import requests, smtplib, ssl, os, sched, time, email.message, email.utils, logging, traceback
from datetime import datetime

# Calendar related
calendar_url = "https://webcalendar.brucity.be/qmaticwebbooking/rest/schedule/branches/e58833ee8321437b292cd75df53f283fdc0b56ca09b678971ad3ca509edcb862/dates;servicePublicId=hidebfeab6987796c5f484529fcea02e924401747b1aca9d20a3695623027cc1;customSlotLength=35"
target_date = datetime(2022, 8, 16)

# Email related
receiver_email = ""
smtp_email = ""
smtp_server = ""
smtp_port = 465
smtp_password = ""

# Create and configure logger
logging.basicConfig(filename="BRU_NDN.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Fetching new dates and acting if needed
def fetch_date(sc):
    try:
        print(">>> Fetching new date...")
        req = requests.get(calendar_url)
        if(req.status_code == 200):
            data = req.json()
            fetched_date = datetime.strptime(data[0]["date"], '%Y-%m-%d')
            fetched_date_str = fetched_date.strftime('%Y-%m-%d')
            print(f"    Earliest date is {fetched_date_str}")
            if(fetched_date < target_date):
                send_email_notification(fetched_date_str)
            else:
                print(f"    \033[93mSadly not earlier :(\033[0m\n")
    except Exception as e:
        logger.error(traceback.format_exc())
    finally:
        sc.enter(11400, 1, fetch_date, (sc,))

# Email Sender
def send_email_notification(new_date):
    print(f"    \033[95mSending email...")
    context = ssl._create_unverified_context()

    msg = email.message.Message()
    msg['From'] = smtp_email
    msg['To'] = receiver_email
    msg['Subject'] = "[BRU] New date available on: " + new_date
    msg.add_header('Content-Type', 'text')

    message = """\
    Hey,

    Just letting you know there is an appointment available at an earlier date than: {target_dat}, it's on {newer_date}

    Feel free to modify your appointment.""".format(target_dat=target_date.strftime('%Y-%m-%d'), newer_date=new_date)

    msg.set_payload(message)

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_email, smtp_password)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

    logger.info("Earlier date found ({newer_date}), email was sent!").format(newer_date=new_date)
    print(f"    Email sent!\033[0m\n")

# Ask for password
if not smtp_password:
    smtp_password = input("Type your smtp password and press enter: ")
os.system('clear')

# Start checking for dates regularly
print("New dates will be checked for around every 10 minutes...")
s = sched.scheduler(time.time, time.sleep)
s.enter(5, 1, fetch_date, (s,))
s.run()
