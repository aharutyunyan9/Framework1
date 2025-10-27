from selenium.webdriver.common.by import By

class DynamicPropertiesPage:
    URL = "https://demoqa.com/dynamic-properties"
    ENABLE_AFTER_BTN = (By.ID, "enableAfter")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_enable_after_button(self):
        self.driver.find_element(*self.ENABLE_AFTER_BTN).click()