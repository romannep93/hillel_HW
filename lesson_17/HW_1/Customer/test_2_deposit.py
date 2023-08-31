import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_deposit(driver):
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Customer Login']"))).click()

    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "userSelect")))
    dropdown.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Ron Weasly']"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='deposit()']"))).click()

    amount_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='amount']")))
    amount_field.clear()
    amount_field.send_keys("100500")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='transactions()']"))).click()

    assert "100500" in driver.page_source

    time.sleep(5)
