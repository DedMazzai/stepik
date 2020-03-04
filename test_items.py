import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_presence_of_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
    time.sleep(30)
    try:
        assert WebDriverWait(browser, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#add_to_basket_form button")))
        print("<<Item found!>>")
    except:
        print("<<O-Oh! Item not found!!!>>")
