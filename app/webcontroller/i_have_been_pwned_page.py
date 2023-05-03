""""
* Author: Cesar M. Gonzalez R.
* CreateAt: 30/04/2023

I Have been pwned page controller
"""
import time
from selenium.webdriver.common.by import By
from webcontroller.base_page import BasePage
from constants import EMAIL_REGEX, PHONE_NUMBER_REGEX, I_HAVE_BEEN_PWNED_URL


class IHaveBeenPwnedPage(BasePage):
    # Page elements locator
    _button_pwned = {"by": By.CSS_SELECTOR, "value": 'button[id="searchPwnage"]'}
    _input_email_phone = {"by": By.CSS_SELECTOR, "value": 'input[type="email"]'}
    _pwn_title = {"by": By.CSS_SELECTOR, "value": 'div[class="pwnTitle"]'}
    _good_news_div = {"by": By.CSS_SELECTOR, "value": 'div[id="noPwnage"]'}

    def __init__(self, driver):
        super().__init__(driver)
        print("I Have been pwned page")
        self._visit(I_HAVE_BEEN_PWNED_URL)

    def check_email_phone_data_breach(self, email: str = None, phone: str = None) -> str:
        """
        Check Email/Phone data breach

        :param: str email: email address to validate
        :param: str phone: phone number to validate
        :return: the validation message
        :rtype: str
        """
        global input_reference
        print("Checking Email/Phone data breach")

        # Email and Phone validation
        if email and phone:
            raise "Just email or phone are allowed, not both"

        if not email and not phone:
            raise "None email or phone were provide"

        if email:
            if EMAIL_REGEX.match(email):
                input_reference = email
            else:
                raise f"Invalid email address: {email}"

        if phone:
            if PHONE_NUMBER_REGEX.match(phone):
                input_reference = phone
            else:
                raise f"Invalid phone number: {phone}"

        # Type the Email/Phone
        print(f"Type email/phone: {input_reference}")
        self._type(input_reference, locator=self._input_email_phone, empty_field=True)

        # Click on pwned button
        print("Click on Pwned")
        self._click(self._button_pwned)

        # wait for results 2 seconds
        time.sleep(5)

        # Wait for result
        self._wait_until(self._pwn_title)

        # Extract "Good news" element class attribute
        good_news_div_class_value = self._get_attribute("class", self._good_news_div)
        pwn_result_message = "Good news — no pwnage found!" if "in" in good_news_div_class_value else "Oh no — pwned!"

        print(f"Pwned result: {pwn_result_message}")

        return pwn_result_message
