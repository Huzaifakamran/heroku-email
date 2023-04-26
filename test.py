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
print("Current Date: ", current_date)
print("Yesterday's Date: ", yesterday_date)

sender_email = "ssamthemessenger@gmail.com"
to_emails = ["muhammad.huzaifa@tmcltd.com"]
cc_emails = ["mohammadhuzaifa72@gmail.com"]
password = "kqtozidepgzdpobb"

HTML = """ 
<!DOCTYPE html>
<html>
<head>
        <title>Daily sSam's performance</title>
        <meta content="summary_large_image" name="twitter:card" />
        <meta content="website" property="og:type" />
        <meta content="" property="og:description" />
        <meta content="" property="og:title" />
        <meta content="" name="description" />
        <meta charset="utf-8" />
        <meta content="width=device-width" name="viewport" />
        <link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css" />
        <style>
            .bee-row-1 .bee-col-1 .bee-block-1,
            .bee-row-2 .bee-col-1,
            .bee-row-2 .bee-col-1 .bee-block-1,
            .bee-row-2 .bee-col-1 .bee-block-5,
            .bee-row-7 .bee-col-1 .bee-block-1 {{
                padding: 10px;
            }}

            .bee-row-1 .bee-col-1,
            .bee-row-2 .bee-col-1,
            .bee-row-2 .bee-col-2,
            .bee-row-3 .bee-col-1,
            .bee-row-4 .bee-col-1,
            .bee-row-4 .bee-col-2,
            .bee-row-5 .bee-col-1,
            .bee-row-6 .bee-col-1,
            .bee-row-7 .bee-col-1 {{
                border-bottom: 0 solid transparent;
                border-left: 0 solid transparent;
                border-right: 0 solid transparent;
                border-top: 0 solid transparent;
            }}

            .bee-html-block {{
                text-align: center;
                position: relative;
            }}

            .bee-row-1,
            .bee-row-1 .bee-row-content,
            .bee-row-2,
            .bee-row-2 .bee-row-content,
            .bee-row-3,
            .bee-row-4,
            .bee-row-5,
            .bee-row-6,
            .bee-row-7,
            .bee-row-7 .bee-row-content {{
                background-repeat: no-repeat;
            }}

            body {{
                background-color: #ecfbff;
                color: #000;
                font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;
            }}

            a {{
                color: #0068a5;
            }}

            .bee-row-2 .bee-row-content {{
                background-color: #143059;
            }}

            .bee-row-2 .bee-col-1 .bee-block-2,
            .bee-row-2 .bee-col-1 .bee-block-4 {{
                padding-left: 20px;
            }}

            .bee-row-2 .bee-col-1 .bee-block-3 {{
                padding-bottom: 10px;
                padding-left: 10px;
                padding-right: 10px;
            }}

            .bee-row-2 .bee-col-2 {{
                padding-bottom: 5px;
                padding-top: 5px;
            }}

            .bee-row-2 .bee-col-2 .bee-block-1,
            .bee-row-2 .bee-col-2 .bee-block-4 {{
                padding: 5px;
            }}

            .bee-row-2 .bee-col-2 .bee-block-2 {{
                padding: 20px;
            }}

            .bee-row-2 .bee-col-2 .bee-block-3 {{
                width: 100%;
                padding: 10px;
            }}

            .bee-row-3 .bee-row-content,
            .bee-row-4 .bee-row-content,
            .bee-row-5 .bee-row-content,
            .bee-row-6 .bee-row-content {{
                background-color: #fff;
                background-repeat: no-repeat;
            }}

            .bee-row-3 .bee-col-1 {{
                padding: 5px;
            }}

            .bee-row-3 .bee-col-1 .bee-block-1 {{
                padding: 20px 30px 10px;
            }}

            .bee-row-4 .bee-col-1 {{
                padding: 5px;
                max-width: 200px;
            }}
            @media only screen and (min-device-width: 560px) {{
                .bee-row-4 .bee-col-1 {{
                    padding: 30px !important;
                }}
            }}
            @media (min-width: 560px) {{
                .bee-row-4 .bee-col-1 {{
                    padding: 30px !important;
                }}
            }}

            .bee-row-5 .bee-col-1 {{
                padding-left: 5px;
                padding-right: 5px;
            }}

            .bee-row-6 .bee-col-1 .bee-block-1 {{
                padding: 10px;
            }}

            * {{
                box-sizing: border-box;
            }}

            body,
            p {{
                margin: 0;
            }}

            .bee-desktop_hide {{
                display: none;
            }}

            .bee-row-content {{
                max-width: 540px;
                margin: 0 auto;
                display: flex;
                justify-content: center;
            }}

            .bee-row-content .bee-col-w6 {{
                flex: 6;
            }}

            .bee-row-content .bee-col-w12 {{
                flex: 12;
            }}

            .bee-image img {{
                display: block;
                width: 100%;
            }}

            .bee-divider,
            .bee-image {{
                overflow: auto;
            }}

            .bee-divider .bee-center,
            .bee-image .bee-center {{
                margin: 0 auto;
            }}

            .bee-text {{
                overflow-wrap: anywhere;
            }}

            @media only screen and (max-device-width: 560px) {{
                .bee-desktop_hide,
                .bee-row-content:not(.no_stack) {{
                    display: block;
                }}
            }}
            @media (max-width: 560px) {{
                .bee-desktop_hide,
                .bee-row-content:not(.no_stack) {{
                    display: block;
                }}
            }}

            .bee-performance-item {{
                padding: 0 10px 10px;
            }}
            @media only screen and (min-device-width: 560px) {{
                .bee-performance-item {{
                    padding: 0 26px 20px !important;
                }}
            }}
            @media (min-width: 560px) {{
                .bee-performance-item {{
                    padding: 0 26px 20px !important;
                }}
            }}
            .primary-label {{
				font-size: 24px;
				font-weight: bold;
				letter-spacing: 1.5px;
			}}
			.primary-label.large-label {{
				/*font-size: calc(40px - 0.5vw);*/
				font-size: 40px;
				margin-top: 10%;
				color: #29873f;
			}}
			.secondary-label {{
				font-size: 16px;
				position: absolute;
				width: 100%;
				text-align: center;
				bottom: 16%;
			}}

			@media only screen and (max-device-width: 480px) {{
				.primary-label {{
					font-size: unset !important;
				}}
				.primary-label.large-label {{
					font-size: 30px !important;
				}}
				.secondary-label {{
					font-size: 14px !important;
				}}
			}}

			@media only screen and (max-device-width: 320px) {{
				.primary-label {{
					font-size: unset;
				}}
				.primary-label.large-label {{
					font-size: 30px;
				}}
				.secondary-label {{
					font-size: 14px !important;
				}}
			}}
        </style>
    </head>
    <body>
        <div class="bee-page-container">
            <div class="bee-row bee-row-1">
                <div class="bee-row-content">
                    <div class="bee-col bee-col-1 bee-col-w12">
                        <div class="bee-block bee-block-1 bee-divider">
                            <div class="spacer" style="height: 0px;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="bee-row bee-row-2">
                <div class="bee-row-content no_stack">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border: 0; max-width: 600px !important;">
                        <tr>
                            <td align="left" style="vertical-align: middle;">
                                <div class="bee-col bee-col-1 bee-col-w6">
                                    <div class="bee-block bee-block-1 bee-text">
                                        <div class="bee-text-content" style="font-size: 12px; line-height: 120%; color: #393d47; font-family: inherit;">
                                            <p style="font-size: 12px; line-height: 14px;"></p>
                                        </div>
                                    </div>
                                    <div class="bee-block bee-block-2 bee-text">
                                        <div class="bee-text-content" style="line-height: 120%; font-size: 12px; color: #ffffff; font-family: inherit;">
                                            <p style="font-size: 14px; line-height: 16px;">
                                                <span style="font-size: 24px; line-height: 40px;">
                                                    <span style="font-weight: bold; line-height: 14px;">
                                                        Daily sSam's  
                                                    </span>
                                                    <span style="font-size: 20px; line-height: 10px;">
                                                        Performance
                                                    </span>
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                    <div class="bee-block bee-block-3 bee-divider">
                                        <div class="spacer" style="height: 0px;"></div>
                                    </div>
                                    <!-- <div class="bee-block bee-block-4 bee-text">
                                        <div class="bee-text-content" style="line-height: 120%; font-size: 12px; color: #ffffff; font-family: inherit;">
                                            <p style="font-size: 14px; line-height: 16px; text-align: left;">
                                                <span style="font-size: 18px; line-height: 21px;">
                                                    
                                                </span>
                                            </p>
                                        </div>
                                    </div> -->
                                    <div class="bee-block bee-block-5 bee-text">
                                        <div class="bee-text-content" style="font-size: 12px; line-height: 120%; color: #393d47; font-family: inherit;">
                                            <p style="font-size: 12px; line-height: 14px;"></p>
                                        </div>
                                    </div>
                                </div>
                            </td>
                            <td align="right" style="vertical-align: middle;">
                                <div class="bee-col bee-col-2 bee-col-w6">
                                    <div class="bee-block bee-block-1 bee-divider">
                                        <div class="spacer" style="height: 0px;"></div>
                                    </div>
                                    <!-- <div class="bee-block bee-block-2 bee-divider bee-desktop_hide">
                                        <div class="spacer" style="height: 0px;"></div>
                                    </div> -->
                                    <div class="bee-block bee-block-3 bee-image">
                                        <img alt="GIFT: 30% OFF" class="bee-center bee-autowidth" src="https://ssam-service.s3.amazonaws.com/images/ssam-logo.png" style="max-width: 150px;" />
                                    </div>
                                    <div class="bee-block bee-block-4 bee-divider">
                                        <div class="spacer" style="height: 0px;"></div>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2">
                                <div class="bee-col bee-col-1 bee-col-w6" style="padding-top: 0;">
                                    <div class="bee-block bee-block-4 bee-text">
                                        <div class="bee-text-content" style="line-height: 120%; font-size: 12px; color: #ffffff; font-family: inherit;">
                                            <p style="font-size: 14px; line-height: 16px; text-align: left;">
                                                <span style="font-size: 14px;">
                                                    {} ~ {}
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bee-col bee-col-1 bee-col-w6" style="padding-top: 0;">
                                    <div class="bee-block bee-block-4 bee-text">
                                        <div class="bee-text-content" style="line-height: 120%; font-size: 12px; color: #ffffff; font-family: inherit;">
                                            <p style="font-size: 14px; line-height: 16px; text-align: left;">
                                                <span style="font-size: 14px;">
                                                    Created -  {} 
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="bee-row bee-row-4">
                <div class="bee-row-content no_stack">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border: 0; max-width: 600px !important;">
                        <tr>
                            <td align="center" style="width: 33.3%;">
                                <div class="bee-col bee-col-1 bee-col-w6" style="padding-bottom: 10px !important;">
                                    <div class="bee-block bee-block-1 bee-html-block">
                                        <div class="our-class" style="width: 100%; height: 0; border: 1px solid black; border-radius: 50%; border-color: #29873f; padding-bottom: 100%; min-width: 80px;">
                                            <div class="primary-label large-label">
                                                20
                                            </div>
                                            <div class="secondary-label">
                                                Daily
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </td>
                            <td align="center" style="width: 33.3%;">
                                <div class="bee-col bee-col-1 bee-col-w6" style="padding-bottom: 10px !important;">
                                    <div class="bee-block bee-block-1 bee-html-block">
                                        <div class="our-class" style="width: 100%; height: 0; border: 1px solid black; border-radius: 50%; border-color: #29873f; padding-bottom: 100%; min-width: 80px;">
                                            <div class="primary-label large-label">
                                                30
                                            </div>
                                            <div class="secondary-label">
                                                Weekly total
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </td>
                            <td align="center" style="width: 33.3%;">
                                <div class="bee-col bee-col-1 bee-col-w6" style="padding-bottom: 10px !important;">
                                    <div class="bee-block bee-block-1 bee-html-block">
                                        <div class="our-class" style="width: 100%; height: 0; border: 1px solid black; border-radius: 50%; border-color: #29873f; padding-bottom: 100%; min-width: 80px;">
                                            <div class="primary-label large-label">
                                                50
                                            </div>
                                            <div class="secondary-label">
                                                Mothly total
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        
                    </table>
                </div>
            </div>
            <div class="bee-row bee-row-3">
                <div class="bee-row-content">
                    <div class="bee-col bee-col-1 bee-col-w12">
                        <div class="bee-block bee-block-1 bee-text">
                            <div class="bee-text-content" style="line-height: 120%; font-size: 12px; color: #000000; font-family: inherit;">
                                <p style="font-size: 14px; line-height: 16px;">
                                    <span style="font-size: 22px; line-height: 28px;">
                                        Interactions to Review:
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="bee-row bee-row-5">
                <div class="bee-row-content">
                    <div class="bee-col bee-col-1 bee-col-w12">
                        <div class="bee-block bee-block-1 bee-html-block">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; border: 0; max-width: 600px !important;">
                                                           
                            <!--begin individual job-->
                            <tr>
                                <td class="bee-performance-item" style="border: 0; font-weight: normal; background-color: #ffffff; mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top">
                                    <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                        <tr>
                                            <td
                                                style="
                                                    border-left: 4px solid #ff6969;
                                                    padding-left: 20px;
                                                    mso-line-height-rule: exactly;
                                                    -ms-text-size-adjust: 100%;
                                                    -webkit-text-size-adjust: 100%;
                                                    text-align: left;
                                                    font-size: 14px;
                                                    font-family: 'Lato', Roboto, Helvetica;
                                                    line-height: 150%;
                                                    color: #000000;
                                                    word-break: break-word;
                                                "
                                                valign="top"
                                            >
                                                <a href="#" rel="noopener" style="color: #ff6969; font-size: 16px; font-weight: bold;" target="_blank">
                                                     results.task 
                                                </a>
                                                <br />
                                                #if uid From: uid 
                                                <br />
                                                else/if Query:  query
                                                <br />
                                                Confidence:  results.task_confidence 
                                                <br />
                                                Status:  status 
                                                <br />
                                                Created:  createdAt 
                                                <br />
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <!--end individual job-->
                           
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="bee-row bee-row-6">
                <div class="bee-row-content">
                    <div class="bee-col bee-col-1 bee-col-w12">
                        <div class="bee-block bee-block-1 bee-divider">
                            <div class="spacer" style="height: 0px;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="bee-row bee-row-7">
                <div class="bee-row-content">
                    <div class="bee-col bee-col-1 bee-col-w12">
                        <div class="bee-block bee-block-1 bee-divider">
                            <div class="spacer" style="height: 0px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
 """.format(yesterday_date,current_date,current_date)

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