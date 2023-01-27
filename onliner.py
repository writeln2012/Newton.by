import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import quickstart


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver.implicitly_wait(10)
    yield chrome_driver
    # chrome_driver.quit()


list = quickstart.main()


def test_other_options(driver):
    driver.get('https://catalog.onliner.by/')
    search_field = driver.find_element(By.CLASS_NAME, 'fast-search__input')
    search_field.send_keys('Акустика Edifier S360DB')
    sleep(3)