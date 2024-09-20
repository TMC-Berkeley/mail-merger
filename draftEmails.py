import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from base64 import urlsafe_b64encode
from email.mime.text import MIMEText
import pandas as pd

# Gmail API scopes
SCOPES = ['https://mail.google.com/']

# Authenticate with Gmail API
def gmail_authenticate():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

# Function to create the email message
def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = urlsafe_b64encode(message.as_bytes()).decode()
    return {'message': {'raw': raw}}

# Function to create draft
def create_draft(service, sender_email, to_email, subject, message_text):
    email_message = create_message(sender_email, to_email, subject, message_text)
    try:
        draft = service.users().drafts().create(userId='me', body=email_message).execute()
        print(f"Draft created for {to_email}. Draft Id: {draft['id']}")
    except Exception as e:
        print(f"An error occurred while creating draft for {to_email}: {str(e)}")

# Main function to iterate over outputDF and create drafts
def create_drafts_from_df(outputDF):
    service = gmail_authenticate()  # Authenticate with Gmail API
    sender_email = 'tmcberkeley@gmail.com'  # Update with your own Gmail address
    subject = "Your Music Connection Placement"

    for index, row in outputDF.iterrows():
        to_email = row['Email']  # Tutor's email
        message_text = row['Text']  # Generated email content
        create_draft(service, sender_email, to_email, subject, message_text)
