import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = '/opt/homebrew/Caskroom/chromedriver/115.0.5790.102/chromedriver-mac-arm64/chromedriver'
    chrome_binary_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument(f'--webdriver-path={chrome_driver_path}')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
