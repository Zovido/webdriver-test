# !/usr/bin/python
# coding=utf-8
import unittest
import pytest
from selenium import webdriver
from pages.login.LoginPage import LoginPage
from pages.dashboard.DashboardPage import DashboardPage
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-sandbox.apps.htec.rs/")
        loginFromContainer = self.driver.find_element_by_class_name('btn-secondary')
        loginFromContainer.click()

    def test_validate_inputs(self):

        loginPage = LoginPage(self.driver)
        loginPage.submitButton.click()

        # Empty email and password fields
        expected_validation = "Email field is required"
        self.assertEqual(expected_validation, loginPage.get_email_validation(expected_validation))
        expected_validation = "Password is required"
        self.assertEqual(expected_validation, loginPage.get_password_validation(expected_validation))

        # Incorrect user with valid password
        loginPage.enter_login_credentials("aaa@gmail.com", "wrong password")
        loginPage.submitButton.click()
        expected_validation = "User not found"
        self.assertEqual(expected_validation, loginPage.get_email_validation(expected_validation))

        # Incorrect password with valid user
        loginPage.clear_inputs()
        loginPage.enter_login_credentials("stancicmilan06@gmail.com", "wrong password")
        loginPage.submitButton.click()
        expected_validation = "Password incorrect"
        self.assertEqual(expected_validation, loginPage.get_password_validation(expected_validation))

        # Check password for case sensitivity with valid user
        loginPage.clear_inputs()
        loginPage.enter_login_credentials("stancicmilan06@gmail.com", "linkinPARK06")
        loginPage.submitButton.click()
        expected_validation = "Password incorrect"
        self.assertEqual(expected_validation, loginPage.get_password_validation(expected_validation))

        # password must be at least 6 characters long valid user
        loginPage.clear_inputs()
        loginPage.enter_login_credentials("stancicmilan06@gmail.com", "pass")
        loginPage.submitButton.click()
        expected_validation = "Password must be at least 6 characters long"
        self.assertEqual(expected_validation, loginPage.get_password_validation(expected_validation))

        # password must be at least 6 characters long with invalid user
        loginPage.clear_inputs()
        loginPage.enter_login_credentials("yoman@gmail.com", "pass")
        loginPage.submitButton.click()
        expected_validation = "Password must be at least 6 characters long"
        self.assertEqual(expected_validation, loginPage.get_password_validation(expected_validation))

    def test_login_to_sandbox(self):

        loginPage = LoginPage(self.driver)

        loginPage.clear_inputs()
        loginPage.enter_login_credentials("stancicmilan06@gmail.com", "lINKINpARK06")
        loginPage.submitButton.click()

        WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='profile_card_id']"))
        )
        dashboardPage = DashboardPage(self.driver)
        profile_card_title = dashboardPage.get_profile_card_title()
        expected_user = "Stančić Milan"
        self.assertEqual(expected_user, profile_card_title)

    def tearDown(self):
        # close the browser window
        self.driver.quit()
