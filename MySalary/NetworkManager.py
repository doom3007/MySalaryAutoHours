from tkinter.messagebox import showinfo

from SeleniumRequestManager import SeleniumManager
from selenium.common.exceptions import TimeoutException


class NetworkManager:
    def __init__(self, state_changer):
        self.selenium_manager = None
        self.is_logged_in = False
        self.state_changer = state_changer

    def login(self, entries):
        try:
            if not self.is_logged_in:
                self.selenium_manager = SeleniumManager(username=entries['username'].get(),
                                                        password=entries['password'].get())
                self.is_logged_in = True
            else:
                self.selenium_manager = None
                self.is_logged_in = False
            self.state_changer(self.is_logged_in)
        except TimeoutException as ex:
            self.order_failed('Timeout', 'Error ' + str(ex))

    def report_shift(self, start_date, end_date, comments, override_data=False):
        try:
            self.selenium_manager.report_shift(start_date, end_date, comments)
        except TimeoutException as ex:
            self.order_failed('Timeout', 'Error ' + str(ex))

    def get_last_salary(self):
        try:
            # self.selenium_manager.get_shift()
            # do some_calculation.
            pass
        except TimeoutException as ex:
            self.order_failed('Timeout', 'Error ' + str(ex))

    def order_failed(self, title, exception_string):
        self.is_logged_in = False
        self.state_changer(self.is_logged_in)
        showinfo(title, exception_string)


if __name__ == '__main__':
    pass
