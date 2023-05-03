""""
* Author: Cesar M. Gonzalez R.
* CreateAt: 30/04/2023

Base Page
"""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url: str):
        """
        Visit Page

        :param: str url: url website
        """
        self.driver.get(url)

    def _find(self, locator, parent_element: WebElement = None) -> WebElement:
        """
        Find element in page using locator or element

        :param: dict locator: locator dict, By-value
        :param: WebElement parent_element: parent element
        :return: Element found
        :rtype: WebElement
        """
        if parent_element:
            return parent_element.find_element(locator["by"], locator["value"])
        else:
            return self.driver.find_element(locator["by"], locator["value"])

    def _find_elements(self, locator, parent_element: WebElement = None) -> [WebElement]:
        """
        Find elements in page using locator or element

        :param: dict locator: locator dict, By-value
        :param: WebElement parent_element: parent element
        :return: Elements found
        :rtype: [WebElement]
        """
        if parent_element:
            return parent_element.find_elements(locator["by"], locator["value"])
        else:
            return self.driver.find_elements(locator["by"], locator["value"])

    def _click(self, locator=None, element: WebElement = None):
        """
        Click on element

        :param: dict locator: locator dict, By-value
        :param: WebElement element: element
        """
        element.click() if element else self._find(locator).click()

    def _type(self, input_text: str, locator=None, element: WebElement = None, empty_field: bool = False):
        """
        Type in UI field

        :param: str input_text: Text to type
        :param: dict locator: locator dict, By-value
        :param: WebElement element: element
        :param: bool empty_field: flag to define if empty field
        :return: Elements found
        :rtype: [WebElement]
        """
        if locator:
            element = self._find(locator)
        if empty_field:
            element.clear()
        element.send_keys(input_text)

    def _is_displayed(self, locator=None, element: WebElement = None) -> bool:
        """
        Check is element is displayered

        :param: dict locator: locator dict, By-value
        :param: WebElement element: element
        :return: Flag element displayed
        :rtype: bool
        """
        return element.is_displayed() if element else self._find(locator).is_displayed()

    def _get_attribute(self, attribute_name: str, locator=None, element: WebElement = None)-> str:
        """
        Get element attribute

        :param: str attribute_name: Attribute name
        :param: dict locator: locator dict, By-value
        :param: WebElement element: element
        :return: Element attribute value
        :rtype: str
        """
        return element.get_attribute(attribute_name) if element else self._find(locator).get_attribute(attribute_name)

    def _wait_until(self, locator=None, timeout: int = 10):
        """
        Wait until element

        :param: dict locator: locator dict, By-value
        :param: WebElement element: element
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator["by"], locator["value"])))
        except Exception:
            raise Exception
