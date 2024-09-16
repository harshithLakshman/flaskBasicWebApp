from mailjet_rest import Client
import os

def sendEmailAck(form_data,jobs):
  api_key = '8e748b5495af5434733bd19a427bdf80'
  api_secret = '803613b7339a8b4824032a1873cb4cfb'
  mailjet = Client(auth=(api_key, api_secret), version='v3.1')
  data = {
    'Messages': [
      {
        "From": {
          "Email": "harshith.l2000@gmail.com",
          "Name": "InnoSphere Careers"
        },
        "To": [
          {
          "Email": form_data['email'],
          "Name": form_data['name']
          }
        ],
        "Subject": "Job Application Acknowledgement",
        "TextPart": "Thank you for your application.",
        "HTMLPart": f"""<!DOCTYPE html>
                      <html lang="en">
                      <head>
                      <meta charset="UTF-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1.0">
                      <title>Job Application Acknowledgement</title>
                      <style>
                      body {{
                          font-family: Arial, sans-serif;
                          color: #333;
                          margin: 0;
                          padding: 0;
                          background-color: #f4f4f4;
                      }}
                      .container {{
                        max-width: 600px;
                        margin: 20px auto;
                        background: #ffffff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                     }}
                      .header {{
                        background-color: #007bff;
                        color: #ffffff;
                        padding: 10px 20px;
                        border-radius: 8px 8px 0 0;
                        text-align: center;
                      }}
                      .content {{
                        padding: 20px;
                      }}
                      .footer {{
                        background-color: #007bff;
                        color: #ffffff;
                        padding: 10px 20px;
                        border-radius: 0 0 8px 8px;
                        text-align: center;
                    }}
                      a {{
                        color: #007bff;
                        text-decoration: none;
                      }}
                      .button {{
                        display: inline-block;
                        background-color: #007bff;
                        color: #ffffff;
                        padding: 10px 20px;
                        border-radius: 5px;
                        text-decoration: none;
                    }}
                      </style>
                    </head>
                    <body>
                      <div class="container">
                      <div class="header">
                        <h4>Thank You for Your Application!</h4>
                      </div>
                      <div class="content">
                        <p>Dear {form_data['name']},</p>
                        <p>Thank you for applying for the position of <strong>{jobs['title']}</strong> at <strong>InnoSphere</strong>. We have received your application and our team is currently reviewing it.</p>
                        <p>We appreciate the time and effort you put into your application. We will get in touch with you soon if your qualifications match our requirements. In the meantime, if you have any questions, feel free to reply to this email.</p>
                        <p>Best regards,<br>
                        The InnoSphere Team</p>
                        <p><a href="https://flaskapp-innoventure-careers.onrender.com/" class="button">Visit Our Website</a></p>
                      </div>
                      <div class="footer">
                        <p>&copy; 2022 InnoSphere. All rights reserved.</p>
                      </div>
                      </div>
                      </body>
                    </html>""",
      "CustomID": "AppAcknowledgement"
      }
    ]
  }
  mailjet.send.create(data=data)

    