from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data
import locators
from selenium.webdriver.common.action_chains import ActionChains


class TestUpsRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(test_data.URL_ADRESS)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
    #
    # def testInvalidEmail(self):
    #     driver = self.driver
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.LOG_IN_XPH))).click()
    #     driver.find_element_by_xpath(locators.LOG_IN_XPH).click()
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.REGISTER_XPH))).click()
    #     # Name
    #     name = driver.find_element_by_xpath(locators.NAME_XPH)
    #     name.send_keys(test_data.NAME)
    #     # Last Name
    #     last_name = driver.find_element_by_xpath(locators.LAST_NAME_XPH)
    #     last_name.send_keys(test_data.LAST_NAME)
    #     # Email
    #     email = driver.find_element_by_xpath(locators.EMAIL_XPH)
    #     email.send_keys(test_data.INVALID_EMAIL, Keys.RETURN)
    #     # Error message check
    #     text_error = driver.find_element_by_xpath(locators.EMAIL_ERROR_XPH).text
    #     self.assertEqual(test_data.EMAIL_ERROR, text_error)
    #
    # def testNumberName(self):
    #     driver = self.driver
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.LOG_IN_XPH))).click()
    #     driver.find_element_by_xpath(locators.LOG_IN_XPH).click()
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.REGISTER_XPH))).click()
    #     # Name
    #     name = driver.find_element_by_xpath(locators.NAME_XPH)
    #     name.send_keys(test_data.NUM_NAME, Keys.RETURN)
    #     # Error message check
    #     text_error = driver.find_element_by_xpath(locators.NAME_ERROR_XPH).text
    #     self.assertEqual(test_data.NAME_ERROR, text_error)
    #
    # def testSpecialKeysLastName(self):
    #     driver = self.driver
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.LOG_IN_XPH))).click()
    #     driver.find_element_by_xpath(locators.LOG_IN_XPH).click()
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.REGISTER_XPH))).click()
    #     # Name
    #     name = driver.find_element_by_xpath(locators.NAME_XPH)
    #     name.send_keys(test_data.NAME)
    #     # Last Name
    #     last_name = driver.find_element_by_xpath(locators.LAST_NAME_XPH)
    #     last_name.send_keys(test_data.SPEC_LAST_NAME, Keys.RETURN)
    #     # Error message check
    #     text_error = driver.find_element_by_xpath(locators.LAST_NAME_ERROR_XPH).text
    #     self.assertEqual(test_data.LAST_NAME_ERROR, text_error)
    #
    # def testPasswordCheck(self):
    #     driver = self.driver
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.LOG_IN_XPH))).click()
    #     driver.find_element_by_xpath(locators.LOG_IN_XPH).click()
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locators.REGISTER_XPH))).click()
    #     # Password
    #     password = driver.find_element_by_xpath(locators.PASS_XPH)
    #     password.send_keys(test_data.PASSWORD)
    #     # Password_2
    #     password2 = driver.find_element_by_xpath(locators.PASS_CONFIRM_XPH)
    #     password2.send_keys(test_data.INVALID_PASS, Keys.RETURN)
    #     # Error message check
    #     text_error = driver.find_element_by_xpath(locators.PASS_CORRECTION_XPH).text
    #     self.assertEqual(test_data.PASSWORD_ERROR, text_error)
    # TODO: Test dodawania przedmiogtu do koszyka. Trzeba sprawic aby strona przesunela sie do pierwszego przedmiotu
    # TODO: do kupienia i kliknac w element aby dodac go do koszyka
    def testCounterCheck(self):
        driver = self.driver
        # Checking if the cart is empty
        sleep(2)
        cart = driver.find_element_by_xpath(locators.CART_COUNT_XPH)
        cart_value = cart.text
        self.assertEqual(cart_value, "0")
        driver.find_element_by_xpath(locators.SEARCH_TEXT_XPH).send_keys("drzwi", Keys.RETURN)
        driver.execute_script("window.scrollBy(0, 300)")
        # TODO: Adding 5 items to cart KLIKNIECIE W PRZYCISK DODANIA DO KOSZYKA
        button = driver.find_element_by_xpath(locators.BUY_BUTTON)
        move = ActionChains(driver)
        move.move_to_element(button).perform()
        button.click()
        cart_value = cart.text
        self.assertEqual(cart_value, "1")
        sleep(3)




