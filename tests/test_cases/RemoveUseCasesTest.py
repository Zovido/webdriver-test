import unittest
from selenium import webdriver
from pages.login.LoginPage import LoginPage
from pages.dashboard.DashboardPage import DashboardPage
from pages.usecases.UseCasesPage import UseCasesPage
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class RemoveUseCasesTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-sandbox.apps.htec.rs/dashboard")
        loginFromContainer = self.driver.find_element_by_class_name('btn-secondary')
        loginFromContainer.click()
        WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit_btn']"))
        )
        loginPage = LoginPage(self.driver)
        loginPage.enter_login_credentials("stancicmilan06@gmail.com", "lINKINpARK06")
        loginPage.submitButton.click()

    def testCreateUseCases(self):
        WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='use_cases_card_id']"))
        )
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.use_cases_card.click()

        use_cases_page = UseCasesPage(self.driver)
        while use_cases_page.get_num_of_use_cases() > 0:
            use_case_page = use_cases_page.get_first_use_case()
            use_case_page.remove()
            #use_cases_page = UseCasesPage(self.driver)