import pytest

from Pages.dynamic_properties_page import DynamicPropertiesPage
from Pages.radio_button_page import RadioButtonPage
from Pages.non_existing_el_page import NonExistingElPage

@pytest.mark.smoke
@pytest.mark.chrome

def test_dynamic_properties(driver):
    page = DynamicPropertiesPage(driver)
    page.open()
    page.click_enable_after_button()
    print(" Dynamic Properties button clicked")

@pytest.mark.regression
@pytest.mark.firefox

def test_radio_button(driver):
    page = RadioButtonPage(driver)
    page.open()
    page.click_impressive()

    assert page.is_impressive_selected(), "'Impressive' radio button not selected"
    print("'Impressive' radio button is selected")

@pytest.mark.ui
@pytest.mark.edge

def test_non_existing_element(driver):
    page = NonExistingElPage(driver)
    page.open()
    page.click_ghost_button()