from datetime import datetime
from . import CssSelectors as cs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


class SeleniumManager:
    def __init__(self, username, password, headless=True):
        self.driver = self.init_chrome_webdrive(headless)
        self.login(username, password)

    @staticmethod
    def init_chrome_webdrive(headless=True):
        """
        Initializing chrome webdriver.
        :param headless: if set to true, the chrome tab will not open up.
        :return driver:
        """
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')
        return webdriver.Chrome(chrome_options=options)

    def login(self, username, password):
        """
        Log into the Deshe page, using basic-auth.
        :param username:
        :param password:
        :return:
        """
        try:
            self.driver.set_page_load_timeout(10)
            self.driver.get(f'https://{username}:{password}@deshe.matrix.co.il/')
        except TimeoutException:
            self.driver.close()
            raise TimeoutException("Timeout. Check your credentials or your internet connection")

    def report_shift(self, start_date: datetime, end_date: datetime):
        """
        Report a shift into a logged in Deshe session.
        :param start_date: Datetime object
        :param end_date: Datetime object
        :return:
        """
        # Due to the Deshe system, cannot report shifts on a couple of days.
        if start_date.month != end_date.month or start_date.day != end_date.day:
            raise ValueError("Cannot report shifts on multiple days")

    def navigate_to_month(self, month, year):
        """
        Navigating the Deshe page to the requested month.
        :param month: the desired month, as a number.
        :param year: number representing the last 2 digits of the dedired year (2019 will be represented as 19)
        :return:
        """
        pass

    def get_current_month(self):
        """
        Get the current displayed month, in numbers.
        :return: number representing the current month
        """
        current_month = self.driver.find_element_by_css_selector(cs.CURRENT_MONTH)
        months_to_numbers = {
            'ינואר': 1,
            'פבואר': 2,
            'מרץ': 3,
            'אפריל': 4,
            'מאי': 5,
            'יוני': 6,
            'יולי': 7,
            'אוגוסט': 8,
            'ספטמבר': 9,
            'אוקטובר': 10,
            'נובמבר': 11,
            'דצמבר': 12,
        }
        return months_to_numbers[current_month]


SeleniumManager('idanru', '123456', headless=False)
