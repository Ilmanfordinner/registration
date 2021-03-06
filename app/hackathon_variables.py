# HACKATHON PERSONALIZATION
import os

from django.utils import timezone

HACKATHON_NAME = 'Oxford Hack 2020'
# What's the name for the application
HACKATHON_APPLICATION_NAME = 'Oxford Hack Registration'
# Hackathon timezone
TIME_ZONE = 'Europe/London'
# This description will be used on the html and sharing meta tags
HACKATHON_DESCRIPTION = 'Oxford Hack is the official Oxford student Hackathon, where over 300 people gather every year to collaborate, innovate, learn and experiment while creating a project from scratch in 24 hours.'
# Domain where application is deployed, can be set by env variable
HACKATHON_DOMAIN = os.environ.get('DOMAIN', None)
HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME', None)
if HEROKU_APP_NAME and not HACKATHON_DOMAIN:
    HACKATHON_DOMAIN = '%s.herokuapp.com' % HEROKU_APP_NAME
elif not HACKATHON_DOMAIN:
    HACKATHON_DOMAIN = 'localhost:8000'
# Hackathon contact email: where should all hackers contact you. It will also be used as a sender for all emails
HACKATHON_CONTACT_EMAIL = 'committee@oxfordhack.co.uk'
# Hackathon logo url, will be used on all emails
HACKATHON_LOGO_URL = 'https://oxfordhack.co.uk/static/media/logo.7b5fedba.png'

HACKATHON_OG_IMAGE = 'https://oxfordhack.co.uk/static/media/logo.7b5fedba.png'
# (OPTIONAL) Track visits on your website
# HACKATHON_GOOGLE_ANALYTICS = 'UA-7777777-2'
# (OPTIONAL) Hackathon twitter user
# HACKATHON_TWITTER_ACCOUNT = 'casassaez'
# (OPTIONAL) Hackathon Facebook page
HACKATHON_FACEBOOK_PAGE = 'oxfordhack2020'
# (OPTIONAL) Github Repo for this project (so meta)
# HACKATHON_GITHUB_REPO = 'https://github.com/Ilmanfordinner/registration'

# (OPTIONAL) Applications deadline
HACKATHON_APP_DEADLINE = timezone.datetime(2020, 11, 11, 23, 59, tzinfo=timezone.pytz.timezone(TIME_ZONE))
# (OPTIONAL) When to arrive at the hackathon
HACKATHON_ARRIVE = 'The opening ceremony will be at <strong>9AM, Saturday 14th of November</strong>. <br>' \
                   'We will provide a streaming link on the Slack group and via email.'

# (OPTIONAL) When to arrive at the hackathon
HACKATHON_LEAVE = 'The project submission deadline will be at <strong>9PM, Sunday 15th of November</strong>. <br>' \
                  'That will be followed by judging on Monday morning and a closing ceremony livestream at 5PM.'

# (OPTIONAL) Hackathon live page
# HACKATHON_LIVE_PAGE = 'https://gerard.space/live'

# (OPTIONAL) Regex to automatically match organizers emails and set them as organizers when signing up
REGEX_HACKATHON_ORGANIZER_EMAIL = '^.*@oxfordhack\.co\.uk$'

# (OPTIONAL) Sends 500 errors to email whilst in production mode.
HACKATHON_DEV_EMAILS = ['ilmansonic@gmail.com']

# Reimbursement configuration
REIMBURSEMENT_ENABLED = False
CURRENCY = '$'
REIMBURSEMENT_EXPIRY_DAYS = 5
REIMBURSEMENT_REQUIREMENTS = 'You have to submit a project and demo it during the event in order to be reimbursed.'
REIMBURSEMENT_DEADLINE = timezone.datetime(2028, 2, 24, 3, 14, tzinfo=timezone.pytz.timezone(TIME_ZONE))

# (OPTIONAL) Max team members. Defaults to 4
TEAMS_ENABLED = True
HACKATHON_MAX_TEAMMATES = 4

# (OPTIONAL) Code of conduct link
# CODE_CONDUCT_LINK = "https://pages.hackcu.org/code_conduct/"

# (OPTIONAL) Slack credentials
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'test'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

# (OPTIONAL) Logged in cookie
# This allows to store an extra cookie in the browser to be shared with other application on the same domain
LOGGED_IN_COOKIE_DOMAIN = '.oxfordhack.co.uk'
LOGGED_IN_COOKIE_KEY = 'hackassistant_logged_in'

# Hardware configuration
HARDWARE_ENABLED = False
# Hardware request time length (in minutes)
HARDWARE_REQUEST_TIME = 15
# Can Hackers start a request on the hardware lab?
# HACKERS_CAN_REQUEST = False

# Enable dubious separate pipeline (disabled by default)
DUBIOUS_ENABLED = False


# Enable blacklist separate pipeline (disabled by default)
BLACKLIST_ENABLED = False

SUPPORTED_RESUME_EXTENSIONS = [".pdf"]

# Mentor/Volunteer applications can expire if they are invited, set to False to not
MENTOR_EXPIRES = False
VOLUNTEER_EXPIRES = False
