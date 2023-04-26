import smtplib
from tabulate import tabulate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import psycopg2
import datetime
import pytz


# Get the current time in the Pacific Time Zone (PST/PDT)
timezone = pytz.timezone('US/Pacific')
current_time = datetime.datetime.now(timezone)

# Get the current date and date one day before the current date
current_date = current_time.strftime('%a, %b %d, %I:%M %p %Z')
yesterday_date = (current_time - datetime.timedelta(days=1)).strftime('%a, %b %d, %I:%M %p %Z')


DATABASE_URL = "postgres://eczvjchosxwpcs:96191a4fb8fc12e2fce2ec7315115b4b634614653acbb6f481d6a4a8d2170192@ec2-100-26-39-41.compute-1.amazonaws.com:5432/dfkh38d1dqeie4"

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()
cur.execute("SELECT * from public.customer_dialogue_tb where date(created_at)=CURRENT_DATE")
rows = cur.fetchall()
cur.close()
# print(rows)
# print(len(rows))
dailyCount = len(rows)

#Weekly
weekly = conn.cursor()
weekly.execute("SELECT user_identifier, user_message, bot_message FROM public.customer_dialogue_tb WHERE created_at >= date_trunc('week', CURRENT_DATE) AND created_at < date_trunc('week', CURRENT_DATE) + INTERVAL '1 week';")
details_res = weekly.fetchall()
weekly.close()
weeklyCount = len(details_res)
# print(weeklyCount)
# print(details_res)

#Monthly
monthly = conn.cursor()
monthly.execute("SELECT user_identifier, user_message, bot_message FROM public.customer_dialogue_tb WHERE created_at >= date_trunc('month', CURRENT_DATE) AND created_at < date_trunc('month', CURRENT_DATE) + INTERVAL '1 month';")
monthly_res = monthly.fetchall()
monthly.close()
monthlyCount = len(monthly_res)
# print(monthlyCount)
# print(monthly_res)


message_rows = {}
for row in monthly_res:
    phone_number = row[0]
    customer_message = row[1]
    bot_message = row[2]

    if phone_number not in message_rows:
        message_rows[phone_number] = []

    message_rows[phone_number].append([customer_message, bot_message])

# print(message_rows)
sender_email = "ssamthemessenger@gmail.com"
to_emails = ["muhammad.huzaifa@tmcltd.com"]
cc_emails = ["mohammadhuzaifa72@gmail.com"]
password = "kqtozidepgzdpobb"

HTML = """  
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
</head>
<body>
    <h1>Daily Updates!!..</h1><br>
    
    <table border="1" style="background: white; border-radius:3px; border-collapse: collapse; height: auto;">
        <tbody>
            <tr style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; padding:8px;">
                <td style="background:#FFFFFF; padding:5px; text-align:left; vertical-align:middle; font-weight:300; font-size:13px; border-right: 1px solid;"><span style="font-weight:bold">Daily Interactions</span></td>
                <td style="background:#FFFFFF; padding:5px; text-align:left; vertical-align:middle; font-weight:300; font-size:13px; border-right: 1px solid;">{}</td>
            </tr>
            <tr style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; padding:8px;">
                <td style="background:#FFFFFF; padding:5px; text-align:left; vertical-align:middle; font-weight:300; font-size:13px; border-right: 1px solid;"><span style="font-weight:bold">Weekly Interactions</span></td>
                <td style="background:#FFFFFF; padding:5px; text-align:left; vertical-align:middle; font-weight:300; font-size:13px; border-right: 1px solid;">{}</td>
            </tr>
        </tbody>
    </table>
    <br>
    <br>
    <table border="1" style="background: white; border-radius:3px; border-collapse: collapse; height: auto;">
        <tbody>
            <tr>
                <th>Phone Number</th>
                <th>Customer Message</th>
                <th>Bot Message</th>
            </tr>
""".format(dailyCount, weeklyCount)

for phone_number, messages in message_rows.items():
    print('len msg',len(messages))
    # print(phone_number)
    print(messages)
    # print(enumerate(messages))
    HTML += "<tr><td rowspan='{}'>{}</td>".format(len(messages), phone_number)
    for i, (customer_message, bot_message) in enumerate(messages):
        # print('i',i)
        print(customer_message)
        print(bot_message)
        if i > 0:
            HTML += "<tr>"
        HTML += "<td>{}</td>".format(customer_message)
        HTML += "<td>{}</td>".format(bot_message)
        HTML += "</tr>"

HTML += """
        </tbody>
    </table>
</body>
</html>
"""

msg = MIMEMultipart()
msg['Subject'] = "Daily updates"
msg['From'] = sender_email
msg['To'] = ", ".join(to_emails)
msg['Cc'] = ", ".join(cc_emails)

html_body = MIMEText(HTML, 'html')
msg.attach(html_body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, to_emails + cc_emails, msg.as_string())