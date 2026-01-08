import requests
from exchangelib import Account, OAuth2Credentials, DELEGATE
from exchangelib.errors import UnauthorizedError
from datetime import datetime

# Replace these placeholders with your actual credentials
CLIENT_ID = 'f6f6a3e7-6a76-4aba-b292-549b0f84dcbf'
CLIENT_SECRET = 'bpQ8Q~~er6KmmrVYjVp48mJvAQ2LztizX8SvCad6'
TENANT_ID = 'd279d730-8679-40ea-8a1a-0a37fbf29735'
EMAIL = 'benjaminbritcliffe@outlook.com'
OAUTH2_TOKEN_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'

def fetch_oauth2_token():
    # Function to fetch OAuth2 token
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://outlook.office365.com/.default',
        'grant_type': 'client_credentials'
    }
    response = requests.post(OAUTH2_TOKEN_URL, data=data)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def fetch_and_merge_emails(subjects_and_dates):
    # Function to fetch emails based on the subject and date
    try:
        token_info = fetch_oauth2_token()
        access_token = token_info['access_token']
        
        # Create OAuth2 credentials using the access token
        credentials = OAuth2Credentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            access_token=access_token,
            token_type='Bearer'  # Set token type to Bearer
        )
        
        # Connect to the Exchange account
        account = Account(EMAIL, credentials=credentials, autodiscover=True, access_type=DELEGATE)
        
        # Fetch emails matching the provided subjects and dates
        emails = []
        for subject, date in subjects_and_dates.items():
            items = account.inbox.filter(subject__icontains=subject, datetime_received__gte=date)
            emails.extend(items)
        
        return emails
    
    except UnauthorizedError:
        print("Invalid credentials. Please check your client ID and secret.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Let's start fetching the emails by subject and date.")
    subjects_and_dates = {}
    
    while True:
        subject = input("Enter the subject of the email to merge (or type 'finish' to stop): ")
        if subject.lower() == 'finish':
            break
        date_str = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
            subjects_and_dates[subject] = date
        except ValueError:
            print("Invalid date format. Please try again.")
    
    print("Fetching emails with the provided subjects and dates.")
    emails = fetch_and_merge_emails(subjects_and_dates)
    
    if emails:
        print(f"Fetched {len(emails)} emails:")
        for email in emails:
            print(f"Subject: {email.subject}, Received: {email.datetime_received}")
    else:
        print("No emails found.")

if __name__ == "__main__":
    main()
