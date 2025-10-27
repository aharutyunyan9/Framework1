from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class NonExistingElPage:
    URL = "https://demoqa.com/automation-practice-form"
    GHOST_BTN = (By.ID, "ghostButton")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_ghost_button(self):
        try:
            self.driver.find_element(*self.GHOST_BTN).click()
        except NoSuchElementException:
            print("⚠️ Element with ID 'ghostButton' not found")