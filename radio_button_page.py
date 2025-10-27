from selenium.webdriver.common.by import By

class RadioButtonPage:
    URL = "https://demoqa.com/radio-button"
    IMPRESSIVE_LABEL = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    IMPRESSIVE_RADIO = (By.ID, "impressiveRadio")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_impressive(self):
        self.driver.find_element(*self.IMPRESSIVE_LABEL).click()

    def is_impressive_selected(self):
        return self.driver.find_element(*self.IMPRESSIVE_RADIO).is_selected()