'''
Configuration Settings
'''

''' Uncomment to configure using the file.  
WARNING: Be careful not to post your account credentials on GitHub.

TWILIO_ACCOUNT_SID = "ACebc9c0c66174393f3031c888c67d056d" 
TWILIO_AUTH_TOKEN = "dab325c61da285e7f18aebfdceb22fe0"
TWILIO_APP_SID = "SD4f57d2e5553a968e28c875535080970d"
TWILIO_CALLER_ID = "+12563306369"
'''

# Begin Heroku configuration - configured through environment variables.
import os
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_CALLER_ID = os.environ.get('TWILIO_CALLER_ID', None)
TWILIO_APP_SID = os.environ.get('TWILIO_APP_SID', None)
