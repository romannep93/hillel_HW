import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_customer(driver):
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Bank Manager Login']"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[1]"))).click()

    first_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='First Name']")))
    first_name_field.clear()
    first_name_field.send_keys("John")

    last_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Last Name']")))
    last_name_field.clear()
    last_name_field.send_keys("Smith")

    post_code_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Post Code']")))
    post_code_field.clear()
    post_code_field.send_keys("123456")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    time.sleep(2)

    expected_text = "Customer added successfully"
    alert_text = driver.switch_to.alert.text
    assert expected_text in alert_text, f"Expected :'{expected_text}'\nActual"
