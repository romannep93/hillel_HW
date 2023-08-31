import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_button_disappearance(driver):
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Customer Login']"))).click()

    time.sleep(2)

    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "userSelect")))
    dropdown.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Ron Weasly']"))).click()

    assert len(driver.find_elements(By.XPATH, "//button[text()='Login']")) > 0

    dropdown.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='---Your Name---']"))).click()

    WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.XPATH, "//button[text()='Login']")))

    assert not driver.find_elements(By.XPATH, "//button[text()='Login']")[0].is_displayed()

