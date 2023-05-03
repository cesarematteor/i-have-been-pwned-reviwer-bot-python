""""
* Author: Cesar M. Gonzalez R.
* CreateAt: 30/04/2023

I have been pwned main
"""

from selenium import webdriver

from webcontroller.i_have_been_pwned_page import IHaveBeenPwnedPage


def check_pwned_list(emails: [str]) -> [tuple]:
    # Init Browser and Page controller
    print("Init I Have Been Pwned webdriver")
    options = webdriver.ChromeOptions()
    # Use the chrome options to execute on Docker or Serverless
    """options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')"""
    driver = webdriver.Chrome(options=options)
    been_pwned = IHaveBeenPwnedPage(driver)

    # For each on of the emails
    print(f"Process {len(emails)} emails")
    for email in emails:
        email_status = been_pwned.check_email_phone_data_breach(email)
        yield (email, email_status)

    # Close browser
    driver.quit()


# Press the green button in the gutter to run the script.
while True:
    emails = ["abe@gmail.com", "redaaasf@hotmail.com", "redf@hotmail.com"]
    emails_results = check_pwned_list(emails)
    print(list(emails_results))
