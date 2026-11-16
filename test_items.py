from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_product_page_has_add_to_basket_button(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )
    button = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")
        )
    )
    assert button.is_enabled(), "Add to basket button should be enabled"
