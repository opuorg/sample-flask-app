import os

class Config:
    SLACK_SUPPORT_URL = os.environ.get('SLACK_SUPPORT_URL')
    SLACK_SECURITY_URL = os.environ.get('SLACK_SECURITY_URL')
    SLACK_WIN_ALERT_URL = os.environ.get('SLACK_WIN_ALERT_URL')
    SLACK_LEAD_ALERT_URL = os.environ.get('SLACK_LEAD_ALERT_URL')
    # STATUSIO_COMPONENT_ID = os.environ.get('STATUSIO_COMPONENT_ID')
    STATUSIO_API_KEY = os.environ.get('STATUSIO_API_KEY')
    STATUSIO_PAGE_ID = os.environ.get('STATUSIO_PAGE_ID')