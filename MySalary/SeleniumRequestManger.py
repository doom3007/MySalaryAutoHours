from selenium import webdriver


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
        self.driver.get(f'https://{username}:{password}@deshe.matrix.co.il/')


SeleniumManager('idanru', '********', headless=False)
