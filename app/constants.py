""""
* Author: Cesar M. Gonzalez R.
* CreateAt: 30/04/2023

I Have been pwned Constants
"""

import re


I_HAVE_BEEN_PWNED_URL = "https://haveibeenpwned.com/"                               # I Have been pwned website URL

EMAIL_REGEX = re.compile("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")               # Email regex validation
PHONE_NUMBER_REGEX = re.compile("^\\+?[1-9][0-9]{7,14}$")                           # Phone number regex validation